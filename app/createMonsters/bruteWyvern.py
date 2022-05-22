# Create Monsters from the Brute Wyvern Phylum
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games

################## Brachydios ##################
addWeakness = Weakness()
games = Games()

Brachydios = Monster(name='Brachydios', generation=3, phylum='brute', variation=1)
Brachydios.create(Brachydios)

Item_weak.applyItemWeakness(mon_id= Brachydios.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.onlyWeakElement(mon_id= Brachydios.id, element='water')
addWeakness.onlyWeakStatus(mon_id= Brachydios.id, status='poison')
Weakpoints.createWeakPoints(mon_id= Brachydios.id, cut='Head, Front Legs', impact='Head, Front Legs', projectile='Head, Tail')

Proficiency.noElement(Brachydios.id)
Ailments.createStatus(mon_id= Brachydios.id, poison=False, sleep=False, para=False, blast=True, stun=False, tremor=True, roar=True, wind=False)
games.inMHGen3(mon_id= Brachydios.id, MH3rd=False, MH3U=True)
games.inMHGen4(mon_id= Brachydios.id, MH4U=True, MHGU=True)
games.inMHGen5(mon_id= Brachydios.id, MHWI=True, MHRS=False)

################## Raging Brachydios ##################
addWeakness = Weakness()
games = Games()

Brachydios_Raging = Monster(name='Raging Brachydios', generation=4, phylum='brute', variation=4)
Brachydios_Raging.create(Brachydios_Raging)

Item_weak.applyItemWeakness(mon_id= Brachydios_Raging.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= Brachydios_Raging.id, fire=False, water=True, thunder=False, ice=True, dragon=False)
addWeakness.onlyWeakStatus(mon_id= Brachydios_Raging.id, status='poison')
Weakpoints.createWeakPoints(mon_id= Brachydios_Raging.id, cut='Head, Head(Red), Forearms, Forearms(Red), Tail, Tail(Red)', 
impact='Head, Head(Red), Forearms, Forearms(Red), Tail, Tail(Red)', projectile='Head, Forearms, Tail')

Proficiency.noElement(Brachydios_Raging.id)
Ailments.createStatus(mon_id= Brachydios_Raging.id, poison=False, sleep=False, para=False, blast=True, stun=False, tremor=True, roar=True, wind=False)
games.inMHGen4(mon_id= Brachydios_Raging.id, MH4U=True, MHGU=True)
games.inMHGen5(mon_id= Brachydios_Raging.id, MHWI=True, MHRS=False)


##################  Glavenus ##################
addWeakness = Weakness()
games = Games()

Glavenus= Monster(name='Glavenus', generation=4, phylum='brute', variation=1)
Glavenus.create(Glavenus)

Item_weak.applyItemWeakness(mon_id= Glavenus.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.onlyWeakElement(mon_id= Glavenus.id, element='water')
addWeakness.onlyWeakStatus(mon_id= Glavenus.id, status='poison')
Weakpoints.createWeakPoints(mon_id= Glavenus.id, cut='Head, Throat, Tail(Heated)', impact='Head, Throat, Tail(Heated)', 
projectile='Head, Horns, Tail(Heated)')

Proficiency.onlyGoodAt(mon_id= Glavenus.id, element='fire')
Ailments.createStatus(mon_id= Glavenus.id, poison=False, sleep=False, para=False, blast=True, stun=False, tremor=False, roar=True, wind=False)
games.inMHGen4(mon_id= Glavenus.id, MH4U=False, MHGU=True)
games.inMHGen5(Glavenus.id, True, False)


################## Acidic Glavenus ##################
addWeakness = Weakness()
games = Games()

addWeakness = Weakness()
games = Games()

Glavenus_Acidic= Monster(name='Acidic Glavenus', generation=5, phylum='brute', variation=2)
Glavenus_Acidic.create(Glavenus_Acidic)

Item_weak.applyItemWeakness(mon_id= Glavenus_Acidic.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.onlyWeakElement(mon_id= Glavenus_Acidic.id, element='fire')
addWeakness.noWeaknessStatus(mon_id= Glavenus_Acidic.id)
Weakpoints.createWeakPoints(mon_id= Glavenus_Acidic.id, cut='Throat, Back, Tail(Sharpened)', impact='Head, Throat, Back, Tail(Sharpened)', 
projectile='Head, Throat, Tail(Sharpened)')

Proficiency.noElement(Glavenus_Acidic.id)
Ailments.createStatus(mon_id= Glavenus_Acidic.id, poison=False, sleep=False, para=False, blast=False, stun=False, tremor=False, roar=True, wind=False)
games.inMHGen5(mon_id= Glavenus_Acidic.id, MHWI=True, MHRS=False)

################## Hellblade Glavenus ##################
addWeakness = Weakness()
games = Games()

Glavenus_Hellblade= Monster(name='Hellblade Glavenus', generation=4, phylum='brute', variation=5)
Glavenus_Hellblade.create(Glavenus_Hellblade)

Item_weak.applyItemWeakness(mon_id= Glavenus_Hellblade.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= Glavenus_Hellblade.id, fire=False, water=True, thunder=False, ice=True, dragon=False)
addWeakness.onlyWeakStatus(mon_id= Glavenus_Hellblade.id, status='poison')
Weakpoints.createWeakPoints(mon_id= Glavenus_Hellblade.id, cut='Head, Throat, Tail [Normal/Heated]', impact='Head, Throat, Tail [Normal/Heated]', 
projectile='Throat, Horns(Normal/Heated)')

Proficiency.onlyGoodAt(mon_id= Glavenus_Hellblade.id, element='fire')
Ailments.createStatus(mon_id= Glavenus_Hellblade.id, poison=False, sleep=False, para=False, blast=True, stun=False, tremor=False, roar=True, wind=True)
games.inMHGen4(mon_id= Glavenus_Hellblade.id, MH4U=False, MHGU=True)


################## Anjanath ##################
addWeakness = Weakness()
games = Games()

Anjanath= Monster(name='Anjanath', generation=5, phylum='brute', variation=1)
Anjanath.create(Anjanath)

Item_weak.applyItemWeakness(mon_id= Anjanath.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.onlyWeakElement(mon_id= Anjanath.id, element='water')
addWeakness.noWeaknessStatus(Anjanath.id)
Weakpoints.createWeakPoints(mon_id= Anjanath.id, cut='Nose, Head, Wings, Legs, Tail', impact='Nose, Head, Wings, Legs, Tail', projectile='Nose, Head, Body, Wings, Legs, Tail')

Proficiency.onlyGoodAt(Anjanath.id, 'fire')
Ailments.createStatus(mon_id= Anjanath.id, poison=False, sleep=False, para=False, blast=False, stun=False, tremor=True, roar=True, wind=True)
games.inMHGen5(Anjanath.id, True, True)

################## Fulgur Anjanath ##################
addWeakness = Weakness()
games = Games()

Anjanath_Fulgur= Monster(name='Fulgur Anjanath', generation=5, phylum='brute', variation=2)
Anjanath_Fulgur.create(Anjanath_Fulgur)

Item_weak.applyItemWeakness(mon_id= Anjanath_Fulgur.id, shock_trap=True, pitfall_trap=True, flash_bomb=True, sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id= Anjanath_Fulgur.id, fire=False, water=True, thunder=False, ice=True, dragon=False)
addWeakness.noWeaknessStatus(Anjanath_Fulgur.id)
Weakpoints.createWeakPoints(mon_id= Anjanath_Fulgur.id, cut='Nose, Head, Wings, Legs, Tail', impact='Nose, Head, Wings, Legs, Tail', projectile='Nose, Head, Body, Wings, Legs, Tail')

Proficiency.onlyGoodAt(Anjanath_Fulgur.id, 'thunder')
Ailments.createStatus(mon_id= Anjanath_Fulgur.id, poison=False, sleep=False, para=True, blast=False, stun=False, tremor=False, roar=True, wind=False)
games.inMHGen5(Anjanath_Fulgur.id, True, False)


Brachydios.family(Brachydios_Raging)
Glavenus.family(Glavenus_Acidic)
Glavenus.family(Glavenus_Hellblade)
Glavenus_Acidic.family(Glavenus_Hellblade)
Anjanath.family(Anjanath_Fulgur)