# Create Monsters from the Snake Wyvern Phylum

from app import app, db
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games


################## Najarala ##################
addWeakness = Weakness()
games = Games()

najarala= Monster(name='Najarala', generation=4, phylum='snake', variation=1)
najarala.create(najarala)

Item_weak.applyItemWeakness(mon_id= najarala.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= najarala.id, fire=False, water=True, thunder=False, ice=True, dragon=False)
addWeakness.noWeaknessStatus(mon_id= najarala.id)
Weakpoints.createWeakPoints(mon_id= najarala.id, cut='Head, Tail, Back Legs, R.Organs', impact='Head, Tail, Back Legs, R.Organs', projectile='Head, Tail, Back Legs')

Proficiency.noElement(mon_id= najarala.id)
Ailments.createStatus(mon_id= najarala.id, poison=False, sleep=False, para=True, blast=False, stun=True, tremor=False, roar=True, wind=False)
games.inMHGen4(mon_id= najarala.id, MH4U=True, MHGU=True)



################## Tidal Najarala ##################
addWeakness = Weakness()
games = Games()

najarala_tidal= Monster(name='Tidal Najarala', generation=4, phylum='snake', variation=2)
najarala_tidal.create(najarala_tidal)

Item_weak.applyItemWeakness(mon_id= najarala_tidal.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= najarala_tidal.id, fire=True, water=False, thunder=True, ice=False, dragon=False)
addWeakness.noWeaknessStatus(mon_id= najarala_tidal.id)
Weakpoints.createWeakPoints(mon_id= najarala_tidal.id, cut='Head, Tail, Back Legs, R.Organs', impact='Head, Tail, Back Legs, R.Organs', projectile='Head, Tail, Back Legs')

Proficiency.applyStrenghts(mon_id= najarala_tidal.id, fire=False, water=True, thunder=False, ice=False, dragon=False)
Ailments.createStatus(mon_id= najarala_tidal.id, poison=False, sleep=False, para=True, blast=False, stun=False, tremor=False, roar=True, wind=False)
games.inMHGen4(mon_id= najarala_tidal.id, MH4U=True, MHGU=False)

najarala.family(najarala_tidal) # T.Najarala is subspecies of Najarala