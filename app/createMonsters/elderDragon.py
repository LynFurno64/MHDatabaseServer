# Create Monsters from the Elder Dragon group
from re import T
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Egames

################## Lunastra ##################
addWeakness = Weakness()

################## Teostra ##################
addWeakness = Weakness()


################## Amatsu ##################
addWeakness = Weakness()


################## Ceadeus ##################
addWeakness = Weakness()

################## Goldbeard Ceadeus ##################
addWeakness = Weakness()

################## Valstrax ##################
addWeakness = Weakness()
Valstrax= Monster(name='Valstrax', generation=4, group='elder', variation=1)
Valstrax.create(Valstrax)

Item_weak.applyItemWeakness(mon_id= Valstrax.id, shock_trap=False, pitfall_trap=False, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= Valstrax.id, fire=True, water=True, thunder=True, ice=True, dragon=False)
addWeakness.applyWeaknessStatus(mon_id= Valstrax.id, poison=False, sleep=False, para=False, blast=True)
Weakpoints.createWeakPoints(mon_id= Valstrax.id, cut='Head, Head (Enraged)', impact='Head, Head (Enraged)', projectile='Head, Head (Enraged), Body, Wing Talons')

Proficiency.onlyGoodAt(mon_id=Valstrax.id, element='dragon')
Ailments.createStatus(mon_id= Valstrax.id, status="", blight="Dragon blight", natural=" Roar(L)")

Egames.putInGames(Valstrax.id,  ['MHGU'])

################# Crimson Glow Valstrax ##################
addWeakness = Weakness()
Valstrax_Crimson= Monster(name='Crimson Glow Valstrax', generation=5, group='elder', variation=4)
Valstrax_Crimson.create(Valstrax_Crimson)

Item_weak.applyItemWeakness(mon_id= Valstrax_Crimson.id, shock_trap=False, pitfall_trap=False, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= Valstrax_Crimson.id, fire=True, water=True, thunder=True, ice=True, dragon=False)
addWeakness.applyWeaknessStatus(mon_id= Valstrax_Crimson.id, poison=False, sleep=True, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id= Valstrax_Crimson.id, cut='Head, Neck, Wing Arm, Tail', impact='Head, Wing Arm, Wing', projectile='Wing Arm')

Proficiency.onlyGoodAt(mon_id= Valstrax_Crimson.id, element='dragon')
Ailments.createStatus(mon_id= Valstrax_Crimson.id, status="", blight="Dragon blight", natural=" Roar(L)")

Egames.putInGames(Valstrax_Crimson.id,  ['MHRS'])

Valstrax.family(Valstrax_Crimson)


################# Nergigante ##################
addWeakness = Weakness()
Nergigante= Monster(name='Nergigante', generation=5, group='elder', variation=1)
Nergigante.create(Nergigante)

Item_weak.elderBlock(mon_id= Nergigante.id)
addWeakness.applyWeaknessElement(mon_id= Nergigante.id, fire=False, water=False, thunder=True, ice=False, dragon=True)
addWeakness.noWeaknessStatus(mon_id= Nergigante.id)
Weakpoints.createWeakPoints(mon_id= Nergigante.id, cut='Head [Normal & White], Forearm [Normal & White], Wings (White), Tail, Tail Tip [Normal & White]', 
impact='Head [Normal & White], Forearm [Normal & White],  Wings (White), Tail, Tail Tip (White)', 
projectile='Horn (Wounded), Head (White), Forearm (White), Wings (White)')

Proficiency.noElement(mon_id= Nergigante.id)
Ailments.createStatus(mon_id= Nergigante.id, status="", blight="", natural="Roar(L), Wind Pressure (S)")
Egames.putInGames(Nergigante.id,  ['MHWI'])

################# Ruiner Nergigante ##################
addWeakness = Weakness()
Nergigante_Ruiner= Monster(name='Ruiner Nergigante', generation=5, group='elder', variation=4)
Nergigante_Ruiner.create(Nergigante_Ruiner)

Item_weak.elderBlock(mon_id= Nergigante_Ruiner.id)
addWeakness.onlyWeakElement(mon_id= Nergigante_Ruiner.id, element='dragon')
addWeakness.noWeaknessStatus(mon_id= Nergigante_Ruiner.id)
Weakpoints.createWeakPoints(mon_id= Nergigante_Ruiner.id, cut='Head [Normal & White], Forearm [Normal & White], Wings (White), Tail, Tail Tip [Normal & White]', 
impact='Head [Normal & White], Forearm [Normal & White],  Wings (White), Tail, Tail Tip (White)', 
projectile='Horn (Wounded), Head [Normal & White], Forearm (White), Wings (White), Tail Tip (White)')

Proficiency.noElement(mon_id= Nergigante_Ruiner.id)
Ailments.createStatus(mon_id= Nergigante_Ruiner.id, status="Bleeding", blight="", natural="Roar(L)")
Egames.putInGames(Nergigante_Ruiner.id,  ['MHWI'])
Nergigante.family(Nergigante_Ruiner)

################## ibushi ##################
addWeakness = Weakness()
ibushi = Monster(name='Ibushi', generation=5, group='elder', variation=1)
ibushi.create(ibushi)

Item_weak.elderBlock(mon_id= ibushi.id)
addWeakness.applyWeaknessElement(mon_id= ibushi.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.noWeaknessStatus(mon_id= ibushi.id)
Weakpoints.createWeakPoints(mon_id= ibushi.id, cut='Head, Chest, Wingarm, Back, Tail Tip', impact='Head, Chest, Wingarm, Back, Tail Tip', projectile='Head, Chest, Wingarm, Back, Tail Tip')

Proficiency.onlyGoodAt(mon_id= ibushi.id, element='dragon')
Ailments.createStatus(mon_id= ibushi.id, status="", blight="Dragon blight", natural="Wind pressure (Large), Roar (Large)")

Egames.putInGames(ibushi.id,  ['MHRS'])

################## Narwa ##################
addWeakness = Weakness()

narwa = Monster("Narwa", 5, "elder", 1)
narwa.create(narwa)

Item_weak.elderBlock(mon_id= narwa.id)
addWeakness.applyWeaknessElement(mon_id= narwa.id, fire=False, water=False, thunder=False, ice=True, dragon=True)
addWeakness.noWeaknessStatus(mon_id= narwa.id)
Weakpoints.createWeakPoints(mon_id= narwa.id, cut='Head, Chest(Charged), Wingarm(Charged), Abdomen, Back, Tail Tip(Charged)', 
impact='Head, Chest(Charged), Wingarm(Charged), Abdomen, Back, Tail Tip(Charged)', projectile='Head, Chest(Charged), Wingarm(Charged), Abdomen')

Proficiency.onlyGoodAt(mon_id= narwa.id, element='thunder')
Ailments.createStatus(mon_id= narwa.id, status="", blight="Thunder blight", natural="Roar (Large)")
Egames.putInGames(narwa.id,  ['MHRS'])

narwa.family(ibushi)


################## Narwa Allmother ##################
addWeakness = Weakness()

narwa_allmother = Monster("Narwa Allmother", 5, "elder", 4)
narwa_allmother.create(narwa_allmother)

Item_weak.elderBlock(mon_id= narwa_allmother.id)
addWeakness.applyWeaknessElement(mon_id= narwa_allmother.id, fire=False, water=False, thunder=False, ice=True, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= narwa_allmother.id, poison=False, sleep=False, para=False, blast=True)
Weakpoints.createWeakPoints(mon_id= narwa_allmother.id, cut='Head, Chest(Charged), Wingarm(Charged), Abdomen, Back, Tail Tip(Charged)', 
impact='Head, Chest(Charged), Wingarm(Charged), Abdomen, Back, Tail Tip(Charged)', projectile='Head, Wingarm(Charged), Abdomen, Tail Tip(Charged)')

Proficiency.onlyGoodAt(mon_id= narwa_allmother.id, element='thunder')
Ailments.createStatus(mon_id= narwa_allmother.id, status="", blight="Thunder blight", natural="Wind pressure (Large), Roar (Large)")
Egames.putInGames(narwa_allmother.id,  ['MHRS'])

narwa.family(narwa_allmother)
ibushi.family(narwa_allmother)