# Create Monsters from the Flying Wyvern group
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

Proficiency.onlyGoodAt(mon_id=rathalos.id, element='fire')
Ailments.createStatus(mon_id= rathalos.id, status="Poison", blight="Fireblight", natural="Wind Pressure, Roar")

#games.addToAll(mon_id=rathalos.id)
games.inMHOld(rathalos.id, True, True)
games.inMHGen3(rathalos.id, True, True)
games.inMHGen4(rathalos.id, True, True)
games.inMHGen5(rathalos.id, True, True)

#################  Azure Rathalos ##################
addWeakness = Weakness()
games = Games() 
rathalos_azure = Monster("Azure Rathalos", 1, "flying", 2)
rathalos_azure.create(rathalos_azure)

Item_weak.applyItemWeakness(mon_id=rathalos_azure.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= rathalos_azure.id, fire=False, water=False, thunder=True, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= rathalos_azure.id, poison=False, sleep=True, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id=rathalos_azure.id, cut='Head, Tail', impact='Head, Belly', projectile='Head, Legs')

Proficiency.onlyGoodAt(mon_id=rathalos_azure.id, element='fire')
Ailments.createStatus(mon_id= rathalos_azure.id, status="Poison", blight="Fireblight", natural="Wind Pressure(L), Roar(L)")
games.inMHOld(rathalos_azure.id, True, True)
games.inMHGen3(rathalos_azure.id, False, True)
games.inMHGen4(rathalos_azure.id, True, True)
games.inMHGen5(rathalos_azure.id, True, False)

rathalos.family(rathalos_azure)
rathalos_azure.family(rathalos)

#################  Silver Rathalos ##################
addWeakness = Weakness()
games = Games() 

rathalos_silver = Monster("Silver Rathalos", 1, "flying", 3)
rathalos_silver.create(rathalos_silver)

Item_weak.applyItemWeakness(mon_id=rathalos_silver.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= rathalos_silver.id, fire=False, water=True, thunder=True, ice=False, dragon=False)
addWeakness.applyWeaknessStatus(mon_id= rathalos_silver.id, poison=False, sleep=True, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id=rathalos_silver.id, cut='Head (Broken), Wings, Tail Tip', impact='Head (Broken), Wings, Tail Tip', 
projectile='Head (Broken), Tail Tip')

Proficiency.onlyGoodAt(mon_id=rathalos_silver.id, element='fire')
Ailments.createStatus(mon_id= rathalos_silver.id, status="Poison", blight="Fireblight", natural="Wind Pressure(L), Roar(L), Stun")
games.inMHOld(rathalos_silver.id, True, True)
games.inMHGen3(rathalos_silver.id, True, True)
games.inMHGen4(rathalos_silver.id, True, True)
games.inMHGen5(rathalos_silver.id, True, True)

rathalos.family(rathalos_silver)
rathalos_silver.family(rathalos)

rathalos_azure.family(rathalos_silver)
rathalos_silver.family(rathalos_azure)


#################  Dreadking Rathalos ##################
addWeakness = Weakness()
games = Games() 

rathalos_dreadking = Monster("Dreadking Rathalos", 4, "flying", 5)
rathalos_dreadking.create(rathalos_dreadking)

Item_weak.applyItemWeakness(mon_id=rathalos_dreadking.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= rathalos_dreadking.id, fire=False, water=False, thunder=True, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= rathalos_dreadking.id, poison=False, sleep=True, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id=rathalos_dreadking.id, cut='Head', impact='Head(Break)', projectile='')

Proficiency.onlyGoodAt(mon_id=rathalos_dreadking.id, element='fire')
Ailments.createStatus(mon_id= rathalos_dreadking.id, status="Noxiuos Poison", blight="Fireblight", natural="Wind Pressure(L), Roar(L)")
games.inMHGen4(rathalos_dreadking.id, False, True)

rathalos.family(rathalos_dreadking)
rathalos_dreadking.family(rathalos)

rathalos_azure.family(rathalos_dreadking)
rathalos_dreadking.family(rathalos_azure)

rathalos_silver.family(rathalos_dreadking)
rathalos_dreadking.family(rathalos_silver)


#################  Tigrex ##################
addWeakness = Weakness()
games = Games() 
 
##################  Molten Tigrex ##################
addWeakness = Weakness()
games = Games()