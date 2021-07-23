#from naverDataMap import *
from numpy import NaN
from DataCrawling import *
from DataCleaning import *
import pandas as pd
import folium
import math
import time

def Main():
    start = time.time()

    keyValue = "&serviceKey=SVAIOlt%2FwZYCMlBnNwQY0KF1QgscYyBeOzrRxwAlFGGNXwxR4I5vGO4LNfv7VvkPb%2B%2BI6q0Rk26GaRQzOI1wew%3D%3D"
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
     
    pageData = 1
    perPageData = 284
    perPageData2 = 10000

    jsonSearchResult = GetGoVSearchResult(endPoint, pageData, perPageData, keyValue) #공공기관 예방접종센터
    jsonSearchResult2 = GetGoVSearchResult(endPoint2, pageData, perPageData2, keyValue) #사설기관 예방접종센터
    
    #"서울특별시"에 있는 센터주소,센터명,센터전화번호를 가져옴
    addr, name, num, lat, lng= GetCenterData(jsonSearchResult, "address","centerName","phoneNumber","lat","lng","서울특별시")
    addr2, name2, num2, lat2, lng2 = GetCenterData(jsonSearchResult2,"orgZipaddr","orgnm","orgTlno",None,None,"서울특별시")
    
    # 센터주소, 센터명, 센터전화번호 데이터를 이용하여 데이터프레임 생성 
    jsonCleaningData = pd.DataFrame(data=list(zip(addr, name, num, lat, lng)), columns = ['Addr', 'name', 'num','lat','lng'])    
    jsonCleaningData2 = pd.DataFrame(data=list(zip(addr2, name2, num2)), columns = ['Addr', 'name', 'num']) 

    jsonCleaningData3= jsonCleaningData.append(jsonCleaningData2,ignore_index=True)
    print("time:",time.time()-start)
    jsonCleaningData3.iloc[2245] = 0
    #jsonCleaningData4 = jsonCleaningData3.drop(jsonCleaningData3.index[2245])
    print(jsonCleaningData3.head(2246))
    print("정제끝")
    # i=0
    # inputCenterName=input("센터이름 입력 :")
    # for x in jsonCleaningData3['name']:   
    #   if (x==str(inputCenterName)):        
    #     if  math.isnan(float(jsonCleaningData3['lat'][i])):
    #       Location=GetLngLatData(GetGeoLocationData(jsonCleaningData3['Addr'][i]))
    #       map_data=folium.Map(Location,tzoom_start=12)
    #       marker= folium.Marker(Location, popup=jsonCleaningData3['num'][i], tooltip=jsonCleaningData3['name'][i],icon=folium.Icon(color="red"))
    #     else:
    #       Location=[jsonCleaningData3['lat'][i],jsonCleaningData3['lng'][i]]
    #       map_data=folium.Map(Location,zoom_start=12)
    #       marker= folium.Marker(Location,color='blue' ,popup=jsonCleaningData3['num'][i], tooltip=jsonCleaningData3['name'][i],icon=folium.Icon(color="green")) 
      
    #     marker.add_to(map_data)
    #     map_data.save(r'c:\module1\navermap4.html')
    #     print("[%s] 저장 성공 : " % datetime.datetime.now())
    #     break
    #   i=i+1
    

    i=0
    map_data = folium.Map([37.56595045963169, 126.98918361888224],zoom_start=12)
    count = 0
    for x in jsonCleaningData3['Addr']:        
        if math.isnan(float(jsonCleaningData3['lat'][i])):
          Location=GetLngLatData(GetGeoLocationData(jsonCleaningData3['Addr'][i]))
          marker= folium.Marker(Location, popup=jsonCleaningData3['num'][i], tooltip=jsonCleaningData3['name'][i],icon=folium.Icon(color="red"))
          marker.add_to(map_data)
        else:
          Location=[jsonCleaningData3['lat'][i],jsonCleaningData3['lng'][i]]
          marker= folium.Marker(Location,color='blue' ,popup=jsonCleaningData3['num'][i], tooltip=jsonCleaningData3['name'][i],icon=folium.Icon(color="green")) 
          marker.add_to(map_data)
        i=i+1
        count += 1
        print(count)
    map_data.save(r'c:\module1\navermap4.html')
  
    print("[%s] 저장 성공 : " % datetime.datetime.now())
    print("time:",time.time()-start)#전체 걸리는 시간을 초로 나타낸 것

if __name__ == '__main__':
    Main()

 
