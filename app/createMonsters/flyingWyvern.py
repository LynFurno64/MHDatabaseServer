# Create Monsters from the Flying Wyvern Phylum

from app import app, db
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games

addWeakness = Weakness()
games = Games()

################## Seltas ##################


rathalos = Monster("Rathalos", 1, "flying", 1)
rathalos.create(rathalos)

Item_weak.applyItemWeakness(rathalos.id, True, True, True, False)
addWeakness.applyWeaknessElement(mon_id= rathalos.id, fire=False, water=False, thunder=True, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= rathalos.id, poison=False, sleep=True, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id=rathalos.id, cut='Head, Tail', impact='Head, Belly', projectile='Head, Legs')

Proficiency.applyStrenghts(mon_id=rathalos.id, fire=True, water=False, thunder=False, ice=False, dragon=False)
Ailments.createStatus(mon_id=rathalos.id, poison=True, sleep=False, para=False, blast=False, stun=True, tremor=False, roar=True, wind=True)
Games.addToAll(mon_id=rathalos.id)

rathian = Monster("Rathian", 1, "flying", 1)
rathian.create(rathian)
Item_weak.applyItemWeakness(rathian.id, True, True, True, False)
#Weakness.applyWeakness(mon_id= rathian.id, fire=False, water=False, thunder=True, ice=False, dragon=True, poison=False, sleep=True, para=False, blast=False)

addWeakness.applyWeaknessElement(mon_id= rathian.id, fire=False, water=False, thunder=False, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= rathian.id, poison=False, sleep=True, para=False, blast=False)

Weakpoints.createWeakPoints(mon_id= rathian.id, cut='Head, Belly', impact='Head, Belly', projectile='Head, Belly, Legs')
Proficiency.applyStrenghts(mon_id= rathian.id, fire=True, water=False, thunder=False, ice=False, dragon=False)
Ailments.createStatus(mon_id= rathian.id, poison=True, sleep=False, para=False, blast=False, stun=True, tremor=False, roar=True, wind=True)
Games.addToAll(mon_id=rathian.id)

rathalos.family(rathian)


rathalos_azure = Monster("Azure Rathalos", 1, "flying", 2)

rathalos_azure.create()
Item_weak.applyItemWeakness(mon_id=.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
Weakness.applyWeakness(mon_id=.id, fire=, water=, thunder=, ice=, dragon=, poison=, sleep=, para=, blast=)

Weakness.applyWeaknessElement(mon_id= .id, fire=, water=False, thunder=True, ice=False, dragon=True)
Weakness.applyWeaknessStatus(mon_id= .id, poison=, sleep=True, para=False, blast=False)

Weakpoints.createWeakPoints(mon_id=.id, cut='Head, Tail', impact='Head, Belly', projectile='Head, Legs')
Proficiency.applyStrenghts(mon_id=.id, fire=, water=, thunder=, ice=, dragon=)
Ailments.createStatus(mon_id=.id, poison=, sleep=, para=, blast=, stun=, tremor=, roar=, wind=)
Games.addToGame(mon_id=.id, MHF=True, MHF2=True, MH3rd=True, MH3U=True, MH4U=True, MHGU=True, MHWI=True, MHRS=True)

rathian_pink = Monster("Pink Rathian", 1, "flying", 2)
.create()
Item_weak.applyItemWeakness(mon_id=.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
Weakness.applyWeakness(mon_id=.id, fire=, water=, thunder=, ice=, dragon=, poison=, sleep=, para=, blast=)

Weakness.applyWeaknessElement(mon_id= .id, fire=, water=False, thunder=True, ice=False, dragon=True)
Weakness.applyWeaknessStatus(mon_id= .id, poison=, sleep=True, para=False, blast=False)

Weakpoints.createWeakPoints(mon_id=.id, cut='Head, Tail', impact='Head, Belly', projectile='Head, Legs')
Proficiency.applyStrenghts(mon_id=.id, fire=, water=, thunder=, ice=, dragon=)
Ailments.createStatus(mon_id=.id, poison=, sleep=, para=, blast=, stun=, tremor=, roar=, wind=)
Games.addToGame(mon_id=.id, MHF=True, MHF2=True, MH3rd=True, MH3U=True, MH4U=True, MHGU=True, MHWI=True, MHRS=True)

rathalos.family(rathalos_azure)
rathian.family(rathian_pink)


rathalos_silver = Monster("Silver Rathalos", 1, "flying", 3)
.create()
Item_weak.applyItemWeakness(mon_id=.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
Weakness.applyWeakness(mon_id=.id, fire=, water=, thunder=, ice=, dragon=, poison=, sleep=, para=, blast=)

Weakness.applyWeaknessElement(mon_id= .id, fire=, water=False, thunder=True, ice=False, dragon=True)
Weakness.applyWeaknessStatus(mon_id= .id, poison=, sleep=True, para=False, blast=False)

Weakpoints.createWeakPoints(mon_id=.id, cut='Head, Tail', impact='Head, Belly', projectile='Head, Legs')
Proficiency.applyStrenghts(mon_id=.id, fire=, water=, thunder=, ice=, dragon=)
Ailments.createStatus(mon_id=.id, poison=, sleep=, para=, blast=, stun=, tremor=, roar=, wind=)
Games.addToGame(mon_id=.id, MHF=True, MHF2=True, MH3rd=True, MH3U=True, MH4U=True, MHGU=True, MHWI=True, MHRS=True)

rathian_gold = Monster("Gold Rathian", 1, "flying", 3)
.create()
Item_weak.applyItemWeakness(mon_id=.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
Weakness.applyWeakness(mon_id=.id, fire=, water=, thunder=, ice=, dragon=, poison=, sleep=, para=, blast=)

Weakness.applyWeaknessElement(mon_id= .id, fire=, water=False, thunder=True, ice=False, dragon=True)
Weakness.applyWeaknessStatus(mon_id= .id, poison=, sleep=True, para=False, blast=False)

Weakpoints.createWeakPoints(mon_id=.id, cut='Head, Tail', impact='Head, Belly', projectile='Head, Legs')
Proficiency.applyStrenghts(mon_id=.id, fire=, water=, thunder=, ice=, dragon=)
Ailments.createStatus(mon_id=.id, poison=, sleep=, para=, blast=, stun=, tremor=, roar=, wind=)
Games.addToGame(mon_id=.id, MHF=True, MHF2=True, MH3rd=True, MH3U=True, MH4U=True, MHGU=True, MHWI=True, MHRS=True)

rathalos.family(rathalos_silver)
rathian.family(rathian_gold)


rathalos_dreadking = Monster("Dreadking Rathalos", 4, "flying", 5)
.create()
Item_weak.applyItemWeakness(mon_id=.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
Weakness.applyWeakness(mon_id=.id, fire=, water=, thunder=, ice=, dragon=, poison=, sleep=, para=, blast=)

Weakness.applyWeaknessElement(mon_id= .id, fire=, water=False, thunder=True, ice=False, dragon=True)
Weakness.applyWeaknessStatus(mon_id= .id, poison=, sleep=True, para=False, blast=False)

Weakpoints.createWeakPoints(mon_id=.id, cut='Head, Tail', impact='Head, Belly', projectile='Head, Legs')
Proficiency.applyStrenghts(mon_id=.id, fire=, water=, thunder=, ice=, dragon=)
Ailments.createStatus(mon_id=.id, poison=, sleep=, para=, blast=, stun=, tremor=, roar=, wind=)
Games.addToGame(mon_id=.id, MHF=True, MHF2=True, MH3rd=True, MH3U=True, MH4U=True, MHGU=True, MHWI=True, MHRS=True)

rathian_dreadqueen = Monster("Dreadqueen Rathian", 4, "flying", 5)
.create()
Item_weak.applyItemWeakness(mon_id=.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
Weakness.applyWeakness(mon_id=.id, fire=, water=, thunder=, ice=, dragon=, poison=, sleep=, para=, blast=)

Weakness.applyWeaknessElement(mon_id= .id, fire=, water=False, thunder=True, ice=False, dragon=True)
Weakness.applyWeaknessStatus(mon_id= .id, poison=, sleep=True, para=False, blast=False)

Weakpoints.createWeakPoints(mon_id=.id, cut='Head, Tail', impact='Head, Belly', projectile='Head, Legs')
Proficiency.applyStrenghts(mon_id=.id, fire=, water=, thunder=, ice=, dragon=)
Ailments.createStatus(mon_id=.id, poison=, sleep=, para=, blast=, stun=, tremor=, roar=, wind=)
Games.addToGame(mon_id=.id, MHF=True, MHF2=True, MH3rd=True, MH3U=True, MH4U=True, MHGU=True, MHWI=True, MHRS=True)

rathalos.family(rathalos_dreadking)
rathian.family(rathian_dreadqueen)