from flask import Blueprint, render_template, redirect, url_for

AvailableProducts = Blueprint(
    'AvailableProducts', __name__,
    static_folder='static',
    static_url_path='/AvailableProducts',
    template_folder='templates'
)

@AvailableProducts.route('/')
def index():
    # Redirect to the 'available_products' route
    return redirect(url_for('AvailableProducts.available_products'))

@AvailableProducts.route('/AvailableProducts')
def available_products():
    # Render the 'AvailableProducts.html' template
    return render_template('AvailableProducts.html')