# Create Monsters from the Piscine Wyvern group
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Egames


##################  Lavasioth ##################
addWeakness = Weakness()

##################  Plesioth ##################
addWeakness = Weakness()

##################  Green Plesioth ##################
addWeakness = Weakness()

##################  Jyuratodus ##################
addWeakness = Weakness()
Jyuratodus= Monster(name='Jyuratodus', generation=5, group='fish', variation=1)
Jyuratodus.create(Jyuratodus)

Item_weak.applyItemWeakness(mon_id= Jyuratodus.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id= Jyuratodus.id, fire=False, water=True, thunder=True, ice=False, dragon=False)
addWeakness.noWeaknessStatus(Jyuratodus.id)
Weakpoints.createWeakPoints(mon_id= Jyuratodus.id, cut='Head (Mud), Tail, Tail (Mud)', impact='Head (Mud), Tail, Tail (Mud)', projectile='Head (Mud), Tail')

Proficiency.onlyGoodAt(mon_id= Jyuratodus.id, element= "water")
Ailments.createStatus(mon_id= Jyuratodus.id, status="", blight="Waterblight", natural="Mud")
Egames.putInGames(Jyuratodus.id, ['MHWI', 'MHRS'])

##################  Beotodus ##################
addWeakness = Weakness()
Beotodus= Monster(name='Beotodus', generation=5, group='fish', variation=1)
Beotodus.create(Beotodus)

Item_weak.applyItemWeakness(mon_id= Beotodus.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id= Beotodus.id, fire=True, water=False, thunder=True, ice=False, dragon=False)
addWeakness.onlyWeakStatus(mon_id= Beotodus.id, status="blast")
Weakpoints.createWeakPoints(mon_id= Beotodus.id, cut='Legs', impact='Legs', projectile='Legs')

Proficiency.onlyGoodAt(mon_id= Beotodus.id, element= "ice")
Ailments.createStatus(mon_id= Beotodus.id, status="", blight="Iceblight", natural="")
Egames.inGame(Beotodus.id, "MHWI")

Jyuratodus.family(Beotodus)