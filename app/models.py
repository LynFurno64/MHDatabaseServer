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

    relative = db.relationship(
        'Monster',
        secondary=related,
        primaryjoin=(related.c.main_id == id),
        secondaryjoin=(related.c.subspecies_id == id),
        backref=db.backref('related', lazy='dynamic'),
        lazy='dynamic')

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
        return '<Item_weak {}>'.format(self.mon_id)


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


class Proficiency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)
    fire = db.Column(db.Boolean)
    water = db.Column(db.Boolean)
    thunder = db.Column(db.Boolean)
    ice = db.Column(db.Boolean)
    dragon = db.Column(db.Boolean)

    def __repr__(self):
        return '<Proficiency {}>'.format(self.mon_id)


class Weakpoints(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cut = db.Column(db.String(140))
    impact = db.Column(db.String(140))
    projectile = db.Column(db.String(140))
    mon_id = db.Column(db.Integer, db.ForeignKey('monster.id'), nullable=False)

    def __repr__(self):
        return '<Weakpoints {}>'.format(self.cut)


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
        return '<Ailments {}>'.format(self.mon_id)
