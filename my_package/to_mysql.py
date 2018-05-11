
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import pymysql
host = '192.168.89.38'
port = 3306
db = 'mq_admin'
user = 'test'
password = 'test'

def predict_save(df):

    engine = create_engine(str(r"mysql+pymysql://%s:" + '%s' + "@%s/%s?charset=utf8mb4") % (user, password, host, db))
    try:
        df.to_sql('behavior_predict',con=engine,if_exists='append',index=False)
    except Exception as e:
        print(e)


def numeric_save(df):

    engine = create_engine(str(r"mysql+pymysql://%s:" + '%s' + "@%s/%s?charset=utf8mb4") % (user, password, host, db))
    try:
        df.to_sql('user_numeric_data',con=engine,if_exists='append',index=False)
    except Exception as e:
        print(e)
