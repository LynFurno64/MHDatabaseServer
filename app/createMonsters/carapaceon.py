# Create Monsters from the Carapaceon Phylum
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games


##################  Shogun Ceanataur ##################
addWeakness = Weakness()
games = Games()

Shogun_Ceanataur = Monster(name='Shogun Ceanataur',generation=2,group='crab',variation=1)
Shogun_Ceanataur.create(Shogun_Ceanataur)

Item_weak.applyItemWeakness(mon_id=Shogun_Ceanataur.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Shogun_Ceanataur.id,fire=False,water=False,thunder=True,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Shogun_Ceanataur.id)
Weakpoints.createWeakPoints(mon_id=Shogun_Ceanataur.id,cut='Shell, Right Claw, Left Claw',impact='Shell, Right Claw, Left Claw',projectile='Shell, Right Claw, Left Claw')

Proficiency.onlyGoodAt(mon_id=Shogun_Ceanataur.id,element='water')
Ailments.createStatus(mon_id=Shogun_Ceanataur.id,status='poison, Bleeding',blight='Waterblight',natural='Stabbed')
games.inMHOld(mon_id=Shogun_Ceanataur.id,MHF=True,MHF2=True)
games.inMHGen4(mon_id=Shogun_Ceanataur.id,MH4U=False,MHGU=True)
games.inMHGen5(mon_id=Shogun_Ceanataur.id,MHWI=False,MHRS=True)


##################  Terra Shogun Ceanataur ##################
addWeakness = Weakness()
games = Games()

Shogun_Ceanataur_Terra = Monster(name='Terra Shogun Ceanataur',generation=2,group='crab',variation=2)
Shogun_Ceanataur_Terra.create(Shogun_Ceanataur_Terra)

Item_weak.applyItemWeakness(mon_id=Shogun_Ceanataur_Terra.id, shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Shogun_Ceanataur_Terra.id,fire=False,water=False,thunder=True,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Shogun_Ceanataur_Terra.id)
Weakpoints.createWeakPoints(mon_id=Shogun_Ceanataur_Terra.id,cut='Shell, Right Claw, Left Claw',impact='Shell, Right Claw, Left Claw',projectile='Shell, Right Claw, Left Claw')

Proficiency.onlyGoodAt(mon_id=Shogun_Ceanataur_Terra.id,element='water')
Ailments.createStatus(mon_id=Shogun_Ceanataur_Terra.id,status='',blight='',natural='')
games.inMHOld(mon_id=Shogun_Ceanataur_Terra.id,MHF=True,MHF2=False)

Shogun_Ceanataur.family(Shogun_Ceanataur_Terra)

##################  Rustrazor Ceanataur ##################
addWeakness = Weakness()
games = Games()

Rustrazor_Ceanataur = Monster(name='Rustrazor Ceanataur',generation=4,group='crab',variation=5)
Rustrazor_Ceanataur.create(Rustrazor_Ceanataur)

Item_weak.applyItemWeakness(mon_id=Rustrazor_Ceanataur.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Rustrazor_Ceanataur.id,fire=False,water=False,thunder=True,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Rustrazor_Ceanataur.id)
Weakpoints.createWeakPoints(mon_id=Rustrazor_Ceanataur.id,cut='Shell, Right Claw, Left Claw',impact='Shell, Right Claw, Left Claw',projectile='Shell, Right Claw, Left Claw')

Proficiency.onlyGoodAt(mon_id=Rustrazor_Ceanataur.id,element='water')
Ailments.createStatus(mon_id=Rustrazor_Ceanataur.id, status='Bleeding, Defense Down',blight='Waterblight',natural='')
games.inMHGen4(mon_id=Rustrazor_Ceanataur.id,MH4U=False,MHGU=True)

Shogun_Ceanataur.family(Rustrazor_Ceanataur)
Shogun_Ceanataur_Terra.family(Rustrazor_Ceanataur)

##################  Daimyo Hermitaur ##################
addWeakness = Weakness()
games = Games()

Hermitaur_Daimyo = Monster(name='Daimyo Hermitaur',generation=4,group='crab',variation=1)
Hermitaur_Daimyo.create(Hermitaur_Daimyo)

Item_weak.applyItemWeakness(mon_id=Hermitaur_Daimyo.id,shock_trap=True,pitfall_trap=True,flash_bomb=True,sonic_bomb=False)
addWeakness.applyWeaknessElement(mon_id=Hermitaur_Daimyo.id,fire=False,water=False,thunder=True,ice=True,dragon=False)
addWeakness.noWeaknessStatus(mon_id=Hermitaur_Daimyo.id)
Weakpoints.createWeakPoints(mon_id=Hermitaur_Daimyo.id,cut='Shell, Right Claw, Left Claw',impact='Shell, Right Claw, Left Claw',projectile='Shell, Right Claw, Left Claw')

Proficiency.onlyGoodAt(mon_id=Hermitaur_Daimyo.id,element='water')
Ailments.createStatus(mon_id=Hermitaur_Daimyo.id, status='Poison',blight='Waterblight',natural='')
games.inMHGen4(mon_id=Hermitaur_Daimyo.id,MH4U=False,MHGU=True)