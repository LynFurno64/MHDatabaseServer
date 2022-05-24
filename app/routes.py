from crypt import methods
from flask import abort
from flask import Flask, jsonify
from flask import make_response
from flask import render_template, flash, redirect, url_for, request
from app import app, db
import json
import os
from os import listdir

from app.models import Monster, Phylum, Subgroup
from app.modelSchema import MonsterSchema

a = open('app/json/branch.json')
branch = json.load(a)

b = open('app/json/phylums.json')
phylums = json.load(b)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    monsters = Monster.query.order_by(Monster.name.asc()).paginate(
        page, app.config['MONS_PER_PAGE'], False
    )

    next_url = url_for('monsterList', page= monsters.next_num) \
        if monsters.has_next else None
    prev_url = url_for('monsterList', page= monsters.prev_num) \
        if monsters.has_prev else None

    return render_template('index.html', title='Monster List', monsters=monsters.items, next_url=next_url, prev_url=prev_url)


@app.route('/app/monsterList', methods=['GET', 'POST'])
def get_monsters():
    monsters = Monster.query.all()

    for mon in monsters:
        name = mon.name
        group = mon.phylum.category
        print("Name: ", name, "\nGroup: ", group, "\n Weakpoints: ")

    monster_schema = MonsterSchema(many=True)
    output = monster_schema.dump(monsters)
    print(output)

    return jsonify({'monsters': output})


@app.route('/app/phylums', methods=['GET'])
def get_phylums():
    return phylums

@app.route('/app/phylums/<int:phylum_id>', methods=['GET'])
def get_phylum(phylum_id):
    phylum = [phylum for phylum in phylums['phylums'] if phylum['id'] == phylum_id]
    if len(phylum) == 0:
        abort(404)
    return phylum[0]


@app.route('/app/branch', methods=['GET'])
def get_tree():
    return branch

@app.route('/app/branch/<int:sub_id>', methods=['GET'])
def get_branch(sub_id):
    subBranch = [subBranch for subBranch in branch['branch']
                 if subBranch['id'] == sub_id]
    if len(subBranch) == 0:
        abort(404)
    return subBranch[0]


    ##### Web ####


@app.route('/monsterList')
def monsterList():
    page = request.args.get('page', 1, type=int)
    monsters = Monster.query.order_by(Monster.name.asc()).paginate(
        page, app.config['MONS_PER_PAGE'], False
    )

    mons = Monster.query.all()
    for m in mons:

        picture(m.name, m.variation)

    
    next_url = url_for('monsterList', page= monsters.next_num) \
        if monsters.has_next else None
    prev_url = url_for('monsterList', page= monsters.prev_num) \
        if monsters.has_prev else None

    return render_template('index.html', title='Monster List', monsters=monsters.items, next_url=next_url, prev_url=prev_url)


def picture(name, num):
    # get the path/directory
    folder_dir = "app/static"
    for images in os.listdir(folder_dir):
 
        # check if the image ends with png
        if (images.endswith(".png")):
            fullstring = name
            i = images.replace('.png','')
            substring = i.replace('_',' ')

            if fullstring.casefold().__eq__(substring.casefold()):
                print('name', fullstring, ' and s2(', substring, ') are equal.')

            
