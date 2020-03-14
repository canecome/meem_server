
# NAME

meem - API dashboards

# Features

API Xross Platform

# DEMO
 
comming soon

# Requirement
 
* Django==2.2.10
* uwsgi==2.0.17
* mysqlclient==1.4.6
 
# Installation
 
```bash
docker-compose up -d
```

# Usage

```
meem_server
├── docker-compose.yml
├── mysql
├── sql
├── nginx
│   ├── config
│   │   └── config_nginx.conf
│   └── uwsgi_params
├── python
│   ├── Dockerfile
│   └── requirements.txt
├── src
│   ├── config
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
└── static
```
 
# Note
 
DBマイグレーション方法

```
docker-compose run python ./manage.py makemigrations
docker-compose run python ./manage.py migrate
```

DB管理者作成方法

```
docker-compose run python ./manage.py createsuperuser
```

##仮想サーバー再起動、確認

```
docker-compose up -d
```

→http://localhost:8000
→http://localhost:8000/admin


CSSが反映されない場合

```
docker-compose run python ./manage.py collectstatic
```

new app start

```
docker-compose run python ./manage.py startapp [app name]
```

# Author

* [@canecome](https://twitter.com/canecome)
* URL:www.picros.com
 
# License

"meem" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
