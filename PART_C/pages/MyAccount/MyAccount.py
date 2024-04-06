from flask import Blueprint,render_template
MyAccount= Blueprint(
    'MyAccount', __name__,
    static_folder='static',
    static_url_path='/MyAccount',
    template_folder='templates'
)
@MyAccount.route('/MyAccount')
def myAccount():
 return render_template("MyAccount.html")
