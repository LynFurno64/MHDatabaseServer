from array import array
from app import app, db

familia = db.Table(
    'related',
    db.Column('main_id', db.Integer, db.ForeignKey('monster.id')),
    db.Column('subspecies_id', db.Integer, db.ForeignKey('monster.id'))
)


class Subgroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    division = db.Column(db.String(140), index=True, unique=True, nullable=False)

    monster = db.relationship('Monster', backref='subgroup', lazy=True)

    def __init__(self, division: str):
        self.division = division

    @staticmethod
    def create(division):  # create Subgroup
        new_form = Subgroup(division)
        db.session.add(new_form)
        db.session.commit()


class Phylum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(140), unique=True, nullable=False)
    codename = db.Column(db.String(100), index=True, unique=True, nullable=False)

    monster = db.relationship('Monster', backref='phylum', lazy=True)

    #def __repr__(self):
        #return '<Phylum {}>'.format(self.name)

    def __init__(self, category: str, codename: str):
        self.category = category
        self.codename = codename

    @staticmethod
    def create(category, codename):  # create Phylum
        new = Phylum(category, codename)
        db.session.add(new)
        db.session.commit()

class Videogames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gamename = db.Column(db.String(140), unique=True, nullable=False)
    shortname = db.Column(db.String(100), index=True, unique=True, nullable=False)

    egames = db.relationship('Egames', backref='videogames', lazy=True)

    def __init__(self, gamename: str, shortname: str):
        self.gamename = gamename
        self.shortname = shortname

    @staticmethod
    def create(gamename, shortname):  # create Vidoegames
        new = Videogames(gamename, shortname)
        db.session.add(new)
        db.session.commit()



class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    generation = db.Column(db.Integer, index=True, nullable=False)
    group = db.Column(db.String(100), db.ForeignKey('phylum.codename'), nullable=False)
    variation = db.Column(db.Integer, db.ForeignKey('subgroup.id'), nullable=False)

    weakpoints = db.relationship('Weakpoints', backref='monster', lazy=True, uselist=False)
    weakness = db.relationship('Weakness', backref='monster', lazy=True, uselist=False)
    proficiency = db.relationship('Proficiency', backref='monster', lazy=True, uselist=False)
    item_weak = db.relationship('Item_weak', backref='monster', lazy=True, uselist=False)
    ailments = db.relationship('Ailments', backref='monster', lazy=True, uselist=False)
    egames = db.relationship('Egames', backref='monster', lazy=True)


    relative = db.relationship(
        'Monster', secondary=familia,
        primaryjoin=(familia.c.main_id == id),
        secondaryjoin=(familia.c.subspecies_id == id),
        backref=db.backref('familia', lazy='dynamic'), lazy='dynamic')


    def __repr__(self):
            return '<Monster {}>'.format(self.name)

    def __init__(self, name: str, generation: int, group: str, variation: int):
        self.name = name
        self.generation = generation
        self.group = group
        self.variation = variation

    @staticmethod
    def create(self): 
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Monster {}>'.format(self.name)


    def family(self, monster):
        if not self.is_family(monster):
            self.relative.append(monster)
            monster.relative.append(self)

    def is_family(self, monster):
        return self.relative.filter(
            familia.c.subspecies_id == monster.id).count() > 0

# Items Monsters are weak to
class Item_weak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)
    shock_trap = db.Column(db.Boolean)
    pitfall_trap = db.Column(db.Boolean)
    flash_bomb = db.Column(db.Boolean)
    sonic_bomb = db.Column(db.Boolean)

    def __repr__(self):
        return '<Item_weak {}>'.format(self.shock_trap)

    def __init__(self, mon_id: int, shock_trap: bool, pitfall_trap: bool, flash_bomb: bool, sonic_bomb: bool):
        self.mon_id = mon_id
        self.shock_trap = shock_trap
        self.pitfall_trap = pitfall_trap
        self.flash_bomb = flash_bomb
        self.sonic_bomb = sonic_bomb

    # Add item weakness to the database
    @staticmethod    
    def applyItemWeakness(mon_id: int, shock_trap: bool, pitfall_trap: bool, flash_bomb: bool, sonic_bomb: bool):
        new = Item_weak(mon_id, shock_trap, pitfall_trap, flash_bomb, sonic_bomb)
        db.session.add(new)
        db.session.commit()

    # All boss monsters are immuned to items
    @staticmethod    
    def elderBlock(mon_id: int):
        new = Item_weak(mon_id, False, False, False, False)
        db.session.add(new)
        db.session.commit()

# Defines the monster's elemental and status weaknesses
class Weakness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)
    fire = db.Column(db.Boolean)
    water = db.Column(db.Boolean)
    thunder = db.Column(db.Boolean)
    ice = db.Column(db.Boolean)
    dragon = db.Column(db.Boolean)
    poison = db.Column(db.Boolean)
    sleep = db.Column(db.Boolean)
    para = db.Column(db.Boolean)
    blast = db.Column(db.Boolean)

    
    def __repr__(self):
        return '<Weakness {}>'.format(self.mon_id)

    # Add the elemental weaknesses to the database if the monsters have more than 1 weakness
    def applyWeaknessElement(self, mon_id: int, fire: bool, water: bool, thunder: bool, ice: bool, dragon: bool):
        self.mon_id = mon_id
        self.fire = fire
        self.water = water
        self.thunder = thunder
        self.ice = ice
        self.dragon = dragon
        db.session.add(self)
        db.session.commit()

    # Add a elemental weakness to the database if the monsters ONLY HAVE 1 weakness
    def onlyWeakElement(self, mon_id: int, element: str):
        self.mon_id = mon_id
        self.fire = False
        self.water = False
        self.thunder = False
        self.ice = False
        self.dragon = False

        if  element == 'fire':
            self.fire = True
        elif  element == 'water':
            self.water = True
        elif  element == 'thunder':
            self.thunder = True
        elif  element == 'ice':
            self.ice = True
        elif  element == 'dragon':
            self.dragon = True
        
        db.session.add(self)
        db.session.commit()
        
    
    # Add the status weaknesses to the database if the monsters have more than 1 weakness
    def applyWeaknessStatus(self, mon_id: int, poison: bool, sleep: bool, para: bool, blast: bool):
        self.mon_id = mon_id
        self.poison = poison
        self.sleep = sleep
        self.para = para
        self.blast = blast
        db.session.add(self)
        db.session.commit()

    # Add a staus weakness to the database if the monsters ONLY HAVE 1 weakness
    def onlyWeakStatus(self, mon_id: int, status: str):
        self.mon_id = mon_id
        self.poison = False
        self.sleep = False
        self.para = False
        self.blast = False

        if  status == 'poison':
            self.poison = True
        elif  status == 'sleep':
            self.sleep = True
        elif  status == 'para':
            self.para = True
        elif  status == 'blast':
            self.blast = True

        db.session.add(self)
        db.session.commit()

    # Add a no weakness to the database if the monsters doesn't have any weakness
    def noWeaknessStatus(self, mon_id: int):
        self.mon_id = mon_id
        self.poison = False
        self.sleep = False
        self.para = False
        self.blast = False
        db.session.add(self)
        db.session.commit()



# Defines the monster's elemental attacks
class Proficiency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)
    fire = db.Column(db.Boolean)
    water = db.Column(db.Boolean)
    thunder = db.Column(db.Boolean)
    ice = db.Column(db.Boolean)
    dragon = db.Column(db.Boolean)

    def __repr__(self):
        return '<Proficiency {}>'.format(self.water)

    def __init__(self, mon_id: int, fire: bool, water: bool, thunder: bool, ice: bool, dragon: bool):
        self.mon_id = mon_id
        self.fire = fire
        self.water = water
        self.thunder = thunder
        self.ice = ice
        self.dragon = dragon


    # Adds elemental attacks for monsters that have more than on element 
    @staticmethod    
    def applyStrenghts(mon_id: int, fire: bool, water: bool, thunder: bool, ice: bool, dragon: bool):
        new = Proficiency(mon_id, fire, water, thunder, ice, dragon)
        db.session.add(new)
        db.session.commit()


    # Does not Add any elemental attack for monsters that don't have
    @staticmethod    
    def noElement(mon_id: int):
        new = Proficiency(mon_id, False, False, False, False, False)
        db.session.add(new)
        db.session.commit()

    # Adds 1 elemental attack for monsters that only have one 
    def onlyGoodAt(mon_id: int, element: str):
        if  element == 'fire':
            new = Proficiency(mon_id, fire=True, water=False, thunder=False, ice=False, dragon=False)
            
        elif  element == 'water':
            new = Proficiency(mon_id, fire=False, water=True, thunder=False, ice=False, dragon=False)

        elif  element == 'thunder':
            new = Proficiency(mon_id, fire=False, water=False, thunder=True, ice=False, dragon=False)

        elif  element == 'ice':
            new = Proficiency(mon_id, fire=False, water=False, thunder=False, ice=True, dragon=False)

        elif  element == 'dragon':
            new = Proficiency(mon_id, fire=False, water=False, thunder=False, ice=False, dragon=True)

        db.session.add(new)
        db.session.commit()


class Weakpoints(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cut = db.Column(db.String(140))
    impact = db.Column(db.String(140))
    projectile = db.Column(db.String(140))
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)

    def __repr__(self):
        return '<Weakpoints {}>'.format(self.cut)

    def __init__(self, mon_id: int, cut: str, impact: str, projectile: str):
        self.mon_id = mon_id
        self.cut = cut
        self.impact = impact
        self.projectile = projectile

    @staticmethod    
    def createWeakPoints(mon_id: int, cut: str, impact: str, projectile: str):
        new = Weakpoints(mon_id, cut, impact, projectile)
        db.session.add(new)
        db.session.commit()


#Defines the ailments induced by the monster
class Ailments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)
    status = db.Column(db.String(250)) # Status Effects
    blight = db.Column(db.String(140)) # Blight Effects
    # For Tremors, Roars, Wind, Stun
    natural = db.Column(db.String(140))

    def __repr__(self):
        return '<Ailments {}>'.format(self.status)

    def __init__(self, mon_id: int, status: str, blight: str, natural: str):
        self.mon_id = mon_id
        self.status = status
        self.blight = blight
        self.natural = natural

    # Add Ailments
    @staticmethod    
    def createStatus( mon_id: int, status: str, blight: str, natural: str):
        new = Ailments(mon_id, status, blight, natural)
        db.session.add(new)
        db.session.commit()

class Egames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)
    games = db.Column(db.String(100), db.ForeignKey('videogames.shortname'), nullable=False)


    def __repr__(self):
        return '<Egames {}>'.format(self.games)

    # Add Monsters to a game
    def inGame(mid: int,  games: str):
        new = Egames(mon_id= mid, games= games)
        db.session.add(new)
        db.session.commit()

    # Add Monsters to multiple games
    def putInGames(mon_id: int,  games: array):
        for x in games:
            new = Egames(mon_id= mon_id, games= x)
            db.session.add(new)
            db.session.commit()