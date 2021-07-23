#from naverDataMap import *
from numpy import NaN
from DataCrawling import *
from DataCleaning import *
import pandas as pd
import folium

def Main():
    keyValue = "&serviceKey=SVAIOlt%2FwZYCMlBnNwQY0KF1QgscYyBeOzrRxwAlFGGNXwxR4I5vGO4LNfv7VvkPb%2B%2BI6q0Rk26GaRQzOI1wew%3D%3D"
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
     
    pageData = 0
    perPageData = 100
    perPageData2 = 100
  
    jsonSearchResult = GetGoVSearchResult(endPoint, pageData, perPageData, keyValue) #공공기관 예방접종센터
    jsonSearchResult2 = GetGoVSearchResult(endPoint2, pageData, perPageData2, keyValue) #사설기관 예방접종센터

    #"서울특별시"에 있는 센터주소,센터명,센터전화번호를 가져옴
    addr, name, num, lat, lng= GetCenterData(jsonSearchResult, "address","centerName","phoneNumber","lat","lng","서울특별시")
    addr2, name2, num2, lat2, lng2 = GetCenterData(jsonSearchResult2,"orgZipaddr","orgnm","orgTlno",None,None,"서울특별시")
    
    # 센터주소, 센터명, 센터전화번호 데이터를 이용하여 데이터프레임 생성 
    jsonCleaningData = pd.DataFrame(data=list(zip(addr, name, num, lat, lng)), columns = ['Addr', 'name', 'num','lat','lng'])    
    jsonCleaningData2 = pd.DataFrame(data=list(zip(addr2, name2, num2)), columns = ['Addr', 'name', 'num']) 
    jsonCleaningData3= jsonCleaningData.append(jsonCleaningData2,ignore_index=True)
    print(jsonCleaningData3)

    # 사용자 입력 받기
    userInput= input("병원 이름을 입력하세요 : ")

    # 센터명을 포함하는 행 추출
    centerResult = jsonCleaningData3[jsonCleaningData3['name'].str.contains(userInput)]
    # 위도/경도 추출
    centerLat = centerResult['lat'].values
    centerLng = centerResult['lng'].values

    

    # 만약 위도/경도가 NaN일 경우 위도/경도 함수 이용
    if(pd.isna(centerLat)) :
        centerAddr = centerResult['Addr'].values
        centerAddr = centerAddr[0]
        print(centerAddr)
        LocationData=GetGeoLocationData(centerAddr)
        centerLocation=GetLngLatData(LocationData)
    else: 
        centerLocation = [centerLat, centerLng]
        

    # 좌표 찍기
    map_data = folium.Map(location=centerLocation, zoom_start=15)
    map_data = folium.Marker(centerLocation, popup='확인', tooltip=centerResult['name'].values).add_to(map_data)
    map_data.save(r'c:\module1\navermap_hyogeong.html')
    print("맵 표시 완료")
    
    '''
    i=0
    map_data = folium.Map([37.56595045963169, 126.98918361888224],zoom_start=12)
    
    for x in jsonCleaningData['Addr']:
      Location=[jsonCleaningData['lat'][i],jsonCleaningData['lng'][i]]
      marker= folium.Marker(Location,color='blue' ,popup=jsonCleaningData['num'][i], tooltip=jsonCleaningData['name'][i],icon=folium.Icon(color="green"))
      marker.add_to(map_data)
      i=i+1
    i=0
    for x in jsonCleaningData2['Addr']:
      LocationData=GetGeoLocationData(x)
      Location=GetLngLatData(LocationData)
      marker= folium.Marker(Location, popup=jsonCleaningData2['num'][i], tooltip=jsonCleaningData2['name'][i],icon=folium.Icon(color="red"))
      marker.add_to(map_data)
      i=i+1  
    map_data.save(r'c:\module1\navermap2.html')
    print("[%s] 저장 성공 : " % datetime.datetime.now())
    '''

if __name__ == '__main__':
    Main()