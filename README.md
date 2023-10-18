# 环境

python3 -m venv env
source env/bin/activate
 建议pip源  -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

pip install -r requirement.txt

//pip freeze > requirements.txt

# 部署

## 数据库

python manage.py migrate
python manage.py createsuperuser



# 测试

python manage.py runserver 0.0.0.0:8000

# 托管

```markup
 #启动
uwsgi --ini uwsgi.ini
#停止
uwsgi --stop uwsgi.pid
# 查看日志
tail -f uwsgi.log
```