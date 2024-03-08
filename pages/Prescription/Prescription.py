from flask import Blueprint, render_template

Prescription = Blueprint(
    'Prescription', __name__,
    static_folder='static',
    static_url_path='/Prescription',
   template_folder='templates'
)


@Prescription.route('/')
@Prescription.route('/Prescription')
def index():
    return render_template('Prescription.html')