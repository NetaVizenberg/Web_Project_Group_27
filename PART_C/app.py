from flask import Flask
from settings import SECRET_KEY
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.secret_key= SECRET_KEY
from pages.Prescription.Prescription import Prescription
app.register_blueprint(Prescription)
from pages.AvailableProducts.AvailableProducts import AvailableProducts
app.register_blueprint(AvailableProducts)
from pages.CreatAnAccount.CreatAnAccount import CreatAnAccount
app.register_blueprint(CreatAnAccount)
from pages.ContactUs.ContactUs import ContactUs
app.register_blueprint(ContactUs)
from pages.Review.Review import Review
app.register_blueprint(Review)
from pages.FollowUs.FollowUs import FollowUs
app.register_blueprint(FollowUs)
from pages.HomePage.HomePage import HomePage
app.register_blueprint(HomePage)
from pages.MyAccount.MyAccount import MyAccount
app.register_blueprint(MyAccount)

if __name__ == '__main__':
    app.run(debug=True)
