# -*- coding: utf-8 -*-
import logging,logging.handlers
from flask import Flask, redirect, url_for, session, request, jsonify
import requests
import os
import api_mod_google_auth as amga

app = Flask(__name__)

# 設定日誌級別
app.logger.setLevel(logging.INFO)

# 設定密鑰
app.secret_key = "your_secret_key"  # 替換為你自己的密鑰, or使用 os.getenv("SECRET_KEY")

# 配置 Flask 的日誌
log_handler = logging.StreamHandler()  # 使用 StreamHandler 將日誌輸出到標準輸出
log_handler.setLevel(logging.DEBUG)      # 設置日誌級別，例如 DEBUG、INFO、ERROR
app.logger.addHandler(log_handler)

# 首頁
@app.route('/')
def index():
    # 從 session 中取得 user_info，如果不存在則為 None
    user_info = session.get('user')
    
    if user_info:
        return f"""
            <h1>Welcome {user_info['name']}!</h1>
            <p>Email: {user_info['email']}</p>
            <img src="{user_info['picture']}" alt="Profile picture">
            <p><a href="/logout">Logout</a></p>
        """
    else:
        return '<a href="/login">Login with Google</a>'

# 登入路由
@app.route('/login')
def login():
    # 取得 Google OAuth 2.0 的所有endpoint
    google_provider_cfg = amga.get_google_provider_cfg()

    # 取得authorization的endpoint
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # 生成授權 URL，讓使用者授權應用程式
    request_uri = (
        f"{authorization_endpoint}?response_type=code"
        f"&client_id={amga.GOOGLE_CLIENT_ID}"
        f"&redirect_uri={amga.REDIRECT_URL}"  # 使用手動指定huma 的回調 URL
        f"&scope=openid%20email%20profile"
    )
    return redirect(request_uri)

@app.route('/authorize')
def authorize():
    code = request.args.get("code")
    google_provider_cfg = amga.get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # 用授權碼交換 access token
    token_url = token_endpoint
    token_data = {
        "code": code,
        "client_id": amga.GOOGLE_CLIENT_ID,
        "client_secret": amga.GOOGLE_CLIENT_SECRET,
        "redirect_uri": f"{amga.REDIRECT_URL}",
        "grant_type": "authorization_code"
    }
    token_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_response = requests.post(token_url, data=token_data, headers=token_headers)
    token_response_json = token_response.json()

    # 打印出 token 回應，檢查回應是否正確
    app.logger.info(f'token_response_json: {token_response_json}')
    print(token_response_json)

    if "access_token" not in token_response_json:
        return f"Error: {token_response_json.get('error_description', 'No access token received')}"

    # 取得使用者資訊
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri = f"{userinfo_endpoint}?access_token={token_response_json['access_token']}"
    userinfo_response = requests.get(uri)

    user_info = userinfo_response.json()

    # 儲存使用者資訊到 session
    session['user'] = user_info

    return redirect('/')


# 登出路由
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')