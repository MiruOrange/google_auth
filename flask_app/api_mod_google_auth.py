import requests


GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

# Google OAuth 2.0 配置
GOOGLE_CLIENT_ID = "Your google client id"
GOOGLE_CLIENT_SECRET = "Your google client secret"

# 回呼網址
REDIRECT_URL = "https://yourwebsite/authorize"

# 取得 Google OAuth 2.0 設定 (這裡包含各個端點的 URL)
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
    

# 取得user的資料
def get_user_info(access_token):
    # 取得 Google OAuth 2.0 設定
    google_provider_cfg = get_google_provider_cfg()

    # 取得 user info
    user_info_endpoint = google_provider_cfg["userinfo_endpoint"]
    url = f"{user_info_endpoint}?access_token={access_token}"
    userinfo_response = requests.get(url)
    user_info = userinfo_response.json()

    i_email = user_info.get('email')
    user_picture_url = user_info.get('picture')  # 取得用戶的頭像 URL

    return i_email, user_picture_url