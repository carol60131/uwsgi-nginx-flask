# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from pymysql.constants.CLIENT import MULTI_STATEMENTS
import socket

db_info = {
	'netsms_global': 'root:@8606#2736@52.58.8.182/netsms_global'
}


class MySQLdb():
	def __init__(self, db, tb):
		self.db = db
		self.tb = tb
		self.db_str = 'mysql+pymysql://' + db_info[db] + '?charset=utf8mb4'
		self.db = create_engine(self.db_str)

	def getEngine(self):
		return self.db

	def execSQL(self, sql):
		with self.db.connect() as con:
			con.execute(sql)

	def insertData(self, df):
		df.to_sql(con=self.db, name=self.tb,
			index=True, if_exists='append', chunksize=10000)


def get_ownIP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	s.close()

	return ip
