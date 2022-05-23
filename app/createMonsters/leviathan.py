# Create Monsters from the Leviathan Phylum
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games

################## Lagiacrus ##################
addWeakness = Weakness()
games = Games()

Lagiacrus = Monster(name='Lagiacrus',generation=3,group='water',variation=1)
Lagiacrus.create(Lagiacrus)

Item_weak.applyItemWeakness(mon_id=Lagiacrus.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Lagiacrus.id,fire=True,water=False,thunder=False,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Lagiacrus.id)
Weakpoints.createWeakPoints(mon_id=Lagiacrus.id,cut='Head, Neck, Back, Body, Tail, Foot',impact='Head, Neck, Back, Body, Tail, Foot',projectile='Head, Neck, Back, Body, Tail, Foot')

Proficiency.onlyGoodAt(mon_id=Lagiacrus.id,element='Thunder')
Ailments.createStatus(mon_id=Lagiacrus.id,status='',blight='Thunderblight, Waterblight(When underwater)',natural='')
games.inMHGen3(mon_id=Lagiacrus.id,MH3rd=False,MH3U=True)
games.inMHGen4(mon_id=Lagiacrus.id,MH4U=False,MHGU=True)


################## Ivory Lagiacrus ##################
addWeakness = Weakness()
games = Games()

Lagiacrus_Ivory = Monster(name='Ivory Lagiacrus',generation=3,group='water',variation=2)
Lagiacrus_Ivory.create(Lagiacrus_Ivory)

Item_weak.applyItemWeakness(mon_id=Lagiacrus_Ivory.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Lagiacrus_Ivory.id,fire=True,water=False,thunder=False,ice=False,dragon=True)
addWeakness.noWeaknessStatus(mon_id=Lagiacrus_Ivory.id)
Weakpoints.createWeakPoints(mon_id=Lagiacrus_Ivory.id,cut='Head, Neck, Back, Body, Tail, Foot',impact='Head, Neck, Back, Body, Tail, Foot',projectile='Head, Neck, Back, Body, Tail, Foot')

Proficiency.applyStrenghts(mon_id=Lagiacrus_Ivory.id,fire=False,water=True,thunder=True,ice=False,dragon=False)
Ailments.createStatus(mon_id=Lagiacrus_Ivory.id,status='',blight='Thunderblight, Waterblight',natural='')
games.inMHGen3(mon_id=Lagiacrus_Ivory.id,MH3rd=False,MH3U=True)

################## Abyssal Lagiacrus ##################
addWeakness = Weakness()
games = Games()

Lagiacrus_Abyssal = Monster(name='Abyssal Lagiacrus',generation=3,group='fanged',variation=3)
Lagiacrus_Abyssal.create(Lagiacrus_Abyssal)

Item_weak.applyItemWeakness(mon_id=Lagiacrus_Abyssal.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Lagiacrus_Abyssal.id,fire=False,water=False,thunder=False,ice=False,dragon=True)
addWeakness.noWeaknessStatus(mon_id=Lagiacrus_Abyssal.id)
Weakpoints.createWeakPoints(mon_id=Lagiacrus_Abyssal.id,cut='Head, Neck, Back, Body, Tail, Foot',impact='Head, Neck, Back, Body, Tail, Foot',projectile='Head, Neck, Back, Body, Tail, Foot')

Proficiency.onlyGoodAt(mon_id=Lagiacrus_Abyssal.id,element='Thunder')
Ailments.createStatus(mon_id=Lagiacrus_Abyssal.id,status='',blight='Thunderblight, Waterblight',natural='')
games.inMHGen3(mon_id=Lagiacrus_Abyssal.id,MH3rd=False,MH3U=True)

##################  Agnaktor ##################
addWeakness = Weakness()
games = Games()

Agnaktor = Monster(name='Agnaktor',generation=3,group='fanged',variation=1)
Agnaktor.create(Agnaktor)

Item_weak.applyItemWeakness(mon_id=Agnaktor.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Agnaktor.id,fire=False,water=True,thunder=False,ice=True,dragon=True)
addWeakness.noWeaknessStatus(mon_id=Agnaktor.id)
Weakpoints.createWeakPoints(mon_id=Agnaktor.id,cut='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail',impact='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail',projectile='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail')

Proficiency.onlyGoodAt(mon_id=Agnaktor.id,element='fire')
Ailments.createStatus(mon_id=Agnaktor.id,status='',blight='Fireblight',natural='')
games.inMHGen3(mon_id=Agnaktor.id,MH3rd=True,MH3U=True)
games.inMHGen4(mon_id=Agnaktor.id,MH4U=False,MHGU=True)

################## Glacial Agnaktor ##################
addWeakness = Weakness()
games = Games()

Agnaktor_Glacial = Monster(name='Glacial Agnaktor',generation=3,group='fanged',variation=2)
Agnaktor_Glacial.create(Agnaktor_Glacial)

Item_weak.applyItemWeakness(mon_id=Agnaktor_Glacial.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Agnaktor_Glacial.id,fire=True,water=False,thunder=False,ice=False,dragon=True)
addWeakness.noWeaknessStatus(mon_id=Agnaktor_Glacial.id)
Weakpoints.createWeakPoints(mon_id=Agnaktor_Glacial.id,cut='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail',impact='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail',projectile='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail')

Proficiency.applyStrenghts(mon_id=Agnaktor_Glacial.id,fire=False,water=True,thunder=False,ice=True,dragon=False)
Ailments.createStatus(mon_id=Agnaktor_Glacial.id,status='',blight='Iceblight, Waterblight',natural='')
games.inMHGen3(mon_id=Agnaktor_Glacial.id,MH3rd=True,MH3U=True)