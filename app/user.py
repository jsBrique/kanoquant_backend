from flask import Blueprint,request, render_template, abort,redirect
from jinja2 import TemplateNotFound
import json
from flask_login import LoginManager,login_required,UserMixin,login_user,logout_user,current_user
from werkzeug.security import generate_password_hash,check_password_hash

USERS = [
    {
        "id": 114514,
        "username": 'dobriq',
        "password": generate_password_hash('Brick233$')
    },
    {
        "id": 2,
        "username": 'tom',
        "password": generate_password_hash('123')
    }
]
class User(UserMixin):
    def __init__(self,user):
        self.username = user.get("username")
        self.password = user.get("password")
        self.id=user.get("id")
    def verify_password(self,password):
        return check_password_hash(self.password,password)
    
    def get_id(self):
        return self.id
    
    def get(user_id):
        if not user_id:
            return None
        for user in USERS:
            if user.get("id")==user_id:
                return User(user)
        return None
    


login_manager = LoginManager()
login_manager.login_view='users.userlogin'
@login_manager.user_loader
def load_user(user_id):
    return User.get(int(user_id))

user_page = Blueprint('users', 'users', template_folder='templates')
    #     from flask_httpauth import HTTPTokenAuth
    #     auth = HTTPBasicAuth()

@user_page.route('/login')
def userlogin():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@user_page.route('/logincheck',methods=['POST'])
def logincheck():
    data = request.get_json()

    for u in USERS:
        if u['username']==data['username'] and check_password_hash(u['password'],data['password']):
            user=User(u)
            login_user(user)
            res={'username':u['username'],'Login':True}
            return json.dumps(res)
    res={'username':data['username'],'Login':False}
    return json.dumps(res)


@user_page.route('/test',methods=['POST'])
@login_required
def test():
    try:
        #logout_user()
        return json.dumps({'page':'test'})#render_template('index.html')
    except TemplateNotFound:
        abort(404)

@user_page.route('/logout',methods=['POST'])
@login_required
def logout():
    logout_user()
    return json.dumps({'login_state':False})

@user_page.route('/check',methods=['GET','POST'])
def check():
    #print(current_user)
    print('check')
    if current_user.is_authenticated:
        return json.dumps({'state':True,'username':current_user.username})
    else:
        return json.dumps({'state':False,'username':'Unknow'})