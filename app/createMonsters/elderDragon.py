# Create Monsters from the Elder Dragon Phylum

from pickle import TRUE
from re import T
from app import app, db
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games



################## ibushi ##################
addWeakness = Weakness()
games = Games()

ibushi = Monster(name='Ibushi', generation=5, phylum='elder', variation=1)
ibushi.create(ibushi)

Item_weak.elderBlock(mon_id= ibushi.id)
addWeakness.applyWeaknessElement(mon_id= ibushi.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.noWeaknessStatus(mon_id= ibushi.id)
Weakpoints.createWeakPoints(mon_id= ibushi.id, cut='Head, Chest, Wingarm, Back, Tail Tip', impact='Head, Chest, Wingarm, Back, Tail Tip', projectile='Head, Chest, Wingarm, Back, Tail Tip')

Proficiency.applyStrenghts(mon_id= ibushi.id, fire=False, water=False, thunder=False, ice=False, dragon=True)
Ailments.createStatus(mon_id= ibushi.id, poison=False, sleep=False, para=False, blast=False, stun=False, tremor=False, roar=True, wind=True)
games.inMHGen5(mon_id= ibushi.id, MHWI=False, MHRS=True)

################## Narwa ##################
addWeakness = Weakness()
games = Games()

narwa = Monster("Narwa", 5, "elder", 1)
narwa.create(narwa)

Item_weak.elderBlock(mon_id= narwa.id)
addWeakness.applyWeaknessElement(mon_id= narwa.id, fire=False, water=False, thunder=False, ice=True, dragon=True)
addWeakness.noWeaknessStatus(mon_id= narwa.id)
Weakpoints.createWeakPoints(mon_id= narwa.id, cut='Head, Chest(Charged), Wingarm(Charged), Abdomen, Back, Tail Tip(Charged)', 
impact='Head, Chest(Charged), Wingarm(Charged), Abdomen, Back, Tail Tip(Charged)', projectile='Head, Chest(Charged), Wingarm(Charged), Abdomen')

Proficiency.applyStrenghts(mon_id= narwa.id, fire=False, water=False, thunder=True, ice=False, dragon=False)
Ailments.createStatus(mon_id= narwa.id, poison=False, sleep=False, para=False, blast=False, stun=False, tremor=False, roar=True, wind=False)
games.inMHGen5(mon_id= narwa.id, MHWI=False, MHRS=True)

################## Narwa Allmother ##################
addWeakness = Weakness()
games = Games()

narwa_allmother = Monster("Narwa Allmother", 5, "elder", 4)
narwa_allmother.create(narwa_allmother)

Item_weak.elderBlock(mon_id= narwa_allmother.id)
addWeakness.applyWeaknessElement(mon_id= narwa_allmother.id, fire=False, water=False, thunder=False, ice=True, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= narwa_allmother.id, poison=False, sleep=False, para=False, blast=True)
Weakpoints.createWeakPoints(mon_id= narwa_allmother.id, cut='Head, Chest(Charged), Wingarm(Charged), Abdomen, Back, Tail Tip(Charged)', 
impact='Head, Chest(Charged), Wingarm(Charged), Abdomen, Back, Tail Tip(Charged)', projectile='Head, Wingarm(Charged), Abdomen, Tail Tip(Charged)')

Proficiency.applyStrenghts(mon_id= narwa_allmother.id, fire=False, water=False, thunder=True, ice=False, dragon=False)
Ailments.createStatus(mon_id= narwa_allmother.id, poison=False, sleep=False, para=False, blast=False, stun=False, tremor=False, roar=True, wind=True)
games.inMHGen5(mon_id= narwa_allmother.id, MHWI=False, MHRS=True)

narwa.family(ibushi)
narwa.family(narwa_allmother)