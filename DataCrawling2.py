import urllib.request
import datetime
import json

def Get_Request_Url(url):
    req = urllib.request.Request(url) #검색 URL 경로 지정

    try:
        response = urllib.request.urlopen(req) # URL을 통해 데이터 요청해서 결과 받음
        if response.getcode() == 200: # 성공코드 : 200
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())
            return(response.read().decode('utf-8'))
    except Exception as ex: # 예외처리
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None

def GetGoVSearchResult(pageValue, perPageValue) : # 사전 준비 작업 및 분류_공공기관
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"

    paraData = "page=" + str(pageValue)
    paraData += "&perPage=" + str(perPageValue)
    keyValue = "&serviceKey=wYSMgFdFROFGWeVY61sO%2FkEsOjQSVRIdOWKXyeFBXKMl0Xg3mr4LZ31GKCBjpRHU3joClHkaQGlhndG3uJX%2BBg%3D%3D"

    url = endPoint + paraData + keyValue

    resultData = Get_Request_Url(url)

    if(resultData == None):
        return None
    else:
        return json.loads(resultData)

def GetGoVSearchResult2(pageValue, perPageValue) : # 사전 준비 작업 및 분류_민간병원
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"

    paraData2 = "page=" + str(pageValue)
    paraData2 += "&perPage=" + str(perPageValue)
    keyValue2 = "&serviceKey=wYSMgFdFROFGWeVY61sO%2FkEsOjQSVRIdOWKXyeFBXKMl0Xg3mr4LZ31GKCBjpRHU3joClHkaQGlhndG3uJX%2BBg%3D%3D"

    url2 = endPoint2 + paraData2 + keyValue2

    resultData = Get_Request_Url(url2)

    if(resultData == None):
        return None
    else:
        return json.loads(resultData)
