import os
from flask import Flask
from flask_pymongo import PyMongo
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)


# My DB on MongoDB
app.config["MONGO_DBNAME"] = 'adventurers'
# SECRET_KEY variable
app.config["MONGO_URI"] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


