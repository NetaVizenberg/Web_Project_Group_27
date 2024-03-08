from flask import Flask
app = Flask(__name__)


from pages.Prescription.Prescription import Prescription
app.register_blueprint(Prescription)
from pages.AvailableProducts.AvailableProducts import AvailableProducts
app.register_blueprint(AvailableProducts)
from pages.CreatAnAccount.CreatAnAccount import CreatAnAccount
app.register_blueprint(CreatAnAccount)
