
・logout機能 完成だけど、リダイレクト先の表示に問題あり
　|
　|ユーザー nodaken としてログインしました。
　|ログアウトしました。
　|
　みたいな感じ


--コマンド-------------------------------------------------

...@...$ docker-compose build && docker-compose up -d && docker-compose exec web bash

root@...# python manage.py makemigrations && python manage.py migrate


--確認用url-------------------------------------------------

http://localhost:18000/accounts/signup/

http://localhost:18000/accounts/login/

http://localhost:18000/api/