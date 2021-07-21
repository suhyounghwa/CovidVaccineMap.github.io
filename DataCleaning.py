import pandas as pd

'''
    백신접종 센터 데이터 정제 함수 (주소/센터명/전화번호 추출)
    resultData - 백신접종 센터 JSON 데이터
    addr - JSON 파일의 주소 변수 명
    name - JSON 파일의 센터명 변수 명
    number - JSON 파일의 전화번호 변수 명
    cityData : 입력한 지역 이름
    함수 호출 예 
        GetCenterData(resultData, "orgZipaddr", "orgnm", "orgTlno", "서울특별시")
'''
def GetCenterData(resultData, addr, name, num, city):
    # json 파일의 data 키값 데이터를 DataFrame 형태로 저장
    tempResult = pd.DataFrame(resultData['data'])
    # 주소/센터명/번호만 추출하여 DataFrame 형태로 저장
    tempResult = tempResult[[str(addr), str(name), str(num)]]
    # 컬럼 확인 후 입력한 지역명의 데이터만 저장
    if str(addr) in tempResult.columns:
        centerResult = tempResult[tempResult[str(addr)].str.contains(city)]
        centerAddr = centerResult[str(addr)].values
        centerName = centerResult[str(name)].values
        centerNum = centerResult[str(num)].values

    return [centerAddr, centerName, centerNum]

'''
    위치 데이터 정제 함수 (위도/경도 추출)
    tempData - 위치 JSON 데이터 
    함수 호출 예
         GetGeoLocationData(tempData)
'''
def GetGeoLocationData(tempData):
    # addresses 키 값의 x 값 출력
    xData = tempData['addresses'][0]['x']
    # addresses 키 값의 y 값 출력
    yData = tempData['addresses'][0]['y']
    return [yData, xData]