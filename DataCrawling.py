import urllib.request
import datetime
import json

client_id = "5l5yadvenl"
client_secret = "ygf36whrwrx4XQGFoGaepijGIrvEdHWIvgCgnmF8"
baseUrl = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

# 코로나 백신접종 센터 데이터 크롤링(공공기관/위탁의료기관)
def Get_Request_Url(url):
    req = urllib.request.Request(url) #검색 URL 경로 지정
    req.add_header("X-NCP-APIGW-API-KEY-ID", client_id) # 경로 접근하기 위한 아이디 - naver에서 발급
    req.add_header("X-NCP-APIGW-API-KEY", client_secret) #경로 접근하기 위한 비밀번호 - naver에서 발급
    
    try:
        response = urllib.request.urlopen(req) # URL을 통해 데이터 요청해서 결과 받음
        if response.getcode() == 200: # 성공코드 : 200
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())
            return(response.read().decode('utf-8'))
    except Exception as ex: # 예외처리
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None


# 사전 준비 작업 및 분류(크롤링을 위한 url 생성)
def GetGoVSearchResult(endPoint, pageValue, perPageValue, keyValue) :
    paraData = "page=" + str(pageValue)
    paraData += "&perPage=" + str(perPageValue)
    # paraData에 문자형식으로 pageValue, perPageValue 저장

    url = endPoint + paraData + keyValue # url 생성

    resultData = Get_Request_Url(url)
    # resultData = Get_Request_Url 함수에서 크롤링해온 데이터

    if(resultData == None):
        return None
    else:
        return json.loads(resultData)
    # resultData파일 json파일 형식으로 리턴

# 위도/경도 값 출력을 위한 사전 준비 작업
def GetGeoLocationData(addr):
        paraData = "?query=%s" % urllib.parse.quote(addr)
        resulturl = baseUrl + paraData
        resultData = Get_Request_Url(resulturl)
        if(resultData == None):
            return None
        else: 
            return json.loads(resultData)