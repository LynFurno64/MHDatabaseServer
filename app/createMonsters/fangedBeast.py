# Create Monsters from the Fanged Beast Phylum
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games


##################  Arzuros ##################
addWeakness = Weakness()
games = Games()

Arzuros =Monster(name='Arzuros',generation=3,phylum='beast',variation=1)
Arzuros.create(Arzuros)

Item_weak.applyItemWeakness(mon_id=Arzuros.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Arzuros.id,fire=True,water=False,thunder=True,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Arzuros.id)
Weakpoints.createWeakPoints(mon_id=Arzuros.id,cut='Head, Upper Half, Forelegs, Hind Legs, Rear',impact='Head, Upper Half, Foreleg, Hind Leg, Rear',projectile='Head, Upper Half, Foreleg, Hind Leg, Rear')

Proficiency.noElement(mon_id=Arzuros.id)
Ailments.createStatus(mon_id=Arzuros.id,poison=False,sleep=False,para=False,blast=False,stun=False,tremor=False,roar=False,wind=False)
games.inMHGen3(mon_id=Arzuros.id,MH3rd=True,MH3U=True)


##################  Redhelm Arzuro ##################
addWeakness = Weakness()
games = Games()

Arzuros_Redhelm = Monster(name='Arzuros Redhelm',generation=4,phylum='beast',variation=2)
Arzuros_Redhelm.create(Arzuros_Redhelm)

Item_weak.applyItemWeakness(mon_id=Arzuros_Redhelm.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=True)
addWeakness.applyWeaknessElement(mon_id=Arzuros_Redhelm.id,fire=True,water=False,thunder=False,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Arzuros_Redhelm.id)
Weakpoints.createWeakPoints(mon_id=Arzuros_Redhelm.id,cut='Head, Upper Half, Forelegs, Hind Legs, Rear',impact='Head, Upper Half, Foreleg, Hind Leg, Rear',projectile='Head, Upper Half, Foreleg, Hind Leg, Rear')

Proficiency.noElement(mon_id=Arzuros_Redhelm.id)
Ailments.createStatus(mon_id=Arzuros_Redhelm.id,poison=False,sleep=False,para=False,blast=False,stun=True,tremor=False,roar=False,wind=False)
games.inMHGen4(mon_id=Arzuros_Redhelm.id,MH4U=False,MHGU=True)


##################  Gammoth ##################
addWeakness = Weakness()
games = Games()

Gammoth = Monster(name='Gammoth',generation=4,phylum='beast',variation=1)
Gammoth.create(Gammoth)

Item_weak.applyItemWeakness(mon_id=Gammoth.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Gammoth.id,fire=True,water=False,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Gammoth.id)
Weakpoints.createWeakPoints(mon_id=Gammoth.id,cut='Head, Trunk, Forelegs, Hind legs',impact='Head, Trunk, Forelegs, Hind legs',projectile='Head, Trunk, Forelegs, Hind legs')

Proficiency.onlyGoodAt(mon_id=Gammoth.id,element='ice')
Ailments.createStatus(mon_id=Gammoth.id,poison=False,sleep=False,para=False,blast=False,stun=False,tremor=True,roar=True,wind=False)
games.inMHGen4(mon_id=Gammoth.id,MH4U=False,MHGU=True)

##################  Elderfrost Gammoth ##################
addWeakness = Weakness()
games = Games()

Gammoth_Elderfrost = Monster(name='Gammoth Elderfrost',generation=4,phylum='beast',variation=2)
Gammoth_Elderfrost.create(Gammoth_Elderfrost)

Item_weak.applyItemWeakness(mon_id=Gammoth_Elderfrost.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Gammoth_Elderfrost.id,fire=True,water=False,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Gammoth_Elderfrost)
Weakpoints.createWeakPoints(mon_id=Gammoth_Elderfrost.id,cut='Head, Trunk, Forelegs, Hind legs',impact='Head, Trunk, Forelegs, Hind legs',projectile='Head, Trunk, Forelegs, Hind legs')

Proficiency.onlyGoodAt(mon_id=Gammoth_Elderfrost.id,element='ice')
Ailments.createStatus(mon_id=Gammoth_Elderfrost.id,poison=False,sleep=False,para=False,blast=False,stun=False,tremor=True,roar=True,wind=False)
games.inMHGen4(mon_id=Gammoth_Elderfrost.id,MH4U=False,MHGU=True)


##################  Goss Harag ##################
addWeakness = Weakness()
games = Games()

Goss_Harag = Monster(name='Goss Harag',generation=5,phylum='beast',variation=1)
Goss_Harag.create(Goss_Harag)

Item_weak.applyItemWeakness(mon_id=Goss_Harag.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Goss_Harag.id,fire=True,water=False,thunder=True,ice=False,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Goss_Harag)
Weakpoints.createWeakPoints(mon_id=Goss_Harag.id,cut='Head, Torso, Forelegs, Ice Clump, Back, Hind Legs',impact='Head, Torso, Forelegs, Ice Clump, Back, Hind Legs',projectile='Head, Torso, Forelegs, Ice Clump, Back, Hind Legs')

Proficiency.onlyGoodAt(mon_id=Goss_Harag.id,element='ice')
Ailments.createStatus(mon_id=Goss_Harag.id,poison=False,sleep=False,para=False,blast=False,stun=False,tremor=False,roar=False,wind=False)
games.inMHGen5(mon_id=Goss_Harag.id,MHWI=False,MHRS=True)