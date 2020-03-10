スターターキット

python 3.8
Django 2.2.6
MySQL 5.8
Nginx 1.13

```
mkdir mysql
```
##現在はこの状態

```
django
├── docker-compose.yml
├── mysql
├── sql
│   └── init.sql
├── nginx
│   ├── conf
│   │   └── config_nginx.conf
│   └── uwsgi_params
└── python
    ├── Dockerfile
    └── requirements.txt
```

##プロジェクト開始

```
docker-compose run python django-admin.py startproject config .
```

##実行の結果

```
django
├── docker-compose.yml
├── mysql
├── sql
├── nginx
│   ├── conf
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

##setting.pyに記述

```setting.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
    }
}
```

##マイグレーション

```
docker-compose run python ./manage.py makemigrations
docker-compose run python ./manage.py migrate
```

##管理者作成

```
docker-compose run python ./manage.py createsuperuser
```

##コンテナ起動、確認

```
docker-compose up -d
```

→http://localhost:8000
→http://localhost:8000/admin

##css適用、setting.pyの最終行に記述

```
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static'
```

staticファイルを集約コピー

```
docker-compose run python ./manage.py collectstatic
```

##コンテナ再起動、確認

```
docker-compose up -d
```
→http://localhost:8000/admin

3台のサーバーが起動できました。src内にdjango-admin.py startprojectしてはじめてください。
以上です。
