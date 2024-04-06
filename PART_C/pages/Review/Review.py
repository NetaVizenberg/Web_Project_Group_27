from flask import Blueprint, render_template

Review= Blueprint(
    'Review', __name__,
    static_folder='static',
    static_url_path='/Review',
    template_folder='templates'
)

@Review.route('/Review')
def review():
    return render_template("Review.html")