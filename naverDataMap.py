import urllib.request
import datetime
import json
import folium
# from config import * #(실무에서는 최종 버전을 만들기 전까지 개발과정에서 다시 사용될 수 있으므로 주석 처리)

client_id = "5l5yadvenl"
client_secret = "ygf36whrwrx4XQGFoGaepijGIrvEdHWIvgCgnmF8"

def get_request_url(url): # 데이터 요청하여 가져오기 - 크럴러 작업
    req = urllib.request.Request(url) #검색 URL 경로 지정
    req.add_header("X-NCP-APIGW-API-KEY-ID", client_id) # 경로 접근하기 위한 아이디 - naver에서 발급
    req.add_header("X-NCP-APIGW-API-KEY", client_secret) #경로 접근하기 위한 비밀번호 - naver에서 발급

    try:
        response = urllib.request.urlopen(req) # URL을 통해 데이터 요청해서 결과 받음
        if response.getcode() == 200: # 200 코드 번호면 성공 400/500 은 Naver 문서에서 확인
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())    
            return response.read().decode('utf-8')
    except Exception as ex:
        print(ex)
        #print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None
        


def GetGeoLocationData(addr):
        baseUrl = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode" #지오
        # baseUrl = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"
        # ?w=300&h=300&center=127.1054221,37.3591614&level=16
        paraData = "?query=%s" % urllib.parse.quote(addr)
        resulturl = baseUrl + paraData

        resultData = get_request_url(resulturl)

        if(resultData == None):
            return None
        
        tempData = json.loads(resultData)
        # 정제 - JSON 파일 분석 후 데이터 찾기 - 위도 / 경도 값
        if 'addresses' in tempData.keys():
            xdata = tempData['addresses'][0]['x']
            ydata = tempData['addresses'][0]['y']
            return [ydata, xdata]

def Main():
    addrData = GetGeoLocationData('팔달구 권광로 373')
    tip = '병원'
    map_data = folium.Map(location=addrData, zoom_start=15)
    map_data = folium.Marker(addrData, popup='확인', tooltip=tip).add_to(map_data)
    map_data.save(r'c:\temp\navermap.html')
    # 다른 방법 Naver API 를 이용한 Naver Map 사용(Static Map)

if __name__ == '__main__':
    Main()