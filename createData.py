# Fill the database with necessary data
import sqlite3
from app import app, db
from app.models import Subgroup, Phylum, Videogames
from flask import g
import json


# Check database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('monData.db')
        print("Success")
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def fillSubgroup():
    # Opening JSON file
    f = open('app/json/branch.json')
    # returns JSON object as a dictionary
    branch = json.load(f)
    for subBranch in branch['branch']:
        division = subBranch['division']
        Subgroup.create(division)
    f.close()


def fillPhylums():
    # Opening JSON file
    f = open('app/json/phylums.json')
    # returns JSON object as a dictionary
    phylums = json.load(f)
    for phylum in phylums['phylums']:
        category = phylum['category']
        codename = phylum['codename']
        Phylum.create(category, codename)
    f.close()

def fillVidya():
    # Opening JSON file
    f = open('app/json/games.json')
    # returns JSON object as a dictionary
    games = json.load(f)
    for game in games['games']:
        gamename = game['gamename']
        shortname = game['shortname']
        Videogames.create(gamename, shortname)
    f.close()


with app.app_context():
    db.create_all()
    cur = get_db().cursor()
    print("Subgroup has:\n ", query_db('select * from subgroup'))
    print("Phylum has:\n ", query_db('select * from phylum'))
    print("Videogames has:\n ", query_db('select * from videogames'))


    # If list is empty
    if not query_db('select * from subgroup'):
        fillSubgroup()
    else:
        for user in query_db('select * from subgroup'):
            if user[1] is None:
                fillSubgroup()


    # Phylum table
    if not query_db('select * from phylum'):
        fillPhylums()
    else:
        for user in query_db('select * from phylum'):
            if user[1] is None:
                fillPhylums()

    
    # Videogames table
    if not query_db('select * from videogames'):
        fillVidya()
    else:
        for user in query_db('select * from videogames'):
            if user[1] is None:
                fillVidya()

    print("Finished\n Now Starting addMonster.py...")

import addMonsters
#from app.dummyInfo import addNeopteron