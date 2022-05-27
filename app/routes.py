from flask import abort
from flask import Flask, jsonify
from flask import render_template, flash, redirect, url_for, request
from app import app, db
import json
from os import listdir
from app.forms import SearchForm

from app.models import Monster, Phylum, Subgroup, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games
from app.modelSchema import MonsterSchema, Item_weakSchema, WeaknessSchema, WeakpointsSchema, ProficiencySchema, AilmentsSchema, GamesSchema

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
    monster_schema = MonsterSchema(many=True)
    output = monster_schema.dump(monsters)
    return jsonify({'monsters': output})

@app.route('/app/monsterList/<int:mon_id>', methods=['GET', 'POST'])
def get_monster(mon_id):
    monster = Monster.query.filter_by(id= mon_id).first_or_404()

    monster_schema = MonsterSchema()
    mon = monster_schema.dump(monster)
    print(mon)
    print(monster)


    return jsonify(mon)

@app.route('/app/phylums', methods=['GET'])
def get_phylums():
    return phylums

@app.route('/app/phylums/<int:phylum_id>', methods=['GET'])
def get_phylum(phylum_id):
    phylum = [phylum for phylum in phylums['phylums'] if phylum['id'] == phylum_id]
    if len(phylum) == 0:
        abort(404)
    return phylum[0]


@app.route('/app/subgroup', methods=['GET'])
def get_tree():
    return branch

@app.route('/app/subgroup/<int:sub_id>', methods=['GET'])
def get_branch(sub_id):
    subBranch = [subBranch for subBranch in branch['branch']
                 if subBranch['id'] == sub_id]
    if len(subBranch) == 0:
        abort(404)
    return subBranch[0]

########################### Getters ######################################

@app.route('/app/itemWeakness', methods=['GET', 'POST'])
def get_itemWeak():
    item_weak = Item_weak.query.all()
    item_weak_schema = Item_weakSchema(many=True)
    output = item_weak_schema.dump(item_weak)
    return jsonify({'item_weak': output})


@app.route('/app/weakness', methods=['GET', 'POST'])
def get_weakness():
    weakness = Weakness.query.all()
    item_weak_schema = WeaknessSchema(many=True)
    output = item_weak_schema.dump(weakness)
    return jsonify({'weakness': output})


@app.route('/app/weakpoints', methods=['GET', 'POST'])
def get_weakpoints():
    weakpoints = Weakpoints.query.all()
    weakpoints_schema = WeakpointsSchema(many=True)
    output = weakpoints_schema.dump(weakpoints)
    return jsonify({'weakpoints': output})

@app.route('/app/strength', methods=['GET', 'POST'])
def get_strength():
    strength = Proficiency.query.all()
    strength_schema = ProficiencySchema(many=True)
    output = strength_schema.dump(strength)
    return jsonify({'strength': output})

@app.route('/app/ailments', methods=['GET', 'POST'])
def get_ailments():
    ailments = Ailments.query.all()
    ailments_schema = AilmentsSchema(many=True)
    output = ailments_schema.dump(ailments)
    return jsonify({'ailments': output})

@app.route('/app/games', methods=['GET', 'POST'])
def get_games():
    games = Games.query.all()
    games_schema = GamesSchema(many=True)
    output = games_schema.dump(games)
    return jsonify({'games': output})


    ##### Web ####

@app.route('/search', methods=['GET'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        find = form.searched.data
        Monster.query.filter_by(name= find)
    return render_template('search.html', form=form, find=find)


@app.route('/monsterList')
def monsterList():
    page = request.args.get('page', 1, type=int)
    monsters = Monster.query.order_by(Monster.id).paginate(
        page, app.config['MONS_PER_PAGE'], False
    )
    next_url = url_for('monsterList', page= monsters.next_num) \
        if monsters.has_next else None
    prev_url = url_for('monsterList', page= monsters.prev_num) \
        if monsters.has_prev else None
    return render_template('index.html', title='Monster List', monsters=monsters.items, next_url=next_url, prev_url=prev_url)
    


@app.route('/monster/<monstername>')
def monster(monstername):
    monster = Monster.query.filter_by(name= monstername).first_or_404()
    print(monster.name)
    print(monster.weakness)

    return render_template('monster.html', title=monster.name, monster=monster)

@app.route('/grouping')
def grouping():
    phylums = Phylum.query.all()
    subgroups = Subgroup.query.all()
    return render_template('grouping.html', title='Home')

@app.route('/monster_class')
def monster_class():
    phylum = Phylum.query.all()
    for x in phylum:
        y = x.category.replace(' ', '_')
        print(y)
    return render_template('monster_class.html', title= "Monster Classes", phylum=phylum)


@app.route('/monster_species')
def monster_species():
    subgroup = Subgroup.query.all()

    page = request.args.get('page', 1, type=int)
    subgroup = Subgroup.query.order_by(Subgroup.id).paginate(
        page, app.config['MONS_PER_PAGE'], False
    )
    next_url = url_for('monster_species', page= subgroup.next_num) \
        if subgroup.has_next else None
    prev_url = url_for('monster_species', page= subgroup.prev_num) \
        if subgroup.has_prev else None
    return render_template('monster_species.html', title= "Monster Species", subgroup=subgroup.items, next_url=next_url, prev_url=prev_url)    
