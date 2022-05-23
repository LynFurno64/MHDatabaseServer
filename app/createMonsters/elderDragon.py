# Create Monsters from the Elder Dragon group
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games

################## Lunastra ##################
addWeakness = Weakness()
games = Games()

################## Teostra ##################
addWeakness = Weakness()
games = Games()


################## Amatsu ##################
addWeakness = Weakness()
games = Games()


################## Ceadeus ##################
addWeakness = Weakness()
games = Games()

################## Goldbeard Ceadeus ##################
addWeakness = Weakness()
games = Games()

################## Valstrax ##################
addWeakness = Weakness()
games = Games()


################# Crimson Glow Valstrax ##################
addWeakness = Weakness()
games = Games()


################# Nergigante ##################
addWeakness = Weakness()
games = Games()

################# Ruiner Nergigante ##################
addWeakness = Weakness()
games = Games()

################## ibushi ##################
addWeakness = Weakness()
games = Games()

ibushi = Monster(name='Ibushi', generation=5, group='elder', variation=1)
ibushi.create(ibushi)

Item_weak.elderBlock(mon_id= ibushi.id)
addWeakness.applyWeaknessElement(mon_id= ibushi.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.noWeaknessStatus(mon_id= ibushi.id)
Weakpoints.createWeakPoints(mon_id= ibushi.id, cut='Head, Chest, Wingarm, Back, Tail Tip', impact='Head, Chest, Wingarm, Back, Tail Tip', projectile='Head, Chest, Wingarm, Back, Tail Tip')

Proficiency.onlyGoodAt(mon_id= ibushi.id, element='dragon')
Ailments.createStatus(mon_id= ibushi.id, status="", blight="Dragon blight", natural="Wind pressure (Large), Roar (Large)")

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

Proficiency.onlyGoodAt(mon_id= narwa.id, element='thunder')
Ailments.createStatus(mon_id= narwa.id, status="", blight="Thunder blight", natural="Roar (Large)")

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

Proficiency.onlyGoodAt(mon_id= narwa_allmother.id, element='thunder')
Ailments.createStatus(mon_id= narwa_allmother.id, status="", blight="Thunder blight", natural="Wind pressure (Large), Roar (Large)")

games.inMHGen5(mon_id= narwa_allmother.id, MHWI=False, MHRS=True)

narwa.family(ibushi)
narwa.family(narwa_allmother)