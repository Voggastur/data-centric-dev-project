import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

# My environment variables
app.config["MONGO_DBNAME"] = 'adventurers'
# SECRET_KEY variable
app.config["MONGO_URI"] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_heroes')
def get_heroes():
    return render_template("heroes.html", view_header="Heroes",
                           heroes=mongo.db.heroes.find(),
                           adventures=mongo.db.adventures.find())


@app.route('/add_hero')
def add_hero():
    return render_template('add_hero.html',
                           view_header="Create Hero",
                           heroes=mongo.db.heroes.find(),
                           adventures=mongo.db.adventures.find())


@app.route('/insert_hero', methods=['POST'])
def insert_hero():
    heroes = mongo.db.heroes
    heroes.insert_one(request.form.to_dict())
    return redirect(url_for('get_heroes'))


@app.route('/edit_hero/<hero_id>')
def edit_hero(hero_id):
    the_hero = mongo.db.heroes.find_one({"_id": ObjectId(hero_id)})
    all_adventures = mongo.db.adventures.find()
    return render_template('edit_hero.html',
                           view_header="Edit Hero",
                           hero=the_hero,
                           adventures=all_adventures)


@app.route('/update_hero/<hero_id>', methods=["POST"])
def update_hero(hero_id):
    heroes = mongo.db.heroes
    heroes.update({'_id': ObjectId(hero_id)},
                  {
        'hero_name': request.form.get('hero_name'),
        'weapon': request.form.get('weapon'),
        'armor': request.form.get('armor'),
        'race': request.form.get('race'),
        'profession': request.form.get('profession'),
        'mount': request.form.get('mount'),
        'home': request.form.get('home'),
        'possessions': request.form.get('possessions'),
        'adventure_name': request.form.get('adventure_name')
                  })
    return redirect(url_for('get_heroes'))


@app.route('/delete_hero/<hero_id>')
def delete_hero(hero_id):
    mongo.db.heroes.remove({'_id': ObjectId(hero_id)})
    return redirect(url_for('get_heroes'))


@app.route('/get_adventure')
def get_adventure():
    return render_template('adventure.html', view_header="Adventures",
                           adventures=mongo.db.adventures.find())


@app.route('/delete_adventure/<adventure_id>')
def delete_adventure(adventure_id):
    mongo.db.adventures.remove({'_id': ObjectId(adventure_id)})
    return redirect(url_for('get_adventure'))


@app.route('/edit_adventure/<adventure_id>')
def edit_adventure(adventure_id):
    the_adventure = mongo.db.adventures.find_one(
        {"_id": ObjectId(adventure_id)})
    return render_template('edit_adventure.html',
                           view_header="Edit Adventure",
                           adventure=the_adventure)


@app.route('/update_adventure/<adventure_id>', methods=['POST'])
def update_adventure(adventure_id):
    adventures = mongo.db.adventures
    adventures.update({'_id': ObjectId(adventure_id)},
                      {
        'adventure_name': request.form.get('adventure_name'),
        'adventure_topic': request.form.get('adventure_topic')
                      })
    return redirect(url_for('get_adventure'))


@app.route('/insert_adventure', methods=['POST'])
def insert_adventure():
    adventures = mongo.db.adventures
    adventures.insert_one(request.form.to_dict())
    return redirect(url_for('get_adventure'))


@app.route('/add_adventure')
def add_adventure():
    return render_template('add_adventure.html',
                           view_header="Add Adventure",
                           adventures=mongo.db.adventures.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
