# -*- coding: utf-8 -*-
from flask import Flask, request
from datetime import datetime as dt
from app.functions import *
app = Flask(__name__)


@app.after_request
def add_header(response):

	response.headers['Cache-Control'] = 'public, max-age=180'
	return response


@app.route("/")
def hello1():

	return "Hello World from Flask, Choya"


# 飛行速率單位轉換
@app.route("/calFlyDist2Unit", methods=['GET'])
def FlyDist2Unit():

	flyDist = request.args.get('FlyDist', type=float, default=1)
	unit = request.args.get('Unit', type=str, default='M')

	result = calFlyDist2Unit(unit, flyDist)
	return str(result)


# 依據出發、抵達、日出、日落時間，計算總飛行時間
@app.route("/calFlyTime", methods=['GET'])
def FlyTime():

	# 出發、抵達時間
	liberationDT = request.args.get('LiberationDT', type=str)
	arrivalDT = request.args.get('ArrivalDT', type=str)

	# 日出、日落時間
	sunriseTime = request.args.get('SunriseTime', type=str, default='06:00:00')
	sunsetTime = request.args.get('SunsetTime', type=str, default='18:00:00')

	# 判斷是否計算夜間時間
	isFix = request.args.get('IsFix', type=int, default=1)

	liberationDT = dt.strptime(liberationDT, '%Y-%m-%d %H:%M:%S')
	arrivalDT = dt.strptime(arrivalDT, '%Y-%m-%d %H:%M:%S')
	sunriseTime = dt.strptime(sunriseTime, '%H:%M:%S')
	sunsetTime = dt.strptime(sunsetTime, '%H:%M:%S')

	time = calFlyTime(liberationDT, arrivalDT, sunriseTime, sunsetTime, isFix)
	return 	'共飛行' + str(time) + '分鐘'


# 依據經緯度計算飛行距離
@app.route("/calGPSDistance", methods=['GET'])
def GPSDistance():

	startLongitude = request.args.get('StartLongitude', type=float, default=0)
	startLatitude = request.args.get('StartLatitude', type=float, default=0)
	endLongitude = request.args.get('EndLongitude', type=float, default=0)
	endLatitude = request.args.get('EndLatitude', type=float, default=0)

	result = calGPSDistance(startLongitude, startLatitude, endLongitude, endLatitude)
	return str(result)


if __name__ == "__main__":
	# Only for debugging while developing
	app.run(host='0.0.0.0', debug=True, port=8080)