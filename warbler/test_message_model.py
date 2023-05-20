import os
from unittest import TestCase
from app import app, db
from models import db, connect_db, User, Message

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

class UserModelTestCase(TestCase):
    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_repr(self):
        user = User(id=1, username='testguy', email='testguy@google.com')
        result = repr(user)

        self.assertEqual(result, "<User #1: testguy, testguy@google.com>")


    def test_is_following(self):
        user1 = User(username='testguy', email='testguy@google.com', password='finsta')
        user2 = User(username='testgirl', email='testgirl@google.com', password='finsta2')

        db.session.add(user1, user2)
        user1.following.append(user2)
        db.session.commit()

        self.assertTrue(user1.is_following(user2))

        self.assertFalse(user2.is_following(user1))

    def tearDown(self):
        db.session.rollback()
