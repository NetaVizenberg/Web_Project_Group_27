import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from settings import DB_URI
from bson import Binary

uri = DB_URI
# Create a new client and connect to the server
cluster = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

mydb = cluster['mydb']
products_col = mydb['products']
user_col = mydb['users']


def insert_products():
    products = [
        {'שם': 'Green Dream', 'כמות': 5, 'CBD': 5, 'THC': 15, 'צורה': 'פרח', 'דירוג': 7, 'תמונה': 'Green Dream.jpg'},
        {'שם': 'Pineapple Haze', 'כמות': 10, 'CBD': 2, 'THC': 20, 'צורה': 'שמן', 'דירוג': 8, 'תמונה': 'Pineapple Haze.jpg'},
        {'שם': 'Kush Blush', 'כמות': 3, 'CBD': 8, 'THC': 10, 'צורה': 'פרח', 'דירוג': 6, 'תמונה': 'Kush Blush.jpg'},
        {'שם': 'Chronic Cloud', 'כמות': 8, 'CBD': 6, 'THC': 18, 'צורה': 'שמן', 'דירוג': 9,'תמונה':'Chronic Cloud.png'},
        {'שם': 'Sativa Serenity', 'כמות': 12, 'CBD': 3, 'THC': 25, 'צורה': 'פרח', 'דירוג': 7,'תמונה': 'Sativa Serenity.png'},
        {'שם': 'Indica Oasis', 'כמות': 6, 'CBD': 10, 'THC': 12, 'צורה': 'שמן', 'דירוג': 8,'תמונה': 'Indica Oasis.png'},
        {'שם': 'Lemon Skunk', 'כמות': 4, 'CBD': 12, 'THC': 8, 'צורה': 'פרח', 'דירוג': 5, 'תמונה': 'Lemon Skunk.png'},
        {'שם': 'Blueberry Bliss', 'כמות': 15, 'CBD': 4, 'THC': 22, 'צורה': 'שמן', 'דירוג': 10,'תמונה': 'Blueberry Bliss.png'},
        {'שם': 'Northern Lights Nirvana', 'כמות': 7, 'CBD': 7, 'THC': 16, 'צורה': 'פרח', 'דירוג': 7,'תמונה': 'Northern Lights Nirvana.png' },
        {'שם': 'Purple Kush Paradise', 'כמות': 9, 'CBD': 9, 'THC': 14, 'צורה': 'פרח', 'דירוג': 8,'תמונה': 'Purple Kush Paradise.png'},
    ]
    for product in products:
        image_filename = product['תמונה']
        image_path = os.path.join(os.path.dirname(__file__),'pics','Images' , image_filename)
        print(f"Checking image path: {image_path}")  # Debugging statement
        if os.path.exists(image_path):
            with open(image_path, 'rb') as image_file:
                # Read the image file as binary data
                image_binary = Binary(image_file.read())
                # Update the product data to include the image binary
                product['תמונה'] = image_binary
                # Insert the product data into MongoDB
                products_col.insert_one(product)
                print(f"Product '{product['שם']}' inserted successfully.")
        else:
            print(f"Image not found for product '{product['שם']}' at path: {image_path}")

    # Call the function to insert products

#insert_products()

# Call the function to insert products
#insert_products()
#products_col.drop()


def sort_products(field, order):
    # Sort products based on the specified field and order
    sorted_products = list(products_col.find().sort(field, order))

    # Print the sorted products
    print(f"Products Sorted by {field.capitalize()}:")
    for product in sorted_products:
        print(product)
#call the function and see the sorted products by rating
#sort_products("דירוג", pymongo.DESCENDING)
#call the function and see the sorted products by amount
#sort_products("כמות", pymongo.DESCENDING)
# call the function and see the sorted products by THC
#sort_products("THC", pymongo.DESCENDING)
#call the function and see the sorted products by CBD
#sort_products("CBD", pymongo.DESCENDING)

def update_rating_by_name(product_name, new_rating):
    if 0 <= new_rating <= 10:
        # Update product's rating based on the product name
        products_col.update_one({'שם': product_name}, {'$set': {'דירוג': new_rating}})
        print(f"Product '{product_name}' updated to rating {new_rating} successfully.")
    else:
        print("Error: Invalid rating. The rating should be between 0 and 10 (inclusive).")

#Example usage:
#update_rating_by_name('Green Dream', 9)  # Update the rating of 'Green Dream' to 9
#update_rating_by_name('Green Dream', 11)  # Update the rating of 'Green Dream' to 9


def insert_users():
   users = [

      { 'דוא"ל':"idan@example.com","סיסמא":"12345678","שם פרטי": "עידן","שם משפחה":"כהן","גיל":25,"מספר טלפון":"0501234567"},
      { 'דוא"ל':"noa@example.com","סיסמא":"abcd1234","שם פרטי":"נועה","שם משפחה":"לוי","גיל":30,"מספר טלפון":"0522345678"},
      { 'דוא"ל':"tamar@example.com","סיסמא":"qwerty1234","שם פרטי":"תמר","שם משפחה":"פרידמן","גיל":22,"מספר טלפון":"0543456789"},
      { 'דוא"ל':"michael@example.com","סיסמא":"!@#*4567","שם פרטי":"מיכאל","שם משפחה":"דוד","גיל":35,"מספר טלפון":"0584567890"},
      { 'דוא"ל':"yael@example.com","סיסמא":"6789qwex","שם פרטי":"יעל","שם משפחה":"אברהם","גיל":28,"מספר טלפון":"0535678901"},
      { 'דוא"ל':"david@example.com","סיסמא":"poiuytrewq","שם פרטי":"דוד","שם משפחה":"כהן","גיל":40,"מספר טלפון":"0506789012"},
      { 'דוא"ל':"sara@example.com","סיסמא":"zxcvbnm1","שם פרטי":"שרה","שם משפחה":"לוי","גיל":20,"מספר טלפון":"0527890123"},
      { 'דוא"ל':"ron@example.com","סיסמא":"1qaz2wsx","שם פרטי":"רון","שם משפחה":"אלקיים","גיל":32,"מספר טלפון":"0548901234"},
      { 'דוא"ל':"dana@example.com","סיסמא": "asdfghjkl","שם פרטי":"דנה","שם משפחה":"בן דוד","גיל":27,"מספר טלפון":"0509012345"},
      { 'דוא"ל':"lior@example.com","סיסמא": "mnbvcxz","שם פרטי": "ליאור","שם משפחה": "פרץ","גיל": 38,"מספר טלפון": "0531234567"}

   ]

   user_col.insert_many(users)
   print("Data inserted into 'users' collection successfully.")

#insert_users()

def drop_all_users():
    # Use drop() to remove the entire 'users' collection
    user_col.drop()

    print("'users' collection dropped successfully.")
#drop_all_users()



def sort_users_by_rating():
    # Sort products by rating in ascending order
    sorted_users = list(user_col.find().sort("גיל", pymongo.DESCENDING))

    # Print the sorted products
    print("Products Sorted by Rating:")
    for user in sorted_users:
        print(user)

#sort_users_by_rating()
def update_user_email(old_email, new_email):
    # Update user's email based on the old email
    user_col.update_one({'דוא"ל': old_email}, {'$set': {'דוא"ל': new_email}})
    print(f"User with email {old_email} updated to {new_email} successfully.")

#Example usage:
#update_user_email("idan@example.com", "new_idan@example.com")
def delete_user_by_email(email):
    # Delete user based on the email
    result = user_col.delete_one({'דוא"ל': email})

    # Check if the document was deleted successfully
    if result.deleted_count > 0:
        print(f"User with email {email} deleted successfully.")
    else:
        print(f"User with email {email} not found.")

# Example usage:
# delete_user_by_email("idan@example.com")

