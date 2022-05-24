# Create Monsters from the Amphibian group
from re import T
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games

##################  Tetsucabra ##################
addWeakness = Weakness()
games = Games()

Tetsucabra = Monster(name='Tetsucabra',generation=4,group='frog',variation=1)
Tetsucabra.create(Tetsucabra)

Item_weak.applyItemWeakness(mon_id=Tetsucabra.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Tetsucabra.id,fire=False,water=True,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Tetsucabra.id)
Weakpoints.createWeakPoints(mon_id=Tetsucabra.id,cut='Head, Front Legs, Hind legs,Tail',impact='Head,Front Legs,Hind Legs,Tail',projectile='Head, Front Legs,Hind Legs, Tail')

Proficiency.noElement(mon_id=Tetsucabra.id)
Ailments.createStatus(mon_id=Tetsucabra.id, status="", blight="", natural="Small Roars, Tremors")
games.inMHGen4(mon_id=Tetsucabra.id,MH4U=True,MHGU=True)

##################  Drilltusk Tetsucabra ##################
addWeakness = Weakness()
games = Games()

Tetsucabra_Drilltusk = Monster(name= 'Drilltusk Tetsucabra',generation=4,group='frog',variation=5)
Tetsucabra_Drilltusk.create(Tetsucabra_Drilltusk)

Item_weak.applyItemWeakness(mon_id=Tetsucabra_Drilltusk.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Tetsucabra_Drilltusk.id,fire=False,water=True,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Tetsucabra_Drilltusk.id)
Weakpoints.createWeakPoints(mon_id=Tetsucabra_Drilltusk.id,cut='Head, Front Legs, Hind legs,Tail',impact='Head, Front Legs, Hind Legs, Tail',projectile='Head, Front Legs, Hind Legs, Tail')

Proficiency.noElement(mon_id=Tetsucabra_Drilltusk.id)
Ailments.createStatus(mon_id= Tetsucabra_Drilltusk.id, status="", blight="", natural="Small Roars, Tremors")
games.inMHGen4(mon_id=Tetsucabra_Drilltusk.id,MH4U=False,MHGU=True)

Tetsucabra.family(Tetsucabra_Drilltusk)


##################  Zamtrios ##################
addWeakness = Weakness()
games = Games()

Zamtrios = Monster(name='Zamtrios',generation=4,group='frog',variation=1)
Zamtrios.create(Zamtrios)

Item_weak.applyItemWeakness(mon_id=Zamtrios.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Zamtrios.id,fire=True,water=False,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Zamtrios.id)
Weakpoints.createWeakPoints(mon_id=Zamtrios.id,cut='Head, Fin, Tail, Belly',impact='Head, Fin, Tail, Belly',projectile='Head, Fin, Tail, Belly')

Proficiency.applyStrenghts(mon_id=Zamtrios.id, fire=False, water=True, thunder=False, ice=True, dragon=False)
Ailments.createStatus(mon_id= Zamtrios.id, status="", blight="Ice and Water Blights", natural="Tremors, Large Roars, Snowman")

games.inMHGen4(mon_id=Zamtrios.id,MH4U=True,MHGU=True)



##################  Tetranadon ##################
addWeakness = Weakness()
games = Games()

Tetranadon = Monster(name='Tetranadon',generation=5,group='frog',variation=1)
Tetranadon.create(Tetranadon)

Item_weak.applyItemWeakness(mon_id=Tetranadon.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Tetranadon.id,fire=True,water=False,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Tetranadon.id)
Weakpoints.createWeakPoints(mon_id=Tetranadon.id,cut='Head, Neck, Torso, Foreleg, Back, Hind Leg, Tail', impact='Head, Neck, Torso, Foreleg, Back, Hind Leg, Tail',projectile='Head, Neck, Torso, Foreleg, Back, Hind Leg, Tail')

Proficiency.onlyGoodAt(mon_id=Tetranadon.id,element='water')
Ailments.createStatus(mon_id= Tetranadon.id, status="", blight="Water Blight", natural="Tremors")

games.inMHGen5(mon_id=Tetranadon.id,MHWI=False,MHRS=True)
