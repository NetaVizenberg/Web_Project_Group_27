from flask import Blueprint, render_template, redirect, url_for

CreatAnAccount = Blueprint(
    'CreatAnAccount', __name__,
    static_folder='static',
    static_url_path='/CreatAnAccount',
    template_folder='templates'
)


@CreatAnAccount.route('/')
def index():
    # Redirect to the 'creat_an_Account' route
    return redirect(url_for('CreatAnAccount.creat_an_account'))


@CreatAnAccount.route('/CreatAnAccount')
def creat_an_account():
    # Render the 'CreatAnAccount.html' template
    return render_template('CreatAnAccount.html')
