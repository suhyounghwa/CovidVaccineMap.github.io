# 공공 데이터 가져오기 (godata.go.kr)
# 공공 병원 + 민간 병원 데이터 합치기

import urllib.request
import datetime
import json

def Get_Request_Url(url): # 크롤러를 담당하는 부분
    req = urllib.request.Request(url) # 검색 URL 경로 지정
    try:
        response = urllib.request.urlopen(req) # URL을 통해 데이터 요청해서 결과 받음
        if response.getcode() == 200: # 200 코드 번호면 성공 400/500 은  Naver 문서에서 확인
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as ex:
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None

def GetGoVSearchResult(endPoint, pageValue, perPageValue, keyValue): # 사전 준비 작업 및 분류
    paraData = "page=" + str(pageValue)
    paraData += "&perPage=" + str(perPageValue)
    

    url = endPoint + paraData + keyValue

    resultData = Get_Request_Url(url)

    if(resultData == None):
        return None
    else:
        return json.loads(resultData)

def GetDateChange(data, jsonResult):
    resultOrg = data['centerName'] + ' ' + data['org']
    resultAddress = data['address']
    resultPhoneNumber = data['phoneNumber']

    jsonResult.append({ 'org' : resultOrg,
                        'address' : resultAddress,
                        'phoneNumber' : resultPhoneNumber
    })

    return

def getDataChange2(data, jsonResult):
    resultOrg = data['orgnm']
    resultAddress = data['orgZipaddr']
    resultPhoneNumber = data['orgTlno']

    jsonResult.append({ 'org' : resultOrg,
                        'address' : resultAddress,
                        'phoneNumber' : resultPhoneNumber
    })

    return

def Main():
    keyValue = "&serviceKey=SVAIOlt%2FwZYCMlBnNwQY0KF1QgscYyBeOzrRxwAlFGGNXwxR4I5vGO4LNfv7VvkPb%2B%2BI6q0Rk26GaRQzOI1wew%3D%3D"
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"

    jsonDataResult = []
    jsonDataResult2 = []

    pageData = 1
    perPageData = 100

    jsonSearchResult = GetGoVSearchResult(endPoint, pageData, perPageData, keyValue)
    jsonSearchResult2 = GetGoVSearchResult(endPoint2, pageData, perPageData, keyValue)

    for data in jsonSearchResult['data']:
        GetDateChange(data, jsonDataResult)
    for data in jsonSearchResult2['data']:
        getDataChange2(data, jsonDataResult2)
    jsonDataResult3 = jsonDataResult + jsonDataResult2
    with open('%s_GoVData_%s.json' % ('병원3', '데이터'), 'w', encoding='utf-8') as filedata:
        rJson = json.dumps(jsonDataResult3 ,
                            indent=4, 
                            sort_keys=True, 
                            ensure_ascii=False)
        filedata.write(rJson)

    print('파일이름 : %s_GoVData_%s.json 저장완료' % ('병원3', '데이터'))

if __name__ == '__main__':
    Main()

