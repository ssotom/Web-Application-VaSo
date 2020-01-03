# Web Application VaSo

_Prototype of a web application that collects customer information and their opinion of some products. For this project django was used in backend, Vue in the fronted and mongoDB as database. This web application has authentication with JTW_

DEMO: https://vasapplication.herokuapp.com/

### Prerequisites 📋

```
Python 3.6
pip
virtualenv
Node.js
```

### installation 🔧

Web-Application-VaSo/
```
virtualenv %HOMEPATH%\eb-virt
source ~/eb-virt/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
Web-Application-VaSo/frontend
```
npm install
npm build
```
Web-Application-VaSo/
```
python manage.py runserver
```
