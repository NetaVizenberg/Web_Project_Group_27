from flask import Blueprint, render_template, request, redirect, url_for,session
from PART_C.mongodrafts import products_col

Prescription = Blueprint(
    'Prescription', __name__,
    static_folder='static',
    static_url_path='/Prescription',
    template_folder='templates'
)


@Prescription.route('/Prescription', methods=['GET', 'POST'])
def prescription():
    if request.method == 'GET':
        # Render the prescription form
        return render_template('Prescription.html')
    elif request.method == 'POST':
        # Process form submission
        amount_str = request.form.get('amount')
        cbd_str = request.form.get('CBD')
        thc_str = request.form.get('THC')
        shape_str = request.form.get('shape')  # Get the shape value from the form

        # Convert strings to integers
        session['amount'] = int(amount_str) if amount_str else None
        session['cbd'] = int(cbd_str) if cbd_str else None
        session['thc'] = int(thc_str) if thc_str else None
        session['shape'] = shape_str if shape_str else None

        # Retrieve values from session
        amount = session.get('amount')
        cbd = session.get('cbd')
        thc = session.get('thc')
        shape = session.get('shape')

        if cbd is not None and thc is not None:
            existing_product = products_col.find_one({'CBD': cbd, 'THC': thc})
            if existing_product:
                # If product found, redirect to AvailableProducts page with product information
                return redirect(url_for('AvailableProducts.available_products'))

        # If product not found or missing CBD and THC values, display a message
        message = "המוצר לא נמצא "
        return render_template('Prescription.html', message=message)

