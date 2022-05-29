# Create Monsters from the Bird Wyvern group
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games


##################  Velocidrome ##################
addWeakness = Weakness()
games = Games()

Velocidrome = Monster(name='Velocidrome',generation=1,group='bird',variation=1)
Velocidrome.create(Velocidrome)

Item_weak.applyItemWeakness(mon_id=Velocidrome.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Velocidrome.id,fire=False,water=False,thunder=True,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Velocidrome.id)
Weakpoints.createWeakPoints(mon_id=Velocidrome.id,cut='Head, Body',impact='Head, Body',projectile='Head, Body')

Proficiency.noElement(mon_id=Velocidrome.id)
Ailments.createStatus(mon_id=Velocidrome.id, status='none', blight='none', natural='none')
games.inMHOld(mon_id=Velocidrome.id,MHF=True,MHF2=True)
games.inMHGen4(mon_id=Velocidrome.id,MH4U=True,MHGU=True)


################## Izuchi ##################
addWeakness = Weakness()
games = Games()

Izuchi = Monster(name='Izuchi',generation=5,group='bird',variation=1)
Izuchi.create(Izuchi)

Item_weak.applyItemWeakness(mon_id=Izuchi.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Izuchi.id,fire=False,water=True,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Izuchi.id)
Weakpoints.createWeakPoints(mon_id=Izuchi.id,cut='Head, Body',impact='Head, Body',projectile='Head, Body')

Proficiency.noElement(mon_id=Izuchi.id)
Ailments.createStatus(mon_id=Izuchi.id, status='', blight='', natural='')
games.inMHGen5(mon_id=Izuchi.id,MHWI=False,MHRS=True)

################## Malfestio ##################
addWeakness = Weakness()
games = Games()

Malfestio = Monster(name='Malfestio',generation=4,group='bird',variation=1)
Malfestio.create(Malfestio)

Item_weak.applyItemWeakness(mon_id=Malfestio.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Malfestio.id,fire=True,water=True,thunder=False,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Malfestio.id)
Weakpoints.createWeakPoints(mon_id=Malfestio.id,cut='Head, Right Wing, Left Wing, Tail',impact='Head, Right Wing, Left Wing, Tail',projectile='Head, Right Wing, Left Wing, Tail')

Proficiency.noElement(mon_id=Malfestio.id)
Ailments.createStatus(mon_id= Malfestio.id, status="Sleep, Confuse", blight="", natural="Wind pressure (small), Roar (small)")

games.inMHGen4(mon_id=Malfestio.id,MH4U=False,MHGU=True)

################## Nightcloak Malfestio ##################
addWeakness = Weakness()
games = Games()

Malfestio_Nightcloak = Monster(name='Nightcloak Malfestio',generation=4,group='bird',variation=5)
Malfestio_Nightcloak.create(Malfestio_Nightcloak)

Item_weak.applyItemWeakness(mon_id=Malfestio_Nightcloak.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Malfestio_Nightcloak.id,fire=True,water=True,thunder=False,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Malfestio_Nightcloak.id)
Weakpoints.createWeakPoints(mon_id=Malfestio_Nightcloak.id,cut='Head, Right Wing, Left Wing, Tail',impact='Head, Right Wing, Left Wing, Tail',projectile='Head, Right Wing, Left Wing, Tail')

Proficiency.noElement(mon_id=Malfestio_Nightcloak.id)
Ailments.createStatus(mon_id= Malfestio_Nightcloak.id, status="Sleep, Confuse", blight="", natural="Wind pressure (small), Roar (small)")

games.inMHGen4(mon_id=Malfestio_Nightcloak.id,MH4U=False,MHGU=True)


################## Aknosom ##################
addWeakness = Weakness()
games = Games()

Aknosom = Monster(name='Aknosom',generation=5,group='bird',variation=1)
Aknosom.create(Aknosom)

Item_weak.applyItemWeakness(mon_id=Aknosom.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Aknosom.id,fire=False,water=True,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Aknosom.id)
Weakpoints.createWeakPoints(mon_id=Aknosom.id,cut='Head, Crest, Neck, Torso, Wing, Legs, Tail, Tail Tip',impact='Head, Crest, Neck, Torso, Wing, Legs, Tail, Tail Tip',projectile='Head, Crest, Neck, Torso, Wing, Legs, Tail, Tail Tip')

Proficiency.onlyGoodAt(mon_id=Aknosom.id,element='fire')
Ailments.createStatus(mon_id= Aknosom.id, status="", blight="Fire blight", natural="Wind pressure (small)")

games.inMHGen5(mon_id=Aknosom.id,MHWI=False,MHRS=True)


Malfestio.family(Malfestio_Nightcloak)
