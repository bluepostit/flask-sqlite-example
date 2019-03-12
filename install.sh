#!/usr/bin/bash

virtualenv env
source env/bin/activate
pip3 install flask
# Uncomment if you have the sqlite3 binary installed:
# sqlite3 data/db.sqlite3 < data/init.sql