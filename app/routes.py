from flask import abort
from flask import Flask, jsonify
from flask import render_template, flash, redirect, url_for, request
from app import app, db
import json
from app.forms import MonsterForm

from app.models import Monster, Phylum, Subgroup, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Egames, familia
from app.modelSchema import GamesSchema, MonsterSchema, Item_weakSchema, WeaknessSchema, WeakpointsSchema, ProficiencySchema, AilmentsSchema

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

@app.route('/app/games', methods=['GET', 'POST'])
def get_games():
    games = Egames.query.all()
    games_schema = GamesSchema(many=True)
    output = games_schema.dump(games)
    return jsonify({'gamesList': output})


############################### Single JSON ####################################
@app.route('/app/family/<int:mon_id>', methods=['GET', 'POST'])
def get_family(mon_id):
    monster = Monster.query.filter_by(id= mon_id).first_or_404()
    relative = monster.relative.all()
    monster_schema = MonsterSchema(many=True)
    mon = monster_schema.dump(relative)
    return jsonify({'relatives': mon})

@app.route('/app/games/<int:mon_id>', methods=['GET', 'POST'])
def get_mongames(mon_id):
    monster = Egames.query.filter_by(mon_id= mon_id)
    games_schema = GamesSchema(many=True)
    mon = games_schema.dump(monster)
    return jsonify({'games_in': mon})

@app.route('/app/itemWeakness/<int:mon_id>', methods=['GET', 'POST'])
def get_itemWeak(mon_id):
    monster = Item_weak.query.filter_by(mon_id= mon_id).first_or_404()

    data_schema = Item_weakSchema()
    mon = data_schema.dump(monster)
    return jsonify(mon)

@app.route('/app/weakness/<int:mon_id>', methods=['GET', 'POST'])
def get_weakness(mon_id):
    monster = Weakness.query.filter_by(mon_id= mon_id).first_or_404()

    data_schema = WeaknessSchema()
    mon = data_schema.dump(monster)
    return jsonify(mon)

@app.route('/app/weakpoints/<int:mon_id>', methods=['GET', 'POST'])
def get_weakpoint(mon_id):
    monster = Weakpoints.query.filter_by(mon_id= mon_id).first_or_404()

    data_schema = WeakpointsSchema()
    mon = data_schema.dump(monster)
    return jsonify(mon)

@app.route('/app/strength/<int:mon_id>', methods=['GET', 'POST'])
def get_strength(mon_id):
    monster = Proficiency.query.filter_by(mon_id= mon_id).first_or_404()

    strength_schema = ProficiencySchema()
    mon = strength_schema.dump(monster)
    return jsonify(mon)


@app.route('/app/ailments/<int:mon_id>', methods=['GET', 'POST'])
def get_ailment(mon_id):
    monster = Ailments.query.filter_by(mon_id= mon_id).first_or_404()
    data_schema = AilmentsSchema()
    mon = data_schema.dump(monster)
    return jsonify(mon)

############################### Web ###############################

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
    return render_template('monster.html', title=monster.name, monster=monster)


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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = MonsterForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        monster = Monster(name= form.monstername.data, generation= form.generation.data, group= form.group.data, variation= form.variation.data)
        db.session.add(monster)
        db.session.commit()

        item_weak = Item_weak(mon_id= monster.id, shock_trap= form.item_weakness.shock_trap.data , pitfall_trap= form.item_weakness.pitfall_trap.data, 
                           flash_bomb= form.item_weakness.flash_bomb.data, sonic_bomb= form.item_weakness.sonic_bomb.data)
        
        proficiency = Proficiency(monster.id, form.element.fire.data, form.element.water.data, form.element.thunder.data, form.element.ice.data, form.element.dragon.data)

        weakness = Weakness()
        weakness.applyWeaknessElement(monster.id, form.elemental_weakness.fire.data, form.elemental_weakness.water.data, form.elemental_weakness.thunder.data, form.elemental_weakness.ice.data, form.elemental_weakness.dragon.data)
        weakness.applyWeaknessStatus(monster.id, form.status_weakness.poison.data, form.status_weakness.sleep.data, form.status_weakness.paralysis.data, form.status_weakness.blast.data)

        weakpoint = Weakpoints(mon_id= monster.id, cut= form.weakpoints.cut.data, impact= form.weakpoints.impact.data, projectile= form.weakpoints.projectile.data)
        ailments = Ailments(mon_id= monster.id, status= form.ailment.status.data, blight= form.ailment.blight.data, natural= form.ailment.natural.data)

        db.session.add(item_weak)
        db.session.add(proficiency)
        db.session.add(weakpoint)
        db.session.add(ailments)
        db.session.commit()

        list = []
        if form.games.MHF.data:
            list.append('MHF')
        if form.games.MHFU.data:
            list.append('MHFU')
        if form.games.MH3rd.data:
            list.append('MH3rd')
        if form.games.MH3U.data:
            list.append('MH3U')
        if form.games.MH4U.data:
            list.append('MH4U')
        if form.games.MHGU.data:
            list.append('MHGU')
        if form.games.MHWI.data:
            list.append('MHWI')
        if form.games.MHRS.data:
            list.append('MHRS')

        Egames.putInGames(monster.id,  list)

        flash('Congratulations, you added a new creature!')
        return redirect(url_for('index'))
    flash(form.errors)
    return render_template('register.html', title='Register New Monster', form=form) 

@app.route('/related/<monstername>', methods=['GET', 'POST'])
def related(monstername):
    print(monstername)
    monster = Monster.query.filter_by(name= monstername).first_or_404()
    monsterinGroup = Monster.query.filter_by(group= monster.phylum.codename).all()

    # Filter out family members
    list = [] 
    for monFromGroup in monsterinGroup:
        print(monster, "vs", monFromGroup, ": ", monster.is_family(monFromGroup))
        if not monster.is_family(monFromGroup):
            if monster != monFromGroup:
                list.append(monFromGroup)
    return render_template('related.html', title='Add Relatives', monster= monster, monlist= list)

@app.route('/related/<mainname>/follow/<subname>')
def follow(mainname, subname):
    monsterMain = Monster.query.filter_by(name= mainname).first()
    monsterSub = Monster.query.filter_by(name= subname).first()

    if monsterSub is None:
        flash('{} not found.'.format(subname))
        return redirect(url_for('index'))
    if monsterSub == monsterMain:
        flash('Cannot follow same species!')
        return redirect(url_for('monster', monstername= mainname))
 
    monsterMain.family(monsterSub)
    db.session.commit()
    flash('{} and {} are now related!'.format(mainname, subname))
    return redirect(url_for('monster', monstername= mainname))

