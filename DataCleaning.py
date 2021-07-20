#import json
import pandas as pd

'''
    백신접종 센터 데이터 정제 함수 (주소/센터명/전화번호 추출)
    resultData - 백신접종 센터 JSON 데이터
    address - JSON 파일의 주소 변수 명
    name - JSON 파일의 센터명 변수 명
    number - JSON 파일의 전화번호 변수 명
    Main에서의 함수 호출 예 
         DataCleaning.GetCenterData(resultData, "orgZipaddr", "orgnm", "orgTlno")
'''
def GetCenterData(resultData, address, name, number):
    # json 파일의 data 키값 데이터를 DataFrame 형태로 저장
    tempResult = pd.DataFrame(resultData['data'])
    # 키 값으로 주소/센터명/번호 값 추출하여 DataFrame 형태로 저장
    centerResult = tempResult[[str(address), str(name), str(number)]]
    return [centerResult]

'''
    위치 데이터 정제 함수 (위도/경도 추출)
    tempData - 위치 JSON 데이터 
    Main에서의 함수 호출 예
         DataCleaning.GetGeoLocationData(tempData)
'''
def GetGeoLocationData(tempData):
    # addresses 키 값의 x 값 출력
    xData = tempData['addresses'][0]['x']
    # addresses 키 값의 y 값 출력
    yData = tempData['addresses'][0]['y']
    return [yData, xData]