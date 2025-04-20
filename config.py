#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from pymongo import MongoClient

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7221760137:AAGvD4ICBuaFufzjsl2woOlHOotxQLlM5xU")
    API_ID = int(os.environ["API_ID", 15958423]
    API_HASH = os.environ["API_HASH", "0f38f0c37cec744bccb074b5180e37b0"]
    AUTH_USERS = "5128979564"
    MONGO_URI = os.environ.get("MONGO_DB_URI", "your_mongo_db_uri")
    
