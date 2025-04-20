#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from pymongo import MongoClient

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7794002726:AAFybvggb5PBrv8wrNytsq7QNyboh43ee1U")
    API_ID = int(os.environ["API_ID", 27058143]
    API_HASH = os.environ["API_HASH", "c569ea4f5ade3fc70d2bb1fd162d9dc9"]
    AUTH_USERS = "8144269730"
    MONGO_URI = os.environ.get("MONGO_DB_URI", "your_mongo_db_uri")
    
