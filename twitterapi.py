# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import sys
sys.path.insert(0, '../passwords')

from twitter_api_credentials import *

password_loc = "../passwords/twitter.csv"

unpw = pd.read_csv(password_loc)


username = unpw['username'][0]
password = unpw['password'][0]

print(ACCESS_TOKEN)
