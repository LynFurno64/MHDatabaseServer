from app import ma
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments

# SQLALchemy to JSON serializer

class MonsterSchema(ma.SQLAlchemyAutoSchema):
    class Meta: 
        model = Monster
        include_fk = True
        load_instance = True


class Item_weakSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Item_weak
        include_fk = True
        load_instance = True
        

class WeaknessSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Weakness
        include_fk = True
        load_instance = True

class WeakpointsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Weakpoints
        include_fk = True
        load_instance = True

class ProficiencySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Proficiency
        include_fk = True
        load_instance = True

class AilmentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ailments
        include_fk = True
        load_instance = True