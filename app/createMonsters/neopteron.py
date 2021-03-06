# Create Monsters from the Neopteron group
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Egames


################## Seltas ##################
addWeakness = Weakness()

seltas = Monster(name='Seltas', generation=4, group='bug', variation=1)
seltas.create(seltas)
Item_weak.applyItemWeakness(mon_id= seltas.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)

addWeakness.applyWeaknessElement(mon_id= seltas.id, fire=True, water=False, thunder=True, ice=False, dragon=False)
addWeakness.applyWeaknessStatus(mon_id= seltas.id, poison=False, sleep=True, para=True, blast=False)
Weakpoints.createWeakPoints(mon_id= seltas.id, cut='Head, Legs, Torso', impact='Head, Legs, Torso', projectile='Head, Claws, Legs, Torso')

Proficiency.noElement(mon_id= seltas.id)
Ailments.createStatus(mon_id= seltas.id, status="Defence Down", blight="", natural="")

Egames.putInGames(seltas.id, ['MH4U', 'MHGU'])

################## Desert Seltas ##################
addWeakness = Weakness()

seltas_Desert = Monster(name='Desert Seltas', generation=4, group='bug', variation=2)
seltas_Desert.create(seltas_Desert)
Item_weak.applyItemWeakness(mon_id= seltas_Desert.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)

addWeakness.applyWeaknessElement(mon_id= seltas_Desert.id, fire=False, water=False, thunder=True, ice=True, dragon=False)
addWeakness.applyWeaknessStatus(mon_id= seltas_Desert.id, poison=False, sleep=True, para=True, blast=False)
Weakpoints.createWeakPoints(mon_id= seltas_Desert.id, cut='Head, Legs, Belly', impact='Head, Legs, Belly', projectile='Head, Claws, Legs, Belly')

Proficiency.noElement(mon_id= seltas_Desert.id)
Ailments.createStatus(mon_id= seltas_Desert.id, status="Para", blight="", natural="")

Egames.inGame(seltas_Desert.id, 'MH4U')

seltas_Desert.family(seltas)

################## Seltas Queen ##################
addWeakness = Weakness()

seltas_queen = Monster(name='Seltas Queen', generation=4, group='bug', variation=1)
seltas_queen.create(seltas_queen)

Item_weak.applyItemWeakness(mon_id= seltas_queen.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= seltas_queen.id, fire=True, water=False, thunder=False, ice=True, dragon=False)
addWeakness.applyWeaknessStatus(mon_id= seltas_queen.id, poison=True, sleep=False, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id= seltas_queen.id, cut='Head, Belly', impact='Head, Belly', projectile='None')

Proficiency.applyStrenghts(mon_id= seltas_queen.id, fire=False, water=True, thunder=False, ice=False, dragon=False)
Ailments.createStatus(mon_id= seltas_queen.id, status="Soiled", blight="Severe Waterblight", natural="Stun")

Egames.putInGames(seltas_queen.id, ['MH4U', 'MHGU'])

seltas_queen.family(seltas)
seltas_queen.family(seltas_Desert)

################## Desert Seltas Queen ##################
addWeakness = Weakness()

seltas_queen_Desert = Monster(name='Desert Seltas Queen', generation=4, group='bug', variation=2)
seltas_queen_Desert.create(seltas_queen_Desert)

Item_weak.applyItemWeakness(mon_id= seltas_queen_Desert.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= seltas_queen_Desert.id, fire=False, water=True, thunder=True, ice=False, dragon=False)
addWeakness.applyWeaknessStatus(mon_id= seltas_queen_Desert.id, poison=True, sleep=True, para=True, blast=False)
Weakpoints.createWeakPoints(mon_id= seltas_queen_Desert.id, cut='Head', impact='Head', projectile='Belly(Break)')

Proficiency.applyStrenghts(mon_id= seltas_queen_Desert.id, fire=False, water=True, thunder=False, ice=False, dragon=False)
Ailments.createStatus(mon_id= seltas_queen_Desert.id, status="Soiled", blight="", natural="Stun, Tremor")

Egames.inGame(seltas_queen_Desert.id, 'MH4U')


seltas_queen_Desert.family(seltas)
seltas_queen_Desert.family(seltas_Desert)
seltas_queen_Desert.family(seltas_queen)

################## Ahtal-Ka ##################
addWeakness = Weakness()

ahtal_ka = Monster(name='Ahtal-Ka', generation=4, group='bug', variation=1)
ahtal_ka.create(ahtal_ka)

Item_weak.elderBlock(mon_id= ahtal_ka.id)
addWeakness.applyWeaknessElement(mon_id= ahtal_ka.id, fire=False, water=True, thunder=True, ice=False, dragon=False)
addWeakness.noWeaknessStatus(mon_id= ahtal_ka.id)
Weakpoints.createWeakPoints(mon_id= ahtal_ka.id, cut='Head, Claws, Arms, Legs', impact='Head, Claws, Arms, Legs', projectile='Head, Tail')

Proficiency.noElement(mon_id= ahtal_ka.id)
Ailments.createStatus(mon_id= ahtal_ka.id, status="Defence Down", blight="", natural="Webbed")

Egames.inGame(ahtal_ka.id, 'MHGU')