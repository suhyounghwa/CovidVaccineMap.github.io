import json
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
    # json 파일을 파이썬 객체로 읽기
    tempData = json.loads(resultData)

    # json 파일을 DataFrame으로 변환
    tempData_df = pd.DataFrame(tempData['data'])

    # 키 값으로 주소/센터명/번호 값 추출하여 데이터프레임 형태로 h_result에 저장
    #h_result = tempData_df[[str(address), str(name), str(number)]]
    h_result = tempData_df[[address, name, number]]

    return [h_result]

'''
    위치 데이터 정제 함수 (위도/경도 추출)
    tempData - 위치 JSON 데이터 
    Main에서의 함수 호출 예
         DataCleaning.GetGeoLocationData(tempData)
'''
def GetGeoLocationData(tempData):
    xdata = tempData['addresses'][0]['x']
    ydata = tempData['addresses'][0]['y']
    return [ydata, xdata]
