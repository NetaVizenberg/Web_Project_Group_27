from flask import Blueprint,render_template



# homepage blueprint definition
HomePage = Blueprint(
    'HomePage',__name__,
    static_folder='static',
    static_url_path='/HomePage',
    template_folder='templates'
)


# Routes
@HomePage.route('/')
def homePage():
    return render_template('HomePage.html')



