# Create Monsters
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Egames

            ### Gore Magala   ###
addWeakness = Weakness()
gore_magala = Monster(name='Gore Magala', generation=4, group='???', variation=1)
gore_magala.create(gore_magala)

Item_weak.applyItemWeakness(mon_id= gore_magala.id, shock_trap=True, pitfall_trap=True, flash_bomb=False, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= gore_magala.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= gore_magala.id, poison=True, sleep=False, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id= gore_magala.id, cut='Head, Neck, Front Legs, Tail', impact='Head,  Neck, Front Legs, Tail', projectile='Head, Neck, Back Legs')

Proficiency.noElement(gore_magala.id)
Ailments.createStatus(mon_id= gore_magala.id, status="", blight="Frenzy virus", natural="Roar, Wind Pressure")
Egames.putInGames(gore_magala.id,  ['MH4U', 'MHGU'])


            ### Shagaru Magala   ###
addWeakness = Weakness()
shagaru_magala = Monster(name='Shagaru Magala', generation=4, group='elder', variation=1)
shagaru_magala.create(shagaru_magala)

Item_weak.elderBlock(shagaru_magala.id)
addWeakness.applyWeaknessElement(mon_id= shagaru_magala.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= shagaru_magala.id, poison=True, sleep=False, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id= shagaru_magala.id, cut='Head, Neck', impact='Head', projectile='Head, Neck, Back Legs')

Proficiency.noElement(shagaru_magala.id)
Ailments.createStatus(mon_id= shagaru_magala.id, status="", blight="Frenzy virus", natural="Roar(L), Wind Pressure")
Egames.putInGames(shagaru_magala.id,  ['MH4U', 'MHGU'])


gore_magala.family(shagaru_magala)
shagaru_magala.family(gore_magala)


            ### Chaotic Gore Magala   ###
addWeakness = Weakness()
gore_magala_chaotic = Monster(name='Chaotic Gore Magala', generation=4, group='???', variation=4)
gore_magala_chaotic.create(gore_magala_chaotic)

Item_weak.applyItemWeakness(mon_id= gore_magala_chaotic.id, shock_trap=True, pitfall_trap=True, flash_bomb=False, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= gore_magala_chaotic.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= gore_magala_chaotic.id, poison=True, sleep=False, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id= gore_magala_chaotic.id, cut='Head, Neck, Front Legs, Tail', impact='Head,  Neck, Front Legs, Tail', projectile='Head, Neck, Back Legs')

Proficiency.noElement(gore_magala_chaotic.id)
Ailments.createStatus(mon_id= gore_magala_chaotic.id, status="", blight="Frenzy virus", natural="Wind Pressure, Roar")
Egames.putInGames(gore_magala_chaotic.id,  ['MH4U', 'MHGU'])


gore_magala.family(gore_magala_chaotic)
shagaru_magala.family(gore_magala)
shagaru_magala.family(gore_magala_chaotic)


################## Fatalis ##################
addWeakness = Weakness()
Fatalis= Monster(name='Fatalis', generation=1, group='elder', variation=1)
Fatalis.create(Fatalis)

Item_weak.elderBlock(Fatalis.id)
addWeakness.applyWeaknessElement(mon_id= Fatalis.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.noWeaknessStatus(Fatalis.id)
Weakpoints.createWeakPoints(mon_id= Fatalis.id, cut='Head, Chest, Forelegs', impact='Head, Chest, Forelegs', projectile='Chest, Forelegs')

Proficiency.applyStrenghts(mon_id= Fatalis.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
Ailments.createStatus(mon_id= Fatalis.id, status="", blight="Dragon Blight, Fire Blight", natural="Roar(L), Wind Pressure (L)")
Egames.putInGames(Fatalis.id,  ['MHF', 'MHFU', 'MH4U', 'MHGU', 'MHWI'])

 
################# Gogmazios ##################
addWeakness = Weakness()
Gogmazios = Monster(name='Gogmazios', generation=4, group='elder', variation=1)
Gogmazios.create(Gogmazios)

Item_weak.elderBlock(Gogmazios.id)
addWeakness.applyWeaknessElement(mon_id= Gogmazios.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.noWeaknessStatus(Gogmazios.id)
Weakpoints.createWeakPoints(mon_id= Gogmazios.id, cut='Front Leg', impact='Back Leg', projectile='Front Leg, Back Leg')

Proficiency.onlyGoodAt(Gogmazios.id, 'fire')
Ailments.createStatus(mon_id= Gogmazios.id, status="Tar", blight="Fireblight", natural="Roar (L)")
Egames.putInGames(Gogmazios.id,  ['MH4U'])
