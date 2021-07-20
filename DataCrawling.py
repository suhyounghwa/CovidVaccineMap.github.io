import urllib.request
import datetime
import json

def Get_Request_Url(url):# 데이터 크롤링
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

def GetGoVSearchResult(endPoint, pageValue, perPageValue, keyValue) : # 사전 준비 작업 및 분류
    paraData = "page=" + str(pageValue)
    paraData += "&perPage=" + str(perPageValue)
    

    url = endPoint + paraData + keyValue

    resultData = Get_Request_Url(url)

    if(resultData == None):
        return None
    else:
        return json.loads(resultData)
