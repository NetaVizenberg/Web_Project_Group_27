from flask import Blueprint, render_template, request, redirect, url_for,session
from PART_C.mongodrafts import user_col
CreatAnAccount = Blueprint(
    'CreatAnAccount', __name__,
    static_folder='static',  # Adjust if needed for static files
    static_url_path='/CreatAnAccount',  # Adjust if needed for static files
    template_folder='templates'  # Adjust if needed for templates
)




@CreatAnAccount.route('/CreatAnAccount', methods=['GET', 'POST'])
def creat_an_account():
    if request.method == 'GET':
        # Display the registration form (already handled by CreatAnAccount.html)

        return render_template('CreatAnAccount.html')
    elif request.method == 'POST':
        print("post is activated")

        # Process user registration using data from the form
        email = request.form.get("email")
        password = request.form.get("password")
        first_name = request.form.get("first_name")  # Assuming space in the name
        last_name = request.form.get("last_name")  # Assuming space in the name
        age = request.form.get("age")
        phone_number = request.form.get("phone_number")


        existing_user = user_col.find_one({'דוא"ל': email})
        print(email)
        if existing_user:
            print(f"Error: User with email {email} already exists. Please choose a different email.")
            # Handle the error and display an appropriate message
            return render_template('error.html',
                                   message="User already exists with this email. Please choose a different email.")
        else:
            # Create a new user and insert it into the 'users' collection
            new_user = {
                'דוא"ל': email,
                'סיסמא': password,
                'שם פרטי': first_name,
                'שם משפחה': last_name,
                'גיל': age,
                'מספר טלפון': phone_number
            }

            user_col.insert_one(new_user)
            session['email'] = email
            session['first_name'] = first_name
            session['last_name'] = last_name
            session['phone_number'] = phone_number

            print(f"Account for {email} created successfully.")
            # Redirect to the success page


            return redirect(url_for('CreatAnAccount.registration_success'))
        # Implement validation and error handling (important!)
        # Validate each field (email format, password strength, etc.)
        # Check if user already exists (database query)

        # Handle any potential errors and display appropriate messages

        # If registration is successful, process further
        # (e.g., create user account in database, send confirmation email)

        # For now, assume successful registration and redirect to a success page


    # Handle other HTTP methods if needed (unlikely in this case)


@CreatAnAccount.route('/registration_success')
def registration_success():
    # Display a success message or redirect to a relevant page
    return render_template('registration_success.html')  # Create this template

