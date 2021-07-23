import pandas as pd
from DataCrawling import GetGeoLocationData
import numpy as np
import multiprocessing
'''
    백신접종센터 데이터 정제 함수 (주소/센터명/전화번호/위도/경도 추출)
    resultData - 백신접종센터 JSON 데이터
    addr - JSON 파일의 주소 변수 명
    name - JSON 파일의 센터명 변수 명
    num - JSON 파일의 전화번호 변수 명
    lat - JSON 파일의 위도 변수 명
    lng - JSON 파일의 경도 변수 명
    city - 정제할 지역명 
    Main에서의 함수 호출 예 
         GetCenterData(jsonSearchResult, "address","centerName","phoneNumber","lat","lng","서울특별시")
'''
def GetCenterData(resultData, addr, name, num, lat, lng, city):
    # json 파일의 data 키값 데이터를 DataFrame 형태로 저장
    tempResult = pd.DataFrame(resultData['data'])
    # 컬럼 확인 후 입력한 지역명의 데이터만 저장
    centerResult = tempResult[tempResult[str(addr)].str.contains(city)]
    # 주소/센터명/번호/위도/경도 값만 추출하여 DataFrame 형태로 저장
    centerAddr = centerResult[str(addr)].values
    centerName = centerResult[str(name)].values
    centerNum = centerResult[str(num)].values
    if(lat!=None):
        centerlng = centerResult[lng].values
        centerlat = centerResult[lat].values
        return [centerAddr, centerName, centerNum,centerlat,centerlng]    
    else:
        centerlng = []
        centerlat = []
        pool=multiprocessing.Pool(processes=multiprocessing.cpu_count())
        centerData=pool.map(mtPr,centerAddr)
        '''
        for addrStr in centerAddr:
            centerLocation = GetLngLatData(GetGeoLocationData(addrStr))
            centerlat.append(centerLocation[0])
            centerlng.append(centerLocation[1])
        #centerlat= None
        #centerlng=None
        '''
        return [centerAddr, centerName, centerNum,centerData]
def mtPr(centerAddr):
    center1=GetGeoLocationData(centerAddr)
    centerLocation=GetLngLatData(center1)
    centerlng=centerLocation[0]
    centerlat=centerLocation[1]
    
    return [centerlng,centerlat]
'''
    민간병원 데이터 정제 함수 (위도/경도 추출)
    LocationData - 위치 JSON 데이터 
    Main에서의 함수 호출 예
         DataCleaning.GetLngLatData(LocationData)
'''
def GetLngLatData(LocationData):
        # 정제 - JSON 파일 분석 후 데이터 찾기 - 위도 / 경도 값
        xdata = LocationData['addresses'][0]['x']
        ydata = LocationData['addresses'][0]['y']
        return [ydata, xdata]