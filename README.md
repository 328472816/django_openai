### 虚拟环境

python3 -m venv env
source env/bin/activate
 建议pip源  -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
### 部署
python manage.py migrate
python manage.py createsuperuser

### 测试
python manage.py runserver 0.0.0.0:8000

### 生产