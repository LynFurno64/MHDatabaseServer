# Create Monsters from the Fanged Beast group
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games


##################  Arzuros ##################
addWeakness = Weakness()
games = Games()

Arzuros =Monster(name='Arzuros',generation=3,group='beast',variation=1)
Arzuros.create(Arzuros)

Item_weak.applyItemWeakness(mon_id=Arzuros.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Arzuros.id,fire=True,water=False,thunder=True,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Arzuros.id)
Weakpoints.createWeakPoints(mon_id=Arzuros.id,cut='Head, Upper Half, Forelegs, Hind Legs, Rear',impact='Head, Upper Half, Foreleg, Hind Leg, Rear',projectile='Head, Upper Half, Foreleg, Hind Leg, Rear')

Proficiency.noElement(mon_id=Arzuros.id)
Ailments.createStatus(mon_id= Arzuros.id, status="", blight="", natural="")

games.inMHGen3(mon_id=Arzuros.id,MH3rd=True,MH3U=True)
games.inMHGen4(mon_id=Arzuros.id,MH4U=False,MHGU=True)
games.inMHGen5(mon_id=Arzuros.id,MHWI=False,MHRS=True)


##################  Redhelm Arzuro ##################
addWeakness = Weakness()
games = Games()

Arzuros_Redhelm = Monster(name='Redhelm Arzuros',generation=4,group='beast',variation=5)
Arzuros_Redhelm.create(Arzuros_Redhelm)

Item_weak.applyItemWeakness(mon_id=Arzuros_Redhelm.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Arzuros_Redhelm.id,fire=True,water=False,thunder=False,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Arzuros_Redhelm.id)
Weakpoints.createWeakPoints(mon_id=Arzuros_Redhelm.id,cut='Head, Upper Half, Forelegs, Hind Legs, Rear',impact='Head, Upper Half, Foreleg, Hind Leg, Rear',projectile='Head, Upper Half, Foreleg, Hind Leg, Rear')

Proficiency.noElement(mon_id=Arzuros_Redhelm.id)
Ailments.createStatus(mon_id= Arzuros_Redhelm.id, status="", blight="", natural="Wind Pressure (s), Roar (s), Tremor")

games.inMHGen4(mon_id=Arzuros_Redhelm.id,MH4U=False,MHGU=True)

Arzuros.family(Arzuros_Redhelm)

##################  Gammoth ##################
addWeakness = Weakness()
games = Games()

Gammoth = Monster(name='Gammoth',generation=4,group='beast',variation=1)
Gammoth.create(Gammoth)

Item_weak.applyItemWeakness(mon_id=Gammoth.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Gammoth.id,fire=True,water=False,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Gammoth.id)
Weakpoints.createWeakPoints(mon_id=Gammoth.id,cut='Head, Trunk, Forelegs, Hind legs',impact='Head, Trunk, Forelegs, Hind legs',projectile='Head, Trunk, Forelegs, Hind legs')

Proficiency.onlyGoodAt(mon_id=Gammoth.id,element='ice')
Ailments.createStatus(mon_id= Gammoth.id, status="", blight="Ice blight", natural="Wind pressure, Roar (small), Snowman, Tremor")

games.inMHGen4(mon_id=Gammoth.id,MH4U=False,MHGU=True)

##################  Elderfrost Gammoth ##################
addWeakness = Weakness()
games = Games()

Gammoth_Elderfrost = Monster(name='Elderfrost Gammoth',generation=4,group='beast',variation=5)
Gammoth_Elderfrost.create(Gammoth_Elderfrost)

Item_weak.applyItemWeakness(mon_id=Gammoth_Elderfrost.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Gammoth_Elderfrost.id,fire=True,water=False,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Gammoth_Elderfrost.id)
Weakpoints.createWeakPoints(mon_id=Gammoth_Elderfrost.id,cut='Head, Trunk, Forelegs, Hind legs',impact='Head, Trunk, Forelegs, Hind legs',projectile='Head, Trunk, Forelegs, Hind legs')

Proficiency.onlyGoodAt(mon_id=Gammoth_Elderfrost.id,element='ice')
Ailments.createStatus(mon_id= Gammoth_Elderfrost.id, status="", blight="Ice blight", natural="Wind pressure, Roar (small), Snowman, Tremor")

games.inMHGen4(mon_id=Gammoth_Elderfrost.id,MH4U=False,MHGU=True)

Gammoth.family(Gammoth_Elderfrost)

##################  Goss Harag ##################
addWeakness = Weakness()
games = Games()

Goss_Harag = Monster(name='Goss Harag',generation=5,group='beast',variation=1)
Goss_Harag.create(Goss_Harag)

Item_weak.applyItemWeakness(mon_id=Goss_Harag.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Goss_Harag.id,fire=True,water=False,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Goss_Harag.id)
Weakpoints.createWeakPoints(mon_id=Goss_Harag.id,cut='Head, Torso, Forelegs, Ice Clump, Back, Hind Legs',impact='Head, Torso, Forelegs, Ice Clump, Back, Hind Legs',projectile='Head, Torso, Forelegs, Ice Clump, Back, Hind Legs')

Proficiency.onlyGoodAt(mon_id=Goss_Harag.id,element='ice')
Ailments.createStatus(mon_id= Goss_Harag.id, status="", blight="Ice blight", natural="Roar (small)")

games.inMHGen5(mon_id=Goss_Harag.id,MHWI=False,MHRS=True)