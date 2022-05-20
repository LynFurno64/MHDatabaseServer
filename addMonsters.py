from sqlalchemy import false, true
from app import app, db
from app.models import Monster, Item_weak, Weakness, Weakpoints, Proficiency, Ailments, Games

rathalos = Monster("Rathalos", 1, "flying", 1)
print(rathalos.id)
db.session.add(rathalos)
db.session.commit()


Item_weak.applyItemWeakness(rathalos.id, True, True, True, False)

rathian = Monster("Rathian", 1, "flying", 1)
rathalos.related(rathian)


rathalos_azure = Monster("Azure Rathalos", 1, "flying", 2)
rathian_pink = Monster("Pink Rathian", 1, "flying", 2)
rathalos.related(rathalos_azure)
rathian.related(rathian_pink)


rathalos_silver = Monster("Silver Rathalos", 1, "flying", 3)
rathian_gold = Monster("Gold Rathian", 1, "flying", 3)
rathalos.related(rathalos_silver)
rathian.related(rathian_gold)


rathalos_dreadking = Monster("Dreadking Rathalos", 4, "flying", 5)
rathian_dreadqueen = Monster("Dreadqueen Rathian", 4, "flying", 5)
rathalos.related(rathalos_dreadking)
rathian.related(rathian_dreadqueen)


ibushi = Monster("Ibushi", 5, "elder", 1)
narwa = Monster("Narwa", 5, "flying", 1)
narwa_allmother = Monster("Narwa Allmother", 5, "flying", 4)

narwa.related(ibushi)
narwa.related(narwa_allmother)