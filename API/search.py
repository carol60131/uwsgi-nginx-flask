# -*- coding: UTF8 -*-
from functions import *
from datetime import datetime as dt
import pandas as pd
import time
import os


def main():
	db = MySQLdb('netsms_global', 'pigsms_train')
	engine = db.getEngine()

	sql = '''
		SELECT *
		FROM pigsms_train
		WHERE 1=1
		limit 100
	'''

	# db.execSQL(sql)

	tp = pd.read_sql(sql=sql, con=engine, chunksize=10000)
	df = pd.concat(tp)
	print(df)

	return df

if __name__ == '__main__':
	tStart = time.time()
	print('\n======== ' + os.path.basename(__file__) + ' ========')
	print('Exec Datetime: ' + dt.now().strftime('%Y-%m-%d, %H:%M:%S'))
	print('Server: ' + get_ownIP())
	print('Path: ' + os.path.dirname(os.path.abspath(__file__)))
	main()
	spendS = time.time() - tStart
	spendM = spendS / 60
	print('Total ' + str(round(spendS)) + ' sec, Like ' + str(round(spendM)) + ' min.')
