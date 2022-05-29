# Create Monsters from the Brute Wyvern group
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Egames

################## Brachydios ##################
addWeakness = Weakness()

Brachydios = Monster(name='Brachydios', generation=3, group='brute', variation=1)
Brachydios.create(Brachydios)

Item_weak.applyItemWeakness(mon_id= Brachydios.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.onlyWeakElement(mon_id= Brachydios.id, element='water')
addWeakness.onlyWeakStatus(mon_id= Brachydios.id, status='poison')
Weakpoints.createWeakPoints(mon_id= Brachydios.id, cut='Head, Front Legs', impact='Head, Front Legs', projectile='Head, Tail')

Proficiency.noElement(Brachydios.id)
Ailments.createStatus(mon_id= Brachydios.id, status="", blight="Blast Blight", natural="Tremors, Large Roars")

Egames.putInGames(Brachydios.id,  ['MH3U', 'MH4U', 'MHGU', 'MHWI'])


################## Raging Brachydios ##################
addWeakness = Weakness()

Brachydios_Raging = Monster(name='Raging Brachydios', generation=4, group='brute', variation=4)
Brachydios_Raging.create(Brachydios_Raging)

Item_weak.applyItemWeakness(mon_id= Brachydios_Raging.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= Brachydios_Raging.id, fire=False, water=True, thunder=False, ice=True, dragon=False)
addWeakness.onlyWeakStatus(mon_id= Brachydios_Raging.id, status='poison')
Weakpoints.createWeakPoints(mon_id= Brachydios_Raging.id, cut='Head, Head(Red), Forearms, Forearms(Red), Tail, Tail(Red)', 
impact='Head, Head(Red), Forearms, Forearms(Red), Tail, Tail(Red)', projectile='Head, Forearms, Tail')

Proficiency.noElement(Brachydios_Raging.id)
Ailments.createStatus(mon_id= Brachydios_Raging.id, status="", blight="Blast Blight", natural="Tremors, Roars (Large)")

Egames.putInGames(Brachydios_Raging.id,  ['MH4U', 'MHGU', 'MHWI'])


##################  Glavenus ##################
addWeakness = Weakness()

Glavenus= Monster(name='Glavenus', generation=4, group='brute', variation=1)
Glavenus.create(Glavenus)

Item_weak.applyItemWeakness(mon_id= Glavenus.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.onlyWeakElement(mon_id= Glavenus.id, element='water')
addWeakness.onlyWeakStatus(mon_id= Glavenus.id, status='poison')
Weakpoints.createWeakPoints(mon_id= Glavenus.id, cut='Head, Throat, Tail(Heated)', impact='Head, Throat, Tail(Heated)', 
projectile='Head, Horns, Tail(Heated)')

Proficiency.onlyGoodAt(mon_id= Glavenus.id, element='fire')
Ailments.createStatus(mon_id= Glavenus.id, status="", blight="Fire blight", natural="Roar (Large)")

Egames.putInGames(Glavenus.id,  ['MHGU', 'MHWI'])


################## Acidic Glavenus ##################
addWeakness = Weakness()

Glavenus_Acidic= Monster(name='Acidic Glavenus', generation=5, group='brute', variation=2)
Glavenus_Acidic.create(Glavenus_Acidic)

Item_weak.applyItemWeakness(mon_id= Glavenus_Acidic.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.onlyWeakElement(mon_id= Glavenus_Acidic.id, element='fire')
addWeakness.noWeaknessStatus(mon_id= Glavenus_Acidic.id)
Weakpoints.createWeakPoints(mon_id= Glavenus_Acidic.id, cut='Throat, Back, Tail(Sharpened)', impact='Head, Throat, Back, Tail(Sharpened)', 
projectile='Head, Throat, Tail(Sharpened)')

Proficiency.noElement(Glavenus_Acidic.id)
Ailments.createStatus(mon_id= Glavenus_Acidic.id, status="Defence Down", blight="", natural="Roar (Large)")

Egames.putInGames(Glavenus_Acidic.id,  ['MHWI'])

Glavenus.family(Glavenus_Acidic)

################## Hellblade Glavenus ##################
addWeakness = Weakness()

Glavenus_Hellblade= Monster(name='Hellblade Glavenus', generation=4, group='brute', variation=5)
Glavenus_Hellblade.create(Glavenus_Hellblade)

Item_weak.applyItemWeakness(mon_id= Glavenus_Hellblade.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= Glavenus_Hellblade.id, fire=False, water=True, thunder=False, ice=True, dragon=False)
addWeakness.onlyWeakStatus(mon_id= Glavenus_Hellblade.id, status='poison')
Weakpoints.createWeakPoints(mon_id= Glavenus_Hellblade.id, cut='Head, Throat, Tail [Normal/Heated]', impact='Head, Throat, Tail [Normal/Heated]', 
projectile='Throat, Horns(Normal/Heated)')

Proficiency.onlyGoodAt(mon_id= Glavenus_Hellblade.id, element='fire')
Ailments.createStatus(mon_id= Glavenus_Hellblade.id, status="", blight="Blast blight", natural="Stun, Wind Pressure (low), Roar (Large)")

Egames.putInGames(Glavenus_Hellblade.id,  ['MHGU'])


Glavenus.family(Glavenus_Hellblade)
Glavenus_Acidic.family(Glavenus_Hellblade)


################## Anjanath ##################
addWeakness = Weakness()

Anjanath= Monster(name='Anjanath', generation=5, group='brute', variation=1)
Anjanath.create(Anjanath)

Item_weak.applyItemWeakness(mon_id= Anjanath.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.onlyWeakElement(mon_id= Anjanath.id, element='water')
addWeakness.noWeaknessStatus(Anjanath.id)
Weakpoints.createWeakPoints(mon_id= Anjanath.id, cut='Nose, Head, Wings, Legs, Tail', impact='Nose, Head, Wings, Legs, Tail', projectile='Nose, Head, Body, Wings, Legs, Tail')

Proficiency.onlyGoodAt(Anjanath.id, 'fire')
Ailments.createStatus(mon_id= Anjanath.id, status="", blight="Fire blight", natural="Roars (Small), Wind Pressure (Small), Tremors")

Egames.putInGames(Anjanath.id,  ['MHWI', 'MHRS'])


################## Fulgur Anjanath ##################
addWeakness = Weakness()

Anjanath_Fulgur= Monster(name='Fulgur Anjanath', generation=5, group='brute', variation=2)
Anjanath_Fulgur.create(Anjanath_Fulgur)

Item_weak.applyItemWeakness(mon_id= Anjanath_Fulgur.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= Anjanath_Fulgur.id, fire=False, water=True, thunder=False, ice=True, dragon=False)
addWeakness.noWeaknessStatus(Anjanath_Fulgur.id)
Weakpoints.createWeakPoints(mon_id= Anjanath_Fulgur.id, cut='Nose, Head, Wings, Legs, Tail', impact='Nose, Head, Wings, Legs, Tail', projectile='Nose, Head, Body, Wings, Legs, Tail')

Proficiency.onlyGoodAt(Anjanath_Fulgur.id, 'thunder')
Ailments.createStatus(mon_id= Anjanath_Fulgur.id, status="", blight="Thunder blight", natural="Roar (Small), Tremors")

Egames.putInGames(Anjanath_Fulgur.id,  ['MHWI'])


Brachydios.family(Brachydios_Raging)
Anjanath.family(Anjanath_Fulgur)