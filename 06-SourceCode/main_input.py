from DataCrawling import *
from DataCleaning import *
import pandas as pd
import folium

def Main():
    keyValue = "&serviceKey=SVAIOlt%2FwZYCMlBnNwQY0KF1QgscYyBeOzrRxwAlFGGNXwxR4I5vGO4LNfv7VvkPb%2B%2BI6q0Rk26GaRQzOI1wew%3D%3D"
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
     
    pageData = 0
    perPageData = 248
    perPageData2 = 10000
  
    jsonSearchResult = GetGoVSearchResult(endPoint, pageData, perPageData, keyValue) #공공기관 예방접종센터
    jsonSearchResult2 = GetGoVSearchResult(endPoint2, pageData, perPageData2, keyValue) #사설기관 예방접종센터

    #"서울특별시"에 있는 센터주소,센터명,센터전화번호를 가져옴
    addr, name, num, lat, lng= GetCenterData(jsonSearchResult, "address","centerName","phoneNumber","lat","lng","서울특별시")
    addr2, name2, num2, location = GetCenterData(jsonSearchResult2,"orgZipaddr","orgnm","orgTlno",None,None,"서울특별시")
    
    # 센터주소, 센터명, 센터전화번호 데이터를 이용하여 데이터프레임 생성 
    jsonCleaningData = pd.DataFrame(data=list(zip(addr, name, num, lat, lng)), columns = ['Addr', 'name', 'num','lat','lng'])    
    jsonCleaningData2 = pd.DataFrame(data=list(zip(addr2, name2, num2, location)), columns = ['Addr', 'name', 'num','location'])
    #jsonCleaningData3= jsonCleaningData.append(jsonCleaningData2,ignore_index=True)
    print(jsonCleaningData, jsonCleaningData2)

    # 사용자 입력 받기
    userInput= input("병원 이름을 입력하세요 : ")

    # 만약 공공 기관인 경우
    if("코로나19" in userInput) :
        # 센터명을 포함하는 행 추출
        centerResult = jsonCleaningData[jsonCleaningData['name'].str.contains(userInput)]
        # 위도/경도 추출
        centerLat = centerResult['lat'].values
        centerLng = centerResult['lng'].values
        centerLocation = [centerLat, centerLng]
    else: # 민간 기관인 경우
        centerResult = jsonCleaningData2[jsonCleaningData2['name'].str.contains(userInput)]
        centerLocation = centerResult['location'].values
        centerLocation = centerLocation[0]

    # 좌표 찍기
    map_data = folium.Map(location=centerLocation, zoom_start=15)
    map_data = folium.Marker(centerLocation, tooltip=str(centerResult['name'].values)).add_to(map_data)
    map_data.save(r'.\googlemap_input.html')
    print("맵 표시 완료")

if __name__ == '__main__':
    Main()
