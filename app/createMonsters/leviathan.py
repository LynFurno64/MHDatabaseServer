# Create Monsters from the Leviathan Phylum
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Egames

################## Lagiacrus ##################
addWeakness = Weakness()

Lagiacrus = Monster(name='Lagiacrus',generation=3,group='water',variation=1)
Lagiacrus.create(Lagiacrus)

Item_weak.applyItemWeakness(mon_id=Lagiacrus.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Lagiacrus.id,fire=True,water=False,thunder=False,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Lagiacrus.id)
Weakpoints.createWeakPoints(mon_id=Lagiacrus.id,cut='Head, Neck, Back, Body, Tail, Foot',impact='Head, Neck, Back, Body, Tail, Foot',projectile='Head, Neck, Back, Body, Tail, Foot')

Proficiency.onlyGoodAt(mon_id=Lagiacrus.id,element='thunder')
Ailments.createStatus(mon_id=Lagiacrus.id,status='',blight='Thunderblight, Waterblight(When underwater)',natural='')

Egames.putInGames(Lagiacrus.id,  ['MH3U', 'MHGU'])



################## Ivory Lagiacrus ##################
addWeakness = Weakness()

Lagiacrus_Ivory = Monster(name='Ivory Lagiacrus',generation=3,group='water',variation=2)
Lagiacrus_Ivory.create(Lagiacrus_Ivory)

Item_weak.applyItemWeakness(mon_id=Lagiacrus_Ivory.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Lagiacrus_Ivory.id,fire=True,water=False,thunder=False,ice=False,dragon=True)
addWeakness.noWeaknessStatus(mon_id=Lagiacrus_Ivory.id)
Weakpoints.createWeakPoints(mon_id=Lagiacrus_Ivory.id,cut='Head, Neck, Back, Body, Tail, Foot',impact='Head, Neck, Back, Body, Tail, Foot',projectile='Head, Neck, Back, Body, Tail, Foot')

Proficiency.applyStrenghts(mon_id=Lagiacrus_Ivory.id,fire=False,water=True,thunder=True,ice=False,dragon=False)
Ailments.createStatus(mon_id=Lagiacrus_Ivory.id,status='',blight='Thunderblight, Waterblight',natural='')
Egames.putInGames(Lagiacrus_Ivory.id,  ['MH3U'])

Lagiacrus.family(Lagiacrus_Ivory)

################## Abyssal Lagiacrus ##################
addWeakness = Weakness()

Lagiacrus_Abyssal = Monster(name='Abyssal Lagiacrus',generation=3,group='water',variation=3)
Lagiacrus_Abyssal.create(Lagiacrus_Abyssal)

Item_weak.applyItemWeakness(mon_id=Lagiacrus_Abyssal.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Lagiacrus_Abyssal.id,fire=False,water=False,thunder=False,ice=False,dragon=True)
addWeakness.noWeaknessStatus(mon_id=Lagiacrus_Abyssal.id)
Weakpoints.createWeakPoints(mon_id=Lagiacrus_Abyssal.id,cut='Head, Neck, Back, Body, Tail, Foot',impact='Head, Neck, Back, Body, Tail, Foot',projectile='Head, Neck, Back, Body, Tail, Foot')

Proficiency.onlyGoodAt(mon_id=Lagiacrus_Abyssal.id,element='thunder')
Ailments.createStatus(mon_id=Lagiacrus_Abyssal.id,status='',blight='Thunderblight, Waterblight',natural='')
Egames.putInGames(Lagiacrus_Abyssal.id,  ['MH3U'])

Lagiacrus.family(Lagiacrus_Abyssal)
Lagiacrus_Ivory.family(Lagiacrus_Abyssal)

##################  Agnaktor ##################
addWeakness = Weakness()

Agnaktor = Monster(name='Agnaktor',generation=3,group='water',variation=1)
Agnaktor.create(Agnaktor)

Item_weak.applyItemWeakness(mon_id=Agnaktor.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Agnaktor.id,fire=False,water=True,thunder=False,ice=True,dragon=True)
addWeakness.noWeaknessStatus(mon_id=Agnaktor.id)
Weakpoints.createWeakPoints(mon_id=Agnaktor.id,cut='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail',impact='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail',projectile='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail')

Proficiency.onlyGoodAt(mon_id=Agnaktor.id,element='fire')
Ailments.createStatus(mon_id=Agnaktor.id,status='',blight='Fireblight',natural='Roar(L)')

Egames.putInGames(Agnaktor.id,  ['MH3rd', 'MH3U', 'MHGU'])


################## Glacial Agnaktor ##################
addWeakness = Weakness()

Agnaktor_Glacial = Monster(name='Glacial Agnaktor',generation=3,group='water',variation=2)
Agnaktor_Glacial.create(Agnaktor_Glacial)

Item_weak.applyItemWeakness(mon_id=Agnaktor_Glacial.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Agnaktor_Glacial.id,fire=True,water=False,thunder=False,ice=False,dragon=True)
addWeakness.noWeaknessStatus(mon_id=Agnaktor_Glacial.id)
Weakpoints.createWeakPoints(mon_id=Agnaktor_Glacial.id,cut='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail',impact='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail',projectile='Head, Neck, Chest, Body, Front Legs, Back Legs, Fin, Tail')

Proficiency.applyStrenghts(mon_id=Agnaktor_Glacial.id,fire=False,water=True,thunder=False,ice=True,dragon=False)
Ailments.createStatus(mon_id=Agnaktor_Glacial.id,status='',blight='Iceblight, Waterblight',natural='Roar(L)')
Egames.putInGames(Agnaktor_Glacial.id,  ['MH3U'])


Agnaktor.family(Agnaktor_Glacial)
