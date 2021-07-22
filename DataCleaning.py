import pandas as pd

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
    else:
        centerlat= None
        centerlng=None
    return [centerAddr, centerName, centerNum,centerlat,centerlng]

def GetLngLatData(LocationData):
        # 정제 - JSON 파일 분석 후 데이터 찾기 - 위도 / 경도 값
        xdata = LocationData['addresses'][0]['x']
        ydata = LocationData['addresses'][0]['y']
        return [ydata, xdata]