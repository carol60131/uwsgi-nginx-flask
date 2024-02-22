將 AVANCE 內方法寫為 API

1. 飛行速率單位轉換 (calFlyDist2Unit)
Body:
{
    "FlyDist":1,
    "Unit":"Km"
}

FlyDist: 飛行距離( float數值)，預設為1
Unit：單位(M, Km, ft, Yrds, Miles)，預設為M


2. 計算總飛行時間 (calFlyTime)
Body:
{
    "LiberationDT": "2024-02-14 08:00:00",
    "ArrivalDT": "2024-02-17 17:00:00",
    "SunriseTime": "06:00:00",
    "SunsetTime":"18:00:00",
    "EndDT":"2024-02-17 15:00:00",
    "IsFix":2
}

LiberationDT：放飛時間，例：2024-02-14 08:00:00 
ArrivalDT：抵達時間，例：2024-02-17 17:00:00
SunriseTime：日出時間，預設為 06:00:00
SunsetTime：日落時間，預設為 18:00:00
EndDT：比賽結束時間，例：2024-02-17 15:00:00
IsFix：判斷是否計算夜間時間(1:不計算，2:計算) ，預設為1


3. 依據經緯度計算飛行距離 (calGPSDistance)
Body:
{
    "StartLongitude": 123.19464,
    "StartLatitude": 25.20548,
    "EndLongitude": 120.4141,
    "EndLatitude": 24.2921
}

StartLongitude：起始經度，預設為 0，例：123.19464
StartLatitude：起始緯度，預設為 0，例：25.20548
EndLongitude：結束經度，預設為 0，例：120.4141
EndLatitude：結束緯度，預設為 0，例：24.2921

