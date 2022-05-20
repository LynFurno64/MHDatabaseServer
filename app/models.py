from app import app, db

related = db.Table(
    'related',
    db.Column('main_id', db.Integer, db.ForeignKey('monster.id')),
    db.Column('subspecies_id', db.Integer, db.ForeignKey('monster.id'))
)


class Subgroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    division = db.Column(db.String(140), index=True, unique=True, nullable=False)

    monster = db.relationship('Monster', backref='division', lazy=True)

    #def __repr__(self):
        #return '<Subgroup {}>'.format(self.type)

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

    monster = db.relationship('Monster', backref='category', lazy=True)

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


class Monster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    generation = db.Column(db.Integer, index=True, nullable=False)
    phylum = db.Column(db.String(100), db.ForeignKey('phylum.codename'), nullable=False)
    variation = db.Column(db.Integer, db.ForeignKey('subgroup.id'), nullable=False)

    weakpoints = db.relationship('Weakpoints', backref='monster', lazy=True)
    weakness = db.relationship('Weakness', backref='monster', lazy=True)
    proficiency = db.relationship('Proficiency', backref='monster', lazy=True)
    item_weak = db.relationship('Item_weak', backref='monster', lazy=True)
    ailments = db.relationship('Ailments', backref='monster', lazy=True)
    games = db.relationship('Games', backref='monster', lazy=True)

    relative = db.relationship(
        'Monster',
        secondary=related,
        primaryjoin=(related.c.main_id == id),
        secondaryjoin=(related.c.subspecies_id == id),
        backref=db.backref('related', lazy='dynamic'),
        lazy='dynamic')


    def __init__(self, name: str, generation: int, phylum: str, variation: int):
        self.name = name
        self.generation = generation
        self.phylum = phylum
        self.variation = variation

    @staticmethod
    def create(name, generation, phylum, variation):  # create Phylum
        new = Monster(name, generation, phylum, variation)
        db.session.add(new)
        db.session.commit()

    def __repr__(self):
        return '<Monster {}>'.format(self.name)

    def is_relative(self, monster):
        return self.relative.filter(
            related.c.subspecies_id == monster.id).count() > 0

    def related(self, monster):
        if not self.is_relative(monster):
            self.relative.append(monster)


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

    @staticmethod    
    def applyItemWeakness(mon_id: int, shock_trap: bool, pitfall_trap: bool, flash_bomb: bool, sonic_bomb: bool):
        new = Item_weak(mon_id, shock_trap, pitfall_trap, flash_bomb, sonic_bomb)
        db.session.add(new)
        db.session.commit()


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
        return '<Weakness {}>'.format(self.fire)

    def __init__(self, mon_id: int, fire: bool, water: bool, thunder: bool, ice: bool, dragon: bool, poison: bool, sleep: bool, para: bool, blast: bool):
        self.mon_id = mon_id
        self.fire = fire
        self.water = water
        self.thunder = thunder
        self.ice = ice
        self.dragon = dragon
        self.poison = poison
        self.sleep = sleep
        self.para = para
        self.blast = blast

    @staticmethod    
    def applyWeakness(mon_id: int, fire: bool, water: bool, thunder: bool, ice: bool, dragon: bool, poison: bool, sleep: bool, para: bool, blast: bool):
        new = Weakness(mon_id,fire, water, thunder, ice, dragon, poison, sleep, para, blast)
        db.session.add(new)
        db.session.commit()


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

    @staticmethod    
    def applyStrenghts(mon_id: int, fire: bool, water: bool, thunder: bool, ice: bool, dragon: bool):
        new = Proficiency(mon_id, fire, water, thunder, ice, dragon)
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



class Ailments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)
    poison = db.Column(db.Boolean)
    sleep = db.Column(db.Boolean)
    para = db.Column(db.Boolean)
    blast = db.Column(db.Boolean)
    stun = db.Column(db.Boolean)
    tremor = db.Column(db.Boolean)
    roar = db.Column(db.Boolean)
    wind = db.Column(db.Boolean)

    def __repr__(self):
        return '<Ailments {}>'.format(self.wind)

    def __init__(self, mon_id: int, poison: bool, sleep: bool, para: bool, blast: bool, stun: bool, tremor: bool, roar: bool, wind: bool):
        self.mon_id = mon_id
        self.poison = poison
        self.sleep = sleep
        self.para = para
        self.blast = blast
        self.stun = stun
        self.tremor = tremor
        self.roar = roar
        self.wind = wind

    @staticmethod    
    def createStatus( mon_id: int, poison: bool, sleep: bool, para: bool, blast: bool, stun: bool, tremor: bool, roar: bool, wind: bool):
        new = Ailments(mon_id, poison, sleep, para, blast, stun, tremor, roar, wind)
        db.session.add(new)
        db.session.commit()



class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)
    MHF = db.Column(db.Boolean)
    MHF2 = db.Column(db.Boolean)
    MH3rd = db.Column(db.Boolean)
    MH3U = db.Column(db.Boolean)
    MH4U = db.Column(db.Boolean)
    MHGU = db.Column(db.Boolean)
    MHWI = db.Column(db.Boolean)
    MHRS = db.Column(db.Boolean)

    def __init__(self, mon_id: int, MHF: bool, MHF2: bool, MH3rd: bool, MH3U: bool, MH4U: bool, MHGU: bool, MHWI: bool, MHRS: bool):
        self.mon_id = mon_id
        self.MHF = MHF
        self.MHF2 = MHF2
        self.MH3rd = MH3rd
        self.MH3U = MH3U
        self.MH4U = MH4U
        self.MHGU = MHGU
        self.MHWI = MHWI
        self.MHRS = MHRS

    @staticmethod    
    def create(mon_id: int, MHF: bool, MHF2: bool, MH3rd: bool, MH3U: bool, MH4U: bool, MHGU: bool, MHWI: bool, MHRS: bool):
        new = Games(mon_id, MHF, MHF2, MH3rd, MH3U, MH4U, MHGU, MHWI, MHRS)
        db.session.add(new)
        db.session.commit()

