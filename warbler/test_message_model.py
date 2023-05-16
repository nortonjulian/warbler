import os
from unittest import TestCase
from app import app, db
from models import db, connect_db, User, Message

class MessaegModelTestCase(TestCase):
    
