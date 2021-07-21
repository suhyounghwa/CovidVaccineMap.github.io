from ssl import create_default_context
import pandas as pd

def GetCenterData(resultData, address, name, number,lat,lng,city):
    # json 파일의 data 키값 데이터를 DataFrame 형태로 저장
    tempResult = pd.DataFrame(resultData['data'])
    # 키 값으로 주소/센터명/번호 값 추출하여 DataFrame 형태로 저장
    if(lat!=None):
        tempResult = tempResult[[str(address), str(name), str(number),str(lat),str(lng)]]
    # 컬럼 확인 후 입력한 지역명의 데이터만 저장
        centerResult = tempResult[tempResult['address'].str.contains(city)]
        centerAddr = centerResult['address'].values
        centerName = centerResult['centerName'].values
        centerNum = centerResult['phoneNumber'].values
        centerlng = centerResult['lng'].values
        centerlat = centerResult['lat'].values
        
    
    else:
        centerResult = tempResult[tempResult['orgZipaddr'].str.contains(city)]
        centerAddr = centerResult['orgZipaddr'].values
        centerName = centerResult['orgnm'].values
        centerNum = centerResult['orgTlno'].values
        centerlat= None
        centerlng=None
    return [centerAddr, centerName, centerNum,centerlat,centerlng]


#def GetEachData(resultData, address, name, number, city):