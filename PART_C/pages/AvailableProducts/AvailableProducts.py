from flask import Blueprint, render_template, jsonify, session
from PART_C.mongodrafts import products_col  # Assuming this import is correct
from bson import Binary
import base64  # Import base64 module for encoding
AvailableProducts = Blueprint(
    'AvailableProducts', __name__,
    static_folder='static',
    static_url_path='/AvailableProducts',
    template_folder='templates'
)
@AvailableProducts.route('/AvailableProducts')
def available_products():
    amount = session.get('amount')
    cbd = session.get('cbd')
    thc = session.get('thc')
    shape = session.get('shape')

    if not all([amount, cbd, thc, shape]):
        return jsonify({'error': 'Missing parameters'}), 400

    product = products_col.find_one({'CBD': cbd, 'THC': thc})
    if product:
        shape = product.get('צורה')
        product_name = product.get('שם')
        image_binary = product.get('תמונה')

        print(f"Product Name: {product_name}")
        print(f"Image Binary: {image_binary}")

        if isinstance(image_binary, str):
            # Convert string to bytes assuming it's encoded in UTF-8
            image_binary = image_binary.encode('utf-8')

        if image_binary:
            # Convert binary image data to base64 encoding
            image_base64 = base64.b64encode(image_binary).decode('utf-8')
        else:
            image_base64 = None

        # Pass data to the template for rendering
        return render_template('AvailableProducts.html', amount=amount, cbd=cbd, thc=thc, shape=shape,
                               product_name=product_name, image_base64=image_base64)
    else:
        return jsonify({'error': 'Product not found'}), 404

