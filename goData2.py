#공공 데이터 가져오기 (godata.go.kr)

import urllib.request
import datetime
import json
import pandas as pd

def Get_Request_Url(url): # 크롤러를 담당하는 부분
    req = urllib.request.Request(url) #검색 URL 경로 지정    
    # https://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=10    
    # serviceKey=spm%2FxLr97h3BZnQQDuIKw4ESJIOX%2F7z%2F8eCDjDXmcSsOQuws8vDlflhHCtm0fXLeptDUkt39rPoI945V%2FCbEPw%3D%3D
    try:
        response = urllib.request.urlopen(req) # URL을 통해 데이터 요청해서 결과 받음
        if response.getcode() == 200: # 200 코드 번호면 성공 400/500 은 Naver 문서에서 확인
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())    
            return response.read().decode('utf-8')
    except Exception as ex:
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None

def GetGoVSearchResult(pageValue, perPageValue): # 사전 준비 작업 및 분류   
    endPoint = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    #paraData1 = "page=" + pageValue
    #paraData2 = "&perPage=" + perPageValue
    paraData = "page=" + str(pageValue)
    paraData += "&perPage=" + str(perPageValue)
    keyValue = "&serviceKey=spm%2FxLr97h3BZnQQDuIKw4ESJIOX%2F7z%2F8eCDjDXmcSsOQuws8vDlflhHCtm0fXLeptDUkt39rPoI945V%2FCbEPw%3D%3D"

    url = endPoint+ paraData + keyValue

    resultData = Get_Request_Url(url)

    if(resultData == None):
        return None
    else:
        tempData = json.loads(resultData)

        # json 파일을 DataFrame으로 변환
        tempData_df = pd.DataFrame(tempData['data'])

        # 키 값으로 주소/센터명/번호 값 추출
        h_result = tempData_df[['orgZipaddr','orgnm','orgTlno']]

        return (h_result)

def GetGoVSearchResult2(pageValue, perPageValue): # 사전 준비 작업 및 분류   
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    #paraData1 = "page=" + pageValue
    #paraData2 = "&perPage=" + perPageValue
    paraData = "page=" + str(pageValue)
    paraData += "&perPage=" + str(perPageValue)
    keyValue = "&serviceKey=spm%2FxLr97h3BZnQQDuIKw4ESJIOX%2F7z%2F8eCDjDXmcSsOQuws8vDlflhHCtm0fXLeptDUkt39rPoI945V%2FCbEPw%3D%3D"

    url = endPoint+ paraData + keyValue

    resultData = Get_Request_Url(url)

    if(resultData == None):
        return None
    else:
        tempData = json.loads(resultData)

        # json 파일을 DataFrame으로 변환
        tempData_df = pd.DataFrame(tempData['data'])

        # 키 값으로 주소/센터명/번호 값 추출
        h_result = tempData_df[['address','centerName','phoneNumber']]

        return (h_result)

def Main():
    pageData = 1
    perPageData = 20 # 50  ~ 100

    jsonSearchResult = GetGoVSearchResult(pageData, perPageData)
    jsonSearchResult2 = GetGoVSearchResult2(pageData, perPageData)

    print(jsonSearchResult)
    print(jsonSearchResult2)

if __name__ == '__main__':
    Main()