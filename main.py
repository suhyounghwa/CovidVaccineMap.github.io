from DataCrawling import *
from DataCleaning import *
import pandas as pd
from pandas.io.json import json_normalize


def Main():
    keyValue = "&serviceKey=SVAIOlt%2FwZYCMlBnNwQY0KF1QgscYyBeOzrRxwAlFGGNXwxR4I5vGO4LNfv7VvkPb%2B%2BI6q0Rk26GaRQzOI1wew%3D%3D"
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
     
    pageData = 1
    perPageData = 100
    jsonSearchResult = GetGoVSearchResult(endPoint, pageData, perPageData, keyValue) #공공기관 예방접종센터
    jsonSearchResult2 = GetGoVSearchResult(endPoint2, pageData, perPageData, keyValue) #사설기관 예방접종센터

    #"서울특별시"에 있는 센터주소,센터명,센터전화번호를 가져옴
    #jsonCleaningData=GetCenterData(jsonSearchResult, "address","centerName","phoneNumber","서울특별시")
    #jsonCleaningData2=GetCenterData(jsonSearchResult2,"orgZipaddr","orgnm","orgTlno","서울특별시")
    addr, name, num = GetCenterData(jsonSearchResult, "address","centerName","phoneNumber","서울특별시")
    addr2, name2, num2 = GetCenterData(jsonSearchResult2,"orgZipaddr","orgnm","orgTlno","서울특별시")
    
    # 센터주소, 센터명, 센터전화번호 데이터를 이용하여 데이터프레임 생성 
    jsonCleaningData = pd.DataFrame(data=list(zip(addr, name, num)), columns = ['Addr', 'name', 'num'])   
    jsonCleaningData2 = pd.DataFrame(data=list(zip(addr2, name2, num2)), columns = ['Addr', 'name', 'num']) 
    #jsonCleaningData3= jsonCleaningData+jsonCleaningData2  #합침
    
    print(jsonCleaningData, jsonCleaningData2)

    

if __name__ == '__main__':
    Main()

