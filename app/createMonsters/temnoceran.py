# Create Monsters from the Temnoceran Phylum
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Egames


################## Nerscylla ##################
addWeakness = Weakness()

Nerscylla = Monster(name='Nerscylla', generation=4, group='spider', variation=1)
Nerscylla.create(Nerscylla)
Item_weak.applyItemWeakness(mon_id= Nerscylla.id, shock_trap=True, pitfall_trap=True, flash_bomb=False, sonic_bomb=False)

addWeakness.applyWeaknessElement(mon_id= Nerscylla.id, fire=True, water=False, thunder=True, ice=False, dragon=False)
addWeakness.applyWeaknessStatus(mon_id= Nerscylla.id, poison=False, sleep=False, para=True, blast=False)
Weakpoints.createWeakPoints(mon_id= Nerscylla.id, cut='Head, Belly', impact='Head, Belly', projectile='Head, Stinger, Belly')

Proficiency.noElement(mon_id= Nerscylla.id)
Ailments.createStatus(mon_id= Nerscylla.id, status="Poison,  Noxious Poison, Sleep", blight="", natural="Webbed")

Egames.putInGames(Nerscylla.id, ['MH4U', 'MHGU'])

################## Shrouded Nerscylla ##################
addWeakness = Weakness()

Shrouded_Nerscylla = Monster(name='Shrouded Nerscylla', generation=4, group='spider', variation=2)
Shrouded_Nerscylla.create(Shrouded_Nerscylla)
Item_weak.applyItemWeakness(mon_id= Shrouded_Nerscylla.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)

addWeakness.applyWeaknessElement(mon_id= Shrouded_Nerscylla.id, fire=True, water=False, thunder=False, ice=True, dragon=False)
addWeakness.noWeaknessStatus(mon_id= Shrouded_Nerscylla.id)
Weakpoints.createWeakPoints(mon_id= Shrouded_Nerscylla.id, cut='Head, Belly', impact='Head, Belly', projectile='Head, Stinger, Belly')

Proficiency.noElement(mon_id= Shrouded_Nerscylla.id)
Ailments.createStatus(mon_id= Shrouded_Nerscylla.id, status="Poison,  Noxious Poison, Paralysis", blight="", natural="Webbed")

Egames.inGame(Shrouded_Nerscylla.id, 'MH4U')

Nerscylla.family(Shrouded_Nerscylla)



################## Rakna-Kadaki ##################
addWeakness = Weakness()

