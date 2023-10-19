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
 vim uwsgi.ini  修改为正确的配置
 #启动
uwsgi --ini uwsgi.ini
#停止
uwsgi --stop uwsgi.pid
# 查看日志
tail -f uwsgi.log
```

# 运行

```
http://hostname:8000/apikey    修改为自己的apikey
http://hostname:8000/chat     进入ai聊天界面
```

![avatar](http://www.zdnwork.cn/image_show/c0175272-6e1e-11ee-9b3f-00163e064bf4.png)

