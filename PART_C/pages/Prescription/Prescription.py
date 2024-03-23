from flask import Blueprint, render_template, redirect, url_for, request
from mongodrafts import products_col

Prescription = Blueprint(
    'Prescription', __name__,
    static_folder='static',
    static_url_path='/Prescription',
    template_folder='templates'
)


@Prescription.route('/')
def index():
    # Redirect to the registration form
    return redirect(url_for('Prescription.prescription'))


@Prescription.route('/Prescription', methods=['GET', 'POST'])
def prescription():
    if request.method == 'POST':

        # Extract CBD and THC values from the form submission
        cbd_str = request.form.get('CBD')
        thc_str = request.form.get('THC')

        # Convert CBD and THC values to integers
        cbd = int(cbd_str)
        thc = int(thc_str)

        # Query the database for the product
        existing_product = products_col.find_one({'CBD': cbd, 'THC': thc})

        if existing_product:
            # If product found, redirect to AvailableProducts page with product information
            return redirect(url_for('AvailableProducts', product_id=existing_product['_id']))
        else:
            # If product not found, display a message
            print("product not found")
            return render_template('Prescription.html', message="Product not found.")

