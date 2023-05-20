import os
from unittest import TestCase
from app import app, db
from models import db, connect_db, User, Message

from app import app, CURR_USER_KEY

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

class ViewTestCase(TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()

    def test_see_followers(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = self.testuser.id

        resp = c.get("/users/{user.id}/followers")

        self.assertEqual(resp.status_code, 200)


    def test_logout_posts(self):

        with self.client as c:

            resp = c.get("/users/{user.id}/followers")

        self.assertEqual(resp.status_code, 302)


    def tearDown(self):
        db.rollback()
