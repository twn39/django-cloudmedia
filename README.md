## Cloud media manager for django

![pypi](https://img.shields.io/pypi/v/django-cloudmedia?style=flat-square)
![python](https://img.shields.io/pypi/pyversions/django-cloudmedia?style=flat-square)
![wheel](https://img.shields.io/pypi/wheel/django-cloudmedia?style=flat-square)
![l](https://img.shields.io/pypi/l/django-cloudmedia?style=flat-square)
![](https://img.shields.io/pypi/djversions/django-cloudmedia?style=flat-square)
[![Maintainability](https://api.codeclimate.com/v1/badges/031dbadae356adf0f2d0/maintainability)](https://codeclimate.com/github/twn39/django-cloudmedia/maintainability)


Support for aliyun OSS, Tencent COS, Huawei OBS 

### Install

```shell
pip install django-cloudmedia
```

add `settings.py`:

```py
INSTALLED_APPS = [
    'cloudmedia',
    ...
]
```


### Usage

**Configure**

add `settings.py`:

```python
# set the default cloud object storage
DEFAULT_FILE_STORAGE = 'cloudmedia.storage.obs.OBSStorage'

COS_SECRET_ID = ''
COS_SECRET_KEY = ''
COS_REGION = 'ap-shanghai'
COS_SCHEME = 'https'
COS_BUCKET = ''
COS_BASE_URI = '' # for image access domain

# Ali OSS storage
OSS_ACCESS_KEY_ID = ''
OSS_ACCESS_KEY_SECRET = ''
OSS_BUCKET = ''
OSS_END_POINT = 'oss-cn-shanghai.aliyuncs.com'
OSS_BASE_URI = ''

# Huawei OBS storage
OBS_ACCESS_KEY_ID = ''
OBS_ACCESS_KEY_SECRET = ''
OBS_BUCKET = ''
OBS_END_POINT = 'obs.cn-east-3.myhuaweicloud.com'
OBS_BASE_URI = ''
```

**Sync the database tables**

```shell
python manager.py migrate
```

Then just access the django admin backend.