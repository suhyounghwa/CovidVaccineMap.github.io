from DataCrawling import *
from DataCleaning import *

def Main():
    keyValue = "&serviceKey=SVAIOlt%2FwZYCMlBnNwQY0KF1QgscYyBeOzrRxwAlFGGNXwxR4I5vGO4LNfv7VvkPb%2B%2BI6q0Rk26GaRQzOI1wew%3D%3D"
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
     
    pageData = 10
    perPageData = 10
    jsonSearchResult = GetGoVSearchResult(endPoint, pageData, perPageData, keyValue) #공공기관 예방접종센터
    jsonSearchResult2 = GetGoVSearchResult(endPoint2, pageData, perPageData, keyValue) #사설기관 예방접종센터

    for data in jsonSearchResult['data']:  #'data' 에서 센터주소,센터명,센터전화번호를 가져옴
        jsonCleaningData=GetCenterData(jsonSearchResult, "address", "centerName", "phoneNumber")

    for data in jsonSearchResult2['data']:
        jsonCleaningData2=GetCenterData(jsonSearchResult2, "orgZipaddr", "orgnm", "orgTlno")
    
    jsonCleaningData3=jsonCleaningData+jsonCleaningData2  #합침

    print(jsonCleaningData3)

if __name__ == '__main__':
    Main()

