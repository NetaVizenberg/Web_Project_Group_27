from flask import Blueprint,render_template
ContactUs = Blueprint(
    'ContactUs', __name__,
    static_folder='static',
    static_url_path='/ContactUs',
    template_folder='templates'
)
@ContactUs.route('/ContactUs')
def contact_us():
 return render_template("ContactUs.html")