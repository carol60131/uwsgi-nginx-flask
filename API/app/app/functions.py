# -*- coding: utf-8 -*-
import math
from datetime import datetime as dt
import datetime


def calFlyDist2Unit(unit, flyDist):

	# 公里
	if unit == 'Km':
		result = flyDist / 0.001

	# 英尺
	elif unit == 'ft':
		result = flyDist * 0.3048
	
	# 碼
	elif unit == 'Yrds':
		result = flyDist * 0.9144
	
	# 英哩
	elif unit == 'Miles':
		result = flyDist * 0.6214 / 0.001

	# 公尺
	else:
		result = flyDist

	result = "{:.3f}".format(result)
	return result


def calFlyTime(liberationDT, arrivalDT, sunriseTime, sunsetTime, isFix):

	# 不計算夜間時間
	if isFix == 1:

		# 出發日期與抵達日期相同(抵達時間-出發時間)
		if arrivalDT.date() == liberationDT.date():
			result = arrivalDT - liberationDT
			resMin = result.seconds / 60 

			return resMin		

		else:
			# 將日出、日落時間與出發時間格式化為同日期
			sunriseTime = dt.strptime(str(liberationDT.date()) + ' ' + str(sunriseTime.time()), '%Y-%m-%d %H:%M:%S')
			sunsetTime = dt.strptime(str(liberationDT.date()) + ' ' + str(sunsetTime.time()), '%Y-%m-%d %H:%M:%S')

			# 日落時間-出發時間(第一天)
			result = sunsetTime - liberationDT

			while True:
				# 出發、日出、日落時間加一日
				liberationDT = liberationDT + datetime.timedelta(days=1)
				sunriseTime = sunriseTime + datetime.timedelta(days=1)
				sunsetTime = sunsetTime + datetime.timedelta(days=1)
				
				if arrivalDT.date() == liberationDT.date():
					break

				else:
					# 日落時間-日出時間
					result += sunsetTime - sunriseTime

			# 抵達時間-日出時間(最後一日)
			result += arrivalDT - sunriseTime
			resMin = result.total_seconds() / 60 

			return resMin

	# 計算夜間時間
	elif isFix == 2:

		# 抵達時間-出發時間
		result = arrivalDT - liberationDT
		resMin = result.total_seconds() / 60 

		return resMin


def calGPSDistance(slong, slat, elong, elat):

	if slong != 0 and slat != 0 and elong != 0 and elat != 0:
		m_Longitude = slong
		m_Latitude = slat
		P_m_Longitude = elong
		P_m_Latitude = elat

		m_a = 6378137.8
		m_finv = 298.257223563

		pi = 3.14159265358979323846
		COORD_EPSILON = 1.e-10
		EPSILON = 5.e-14

		m_Radius = 6366707.01896486
		m_GeosyncRadius = 42164211
		m_Deg2Rad = 1.74532925199433E-02

		dlat1 = m_Deg2Rad * m_Latitude
		dlat2 = m_Deg2Rad * P_m_Latitude
		dlong1 = m_Deg2Rad * m_Longitude
		dlong2 = m_Deg2Rad * P_m_Longitude

		a0 = m_a
		flat = 1 / m_finv
		r = 1 - flat
		b0 = a0 * r

		tanu1 = r * math.tan(dlat1)
		tanu2 = r * math.tan(dlat2)

		dtmp = math.atan(tanu1)
		if abs(m_Latitude) >= 90:
			dtmp = dlat1

		cosu1 = math.cos(dtmp)
		sinu1 = math.sin(dtmp)

		dtmp = math.atan(tanu2)
		if abs(P_m_Latitude) >= 90:
			dtmp = dlat2

		cosu2 = math.cos(dtmp)
		sinu2 = math.sin(dtmp)

		omega = dlong2 - dlong1

		lambda1 = omega

		while True:
			testlambda = lambda1
			ss1 = cosu2 * math.sin(lambda1)
			ss2 = cosu1 * sinu2 - sinu1 * cosu2 * math.cos(lambda1)
			ss = math.sqrt(ss1 * ss1 + ss2 * ss2)
			cs = sinu1 * sinu2 + cosu1 * cosu2 * math.cos(lambda1)
			sigma = math.atan2(ss, cs)
			sinalpha = cosu1 * cosu2 * math.sin(lambda1) / ss
			cosalpha2 = 1 - sinalpha * sinalpha
			c2sm = cs - 2 * sinu1 * sinu2 / cosalpha2
			c = flat / 16 * cosalpha2 * (4 + flat * (4 - 3 * cosalpha2))
			lambda1 = omega + (1 - c) * flat * sinalpha * (sigma + c * ss * (c2sm + c * cs * (-1 + 2 * c2sm * c2sm)))
			dDeltaLambda = abs(testlambda - lambda1)

			if dDeltaLambda > EPSILON:
				break

		u2 = cosalpha2 * (a0 * a0 - b0 * b0) / (b0 * b0)
		a = 1 + (u2 / 16384) * (4096 + u2 * (-768 + u2 * (320 - 175 * u2)))
		b = (u2 / 1024) * (256 + u2 * (-128 + u2 * (74 - 47 * u2)))

		dsigma = b * ss * (c2sm + (b / 4) * (cs * (-1 + 2 * c2sm * c2sm) - (b / 6.) * c2sm * (-3 + 4 * ss * ss) * (-3 + 4 * c2sm * c2sm)))

		s = b0 * a * (sigma - dsigma)
		s = s / 1000

	else:
		s = 0
	
	return s
