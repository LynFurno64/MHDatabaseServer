# Create Monsters from the Fanged Wyvern Phylum
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Egames


################## Zinogre ##################
addWeakness = Weakness()

Zinogre =Monster(name='Zinogre',generation=3,group="fanged",variation=1)
Zinogre.create(Zinogre)

Item_weak.applyItemWeakness(mon_id=Zinogre.id,shock_trap=False,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Zinogre.id,fire=False,water=True,thunder=False,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Zinogre.id)
Weakpoints.createWeakPoints(mon_id=Zinogre.id,cut='Head, Body, Back, Forearms(Shell), Forearms,Back Legs(shell), Back Legs, Tail,Tail End',impact='Head, Body, Back, Forearms(Shell), Forearms,Back Legs(shell), Back Legs, Tail,Tail End',projectile='Head, Body, Back, Forearms(Shell), Forearms,Back Legs(shell), Back Legs, Tail,Tail End')

Proficiency.onlyGoodAt(mon_id=Zinogre.id,element='thunder')
Ailments.createStatus(mon_id=Zinogre.id,status='Paralysis',blight='Thunderblight',natural='')
Egames.putInGames(Zinogre.id,  ['MH3rd', 'MH3U', 'MH4U', 'MHGU', 'MHWI', 'MHRS'])


################## Stygian Zinogre ##################
addWeakness = Weakness()

Zinogre_Stygian = Monster(name='Stygian Zinogre',generation=3,group='fanged',variation=2)
Zinogre_Stygian.create(Zinogre_Stygian)

Item_weak.applyItemWeakness(mon_id=Zinogre_Stygian.id,shock_trap=False,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Zinogre_Stygian.id,fire=False,water=False,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Zinogre_Stygian.id)
Weakpoints.createWeakPoints(mon_id=Zinogre_Stygian.id,cut='Head, Body, Back, Forearms(Shell), Forearms,Back Legs(shell), Back Legs, Tail,Tail End',impact='Head, Body, Back, Forearms(Shell), Forearms,Back Legs(shell), Back Legs, Tail,Tail End',projectile='Head, Body, Back, Forearms(Shell), Forearms,Back Legs(shell), Back Legs, Tail,Tail End')

Proficiency.applyStrenghts(mon_id=Zinogre_Stygian.id,fire=False,water=False,thunder=True,ice=False,dragon=True)
Ailments.createStatus(mon_id=Zinogre_Stygian.id,status='Paralysis, Dracophage Erosion',blight='Dragonblight',natural='')
Egames.putInGames(Zinogre_Stygian.id,  ['MH3U', 'MH4U', 'MHGU', 'MHWI'])


Zinogre.family(Zinogre_Stygian)

################## Thunderlord Zinogre ##################
addWeakness = Weakness()

Zinogre_Thunderlord = Monster(name='Thunderlord Zinogre',generation=4,group='fanged',variation=5)
Zinogre_Thunderlord.create(Zinogre_Thunderlord)

Item_weak.applyItemWeakness(mon_id=Zinogre_Thunderlord.id,shock_trap=False,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Zinogre_Thunderlord.id,fire=False,water=False,thunder=False,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Zinogre_Thunderlord.id)
Weakpoints.createWeakPoints(mon_id=Zinogre_Thunderlord.id,cut='Head, Body, Back, Forearms(Shell), Forearms,Back Legs(shell), Back Legs, Tail,Tail End',impact='Head, Body, Back, Forearms(Shell), Forearms,Back Legs(shell), Back Legs, Tail,Tail End',projectile='Head, Body, Back, Forearms(Shell), Forearms,Back Legs(shell), Back Legs, Tail,Tail End')

Proficiency.onlyGoodAt(mon_id=Zinogre_Thunderlord.id,element='thunder')
Ailments.createStatus(mon_id=Zinogre_Thunderlord.id, status='Stun',blight='Thunderblight',natural='')
Egames.putInGames(Zinogre_Thunderlord.id,  ['MHGU'])

Zinogre.family(Zinogre_Thunderlord)
Zinogre_Stygian.family(Zinogre_Thunderlord)

################## Magnamalo ##################
addWeakness = Weakness()

Magnamalo = Monster(name='Magnamalo',generation=5,group='fanged',variation=1)
Magnamalo.create(Magnamalo)

Item_weak.applyItemWeakness(mon_id=Magnamalo.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Magnamalo.id,fire=False,water=True,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Magnamalo.id)
Weakpoints.createWeakPoints(mon_id=Magnamalo.id,cut='Head, Torso, Foreleg, Armblade,Back,Hind leg, Tail, Tailblade',impact='Head, Torso, Foreleg, Armblade,Back,Hind leg, Tail, Tailblade',projectile='Head, Torso, Foreleg, Armblade,Back,Hind leg, Tail, Tailblade')

Proficiency.noElement(mon_id=Magnamalo.id)
Ailments.createStatus(mon_id=Magnamalo.id,status='',blight='Hellfireblight',natural='')
Egames.putInGames(Magnamalo.id,  ['MHRS'])
