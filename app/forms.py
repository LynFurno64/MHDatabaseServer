from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, TextAreaField, SelectMultipleField, RadioField, FormField
from wtforms.validators import ValidationError, DataRequired

from app.models import Monster


class SearchForm(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ElementForm(FlaskForm):
    fire = BooleanField('Fire')
    water= BooleanField('Water')
    thunder= BooleanField('Thunder')
    ice = BooleanField('Ice')
    dragon = BooleanField('Dragon')

class StatusForm(FlaskForm):
    poison = BooleanField('Poison')
    sleep = BooleanField('Sleep')
    blast = BooleanField('blast')
    paralysis = BooleanField('Paralysis')

class WeakpointForm(FlaskForm):
    cut = StringField('Cut Weakpoint', validators=[DataRequired()])
    impact = StringField('Impact Weakpoint', validators=[DataRequired()])
    projectile = StringField('Projectile Weakpoint', validators=[DataRequired()])

class AilmentForm(FlaskForm):
    status = StringField('Status Ailment')
    blight = StringField('Blight Ailment')
    natural = StringField('Natural Ailment')

class ItemWeakForm(FlaskForm):
    shock_trap = BooleanField('Shock Trap')
    pitfall_trap= BooleanField('Pitfall Trap')
    flash_bomb= BooleanField('Flash Bombs')
    sonic_bomb= BooleanField('Sonic Bombs')


class MonsterForm(FlaskForm):
    monstername = StringField('Name', validators=[DataRequired()])
    generation = IntegerField('Generation Debut', validators=[DataRequired()])
    group = SelectField('Group', choices=[('bug', 'Neopteron'), ('spider', 'Temnoceran'), ('bird', 'Bird Wyvern'), ('flying', 'Flying Wyvern'), 
                                                ('fish', 'Piscine Wyvern'), ('crab', 'Carapaceon'), ('frog', 'Amphibian'), ('beast', 'Fanged Beast'), 
                                                ('water', 'Leviathan'), ('snake', 'Snake Wyvern'), ('brute', 'Brute Wyvern'), ('fanged', 'Fanged Wyvern'), 
                                                ('elder', 'Elder Dragon'), ('???', 'Unknown')], 
                                                validators=[DataRequired()])
    variation = SelectField('Species', choices=[('1', 'Normal'), ('2', 'Subspecies'), ('3', 'Rare Species'), ('4', 'Variant'), 
                                                ('5', 'Deviant')], validators=[DataRequired()])

    item_weakness = FormField(ItemWeakForm)
    element = FormField(ElementForm)
    ailment = FormField(AilmentForm)
    elemental_weakness = FormField(ElementForm) 
    status_weakness = FormField(StatusForm)
    weakpoints = FormField(WeakpointForm)
    submit = SubmitField('Add Creature')
        #age_range = IntegerRangeField(default='(0,100)', blank=True, validators=[RangeMinValueValidator(1), RangeMaxValueValidator(100)])

class LanguageForm(FlaskForm):
    language = SelectMultipleField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    status = StringField('Status Ailment', validators=[DataRequired()])
    dynamic_select = SelectField("Choose an option", choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')], validate_choice=False)

    radio = RadioField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    item_weakness = FormField(ItemWeakForm)

    help = SubmitField('Add')
