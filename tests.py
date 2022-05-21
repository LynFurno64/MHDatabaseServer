#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import Monster, Weakness


class MonsterModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_weakness(self):
        er1 = Monster(name='los', generation=1, phylum='bug', variation=1)
        we = Weakness()
        
        self.assertFalse(Weakness.applyWeaknessElement(mon_id=er1.id, fire=False, water=False, thunder=True, ice=False, dragon=True))
        self.assertFalse(Weakness.applyWeaknessStatus(mon_id= er1.id, poison=False, sleep=True, para=False, blast=False))

    
    def test_family(self):
        er1 = Monster(name='los', generation=1, phylum='bug', variation=1)
        er2 = Monster(name='ian', generation=2, phylum='bug', variation=2)
        
        db.session.add(er1)
        db.session.add(er2)
        db.session.commit()
        self.assertEqual(er1.relative.all(), [])
        self.assertEqual(er1.familia.all(), [])

        er1.family(er2)
        db.session.commit()
        self.assertTrue(er1.is_family(er2))
        self.assertEqual(er1.relative.count(), 1)
        self.assertEqual(er1.relative.first().name, 'ian')
        self.assertEqual(er2.familia.count(), 1)
        self.assertEqual(er2.familia.first().name, 'los')

        

    def test_follow_posts(self):

        # create four mons
        er1 = Monster(name='1', generation=1, phylum='bug', variation=1)
        er2 = Monster(name='2', generation=2, phylum='bug', variation=2)
        er3 = Monster(name='3', generation=3, phylum='brute', variation=3)
        er4 = Monster(name='4', generation=4, phylum='fish', variation=4)
        er5 = Monster(name='5', generation=5, phylum='elder', variation=5)
        db.session.add_all([er1, er2, er3, er4])
        db.session.commit()

        # setup the followers
        er1.family(er2)
        er3.family(er4)
        er4.family(er5)
        er5.family(er1)
        db.session.commit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

