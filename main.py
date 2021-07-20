from DataCrawling import *
from DataCleaning import *

def Main():
    keyValue = "&serviceKey=SVAIOlt%2FwZYCMlBnNwQY0KF1QgscYyBeOzrRxwAlFGGNXwxR4I5vGO4LNfv7VvkPb%2B%2BI6q0Rk26GaRQzOI1wew%3D%3D"
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
     
    
    #jsonDataResult2=[]
    pageData = 10
    perPageData = 10
    jsonSearchResult = GetGoVSearchResult(endPoint, pageData, perPageData, keyValue)
    jsonSearchResult2 = GetGoVSearchResult(endPoint2, pageData, perPageData, keyValue)
    jsonDataResult=json.loads(jsonSearchResult)
    jsonDataResult2=json.loads(jsonSearchResult2)
   
    for data in jsonDataResult['data']:
        jsonCleaningData=GetCenterData(jsonSearchResult, "address", "centerName", "phoneNumber")

    for data in jsonDataResult2['data']:
        jsonCleaningData2=GetCenterData(jsonSearchResult2, "orgZipaddr", "orgnm", "orgTlno")
    
    jsonCleaningData3=jsonCleaningData+jsonCleaningData2

    print(jsonCleaningData3)

    '''
    with open('%s_GoVData_%s.json' % ('병원6', '데이터'), 'w', encoding='utf-8') as filedata:
 
        print(type(jsonDataResult3))
        rJson = json.dumps( jsonDataResult3,
                            indent=4, 
                            sort_keys=True, 
                            ensure_ascii=False)
      
        
        filedata.write(jsonDataResult3)
    
    print('파일이름 : %s_GoVData_%s.json 저장완료' % ('병원6', '데이터'))
    '''
    
if __name__ == '__main__':
    Main()

