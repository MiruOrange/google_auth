# google_auth - 使用ngrok解鎖Google Auth 2.0的力量！

## 跨入無縫測試的領域

準備好，這是用**ngrok**測試Google OAuth 2.0的終極指南，就像一個數字巫師一樣！通過這個秘法設置，你謙遜的本地項目將超越平凡的 `127.0.0.1:8000`，成為在地球各個角落都可見的燈塔，這一切都通過**ngrok**的魔力實現。再也不用擔心你的localhost在第三方API眼中只是凡人了！

## 使用的古老技術
- **ngrok** - 通往數字領域的大門。
- **Docker Compose** - 輕鬆召喚你的容器。
- **Google Cloud Console** - 通往雲端諸神的入口。
- **nginx** - 你的虛擬領域的守護者。

## 專案說明

以前在本地啟動專案時，你的網址可能會長這樣：127.0.0.1:8000。即使你使用了nginx，網址最多變成localhost，但無法像這樣變成https://yourwebsite.com。現在使用**ngrok**，可以立刻把測試網址變成正式網址，讓世界各地都可以存取。

## 使用ngrok的好處

當測試第三方API時，經常會遇到跳轉到第三方驗證或授權後，需返回原網頁的情況。如果你使用localhost網址，第三方API可能無法正常跳轉回來。例如Google OAuth 2.0或綠界刷卡等情況。此時，**ngrok**就是你的救世主。

## 專案使用時的改動指南

1. **ngrok的NGROK_AUTHTOKEN環境變數**：請自行到ngrok註冊免費帳號取得token，並在docker-compose.yml中進行修改。
2. **Google Cloud Console**：建立專案，獲取專案的client_id和client_secret。
3. **修改專案配置**：打開`api_mod_google_auth.py`，修改`GOOGLE_CLIENT_ID`和`GOOGLE_CLIENT_SECRET`為你的憑證。
4. **初次設置Google Cloud Console**：在專案的Authorized JavaScript origins中，先隨便填寫一個URL，比如`https://google.com`。
5. **Authorized redirect URLs**：同樣，隨便填寫一個URL，比如`https://google.com`。

當你準備好正式啟動**ngrok**並獲取真實網址後，請回到專案中，按照以下步驟進行調整。

## 神聖操作順序
1. 祭出`docker compose up -d --build`命令，打包image檔案並啟動container。
2. 登入**ngrok**，查看Agents，找到目前啟用分配的神秘網址。
3. 修改專案中的`api_mod_google_auth.py`中的`REDIRECT_URL`為新獲取的網址。
4. 回到Google Cloud Console專案中，將Authorized JavaScript origins的URL修改為你的ngrok網址，例如：`https://27e7-185.ngrok-free.app`。
5. 將Authorized redirect URLs修改為：`https://27e7-185.ngrok-free.app/authorize`。
6. 存檔，一切完成，大功告成！

以此秘法，你將無縫進行Google Auth 2.0測試，享受每一秒的成功感！
