from flask import Blueprint,render_template
FollowUs = Blueprint(
    'FollowUs', __name__,
    static_folder='static',
    static_url_path='/FollowUs',
    template_folder='templates'
)
@FollowUs.route('/FollowUs')
def followUs():
 return render_template("FollowUs.html")
