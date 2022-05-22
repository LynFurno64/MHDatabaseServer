# Create Monsters from the Flying Wyvern Phylum
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games

#################  Rathalos ##################
addWeakness = Weakness()
games = Games() 

rathalos = Monster("Rathalos", 1, "flying", 1)
rathalos.create(rathalos)

Item_weak.applyItemWeakness(rathalos.id, True, True, True, False)
addWeakness.applyWeaknessElement(mon_id= rathalos.id, fire=False, water=False, thunder=True, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= rathalos.id, poison=False, sleep=True, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id=rathalos.id, cut='Head, Tail', impact='Head, Belly', projectile='Head, Legs')

Proficiency.applyStrenghts(mon_id=rathalos.id, fire=True, water=False, thunder=False, ice=False, dragon=False)
Ailments.createStatus(mon_id=rathalos.id, poison=True, sleep=False, para=False, blast=False, stun=True, tremor=False, roar=True, wind=True)
Games.addToAll(mon_id=rathalos.id)



#################  Azure Rathalos ##################
addWeakness = Weakness()
games = Games() 
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


#################  Silver Rathalos ##################
addWeakness = Weakness()
games = Games() 

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



#################  Dreadking Rathalos ##################
addWeakness = Weakness()
games = Games() 

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


#################  Tigrex ##################
addWeakness = Weakness()
games = Games() 
 
##################  Molten Tigrex ##################
addWeakness = Weakness()
games = Games()