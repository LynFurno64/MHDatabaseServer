from app import app, db
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games

addWeakness = Weakness()


################## ADD Neopteron ##################
from app.createMonsters import neopteron

################## ADD Temnoceran ##################
from app.createMonsters import temnoceran

################## ADD Bird Wyvern ##################
from app.createMonsters import birdWyvern

################## ADD Flying Wyvern ##################
#from app.createMonsters import flyingWyvern

################## ADD Piscine Wyvern ##################
################## ADD Carapaceon     ##################
################## ADD Amphibian      ##################
################## ADD Fanged Beast   ##################
################## ADD Leviathan      ##################
################## ADD Snake Wyvern   ##################
from app.createMonsters import snakeWyern

################## ADD Brute Wyvern   ##################
################## ADD Fanged Wyvern   ##################

################## ADD Elder Dragon   ##################
from app.createMonsters import elderDragon

games = Games()
################## ADD ???   ##################
            ### Gore Magala   ###
addWeakness = Weakness()
games = Games()
gore_magala = Monster(name='Gore Magala', generation=4, phylum='???', variation=1)
gore_magala.create(gore_magala)

Item_weak.applyItemWeakness(mon_id= gore_magala.id, shock_trap=True, pitfall_trap=True, flash_bomb=False, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= gore_magala.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= gore_magala.id, poison=True, sleep=False, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id= gore_magala.id, cut='Head, Neck, Front Legs, Tail', impact='Head,  Neck, Front Legs, Tail', projectile='Head, Neck, Back Legs')

Proficiency.noElement(mon_id= gore_magala.id)
Ailments.createStatus(mon_id= gore_magala.id, poison=False, sleep=False, para=False, blast=False, stun=False, tremor=True, roar=True, wind=True)
games.inMHGen4(mon_id= gore_magala.id, MH4U=True, MHGU=True)

            ### Shagaru Magala   ###
addWeakness = Weakness()
games = Games()
shagaru_magala = Monster(name='Shagaru Magala', generation=4, phylum='elder', variation=1)
shagaru_magala.create(shagaru_magala)

Item_weak.elderBlock(mon_id= shagaru_magala.id)
addWeakness.applyWeaknessElement(mon_id= shagaru_magala.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= shagaru_magala.id, poison=True, sleep=False, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id= shagaru_magala.id, cut='Head, Neck', impact='Head', projectile='Head, Neck, Back Legs')

Proficiency.noElement(mon_id= shagaru_magala.id)
Ailments.createStatus(mon_id= shagaru_magala.id, poison=False, sleep=False, para=False, blast=False, stun=False, tremor=True, roar=True, wind=False)
games.inMHGen4(mon_id= shagaru_magala.id, MH4U=True, MHGU=True)

            ### Chaotic Gore Magala   ###
addWeakness = Weakness()
games = Games()
gore_magala_chaotic = Monster(name='Chaotic Gore Magala', generation=4, phylum='???', variation=4)
gore_magala_chaotic.create(gore_magala_chaotic)

Item_weak.applyItemWeakness(mon_id= gore_magala_chaotic.id, shock_trap=True, pitfall_trap=True, flash_bomb=False, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= gore_magala_chaotic.id, fire=True, water=False, thunder=False, ice=False, dragon=True)
addWeakness.applyWeaknessStatus(mon_id= gore_magala_chaotic.id, poison=True, sleep=False, para=False, blast=False)
Weakpoints.createWeakPoints(mon_id= gore_magala_chaotic.id, cut='Head, Neck, Front Legs, Tail', impact='Head,  Neck, Front Legs, Tail', projectile='Head, Neck, Back Legs')

Proficiency.noElement(mon_id= gore_magala_chaotic.id)
Ailments.createStatus(mon_id= gore_magala_chaotic.id, poison=False, sleep=False, para=False, blast=False, stun=False, tremor=True, roar=True, wind=True)
games.inMHGen4(mon_id= gore_magala_chaotic.id, MH4U=True, MHGU=True)

gore_magala.family(gore_magala_chaotic)
shagaru_magala.family(gore_magala)
shagaru_magala.family(gore_magala_chaotic)

print('COMPLETED!!')