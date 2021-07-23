from DataCrawling import *
from DataCleaning import *
import pandas as pd
import folium

def Main():
    keyValue = "&serviceKey=SVAIOlt%2FwZYCMlBnNwQY0KF1QgscYyBeOzrRxwAlFGGNXwxR4I5vGO4LNfv7VvkPb%2B%2BI6q0Rk26GaRQzOI1wew%3D%3D"
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    pageData = 1
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
    
    map_data = folium.Map([37.56595045963169, 126.98918361888224],zoom_start=12)

    for i in range(0, len(jsonCleaningData)):
      Location=[jsonCleaningData['lat'][i],jsonCleaningData['lng'][i]]
      marker= folium.Marker(Location,popup=jsonCleaningData['num'][i], tooltip=jsonCleaningData['name'][i],icon=folium.Icon(color="green"))
      marker.add_to(map_data)    
    for i in range(0, len(jsonCleaningData2)):
      Location=[jsonCleaningData2['location'][i]]
      marker= folium.Marker(Location[0],popup=jsonCleaningData2['num'][i], tooltip=jsonCleaningData2['name'][i],icon=folium.Icon(color="red"))
      marker.add_to(map_data)
      
    map_data.save(r'.\googlemap.html')
  

if __name__ == '__main__':
    Main()
