# json파일 합치기

import urllib.request
import datetime
import json

def Get_Request_Url(url): # 크롤러를 담당하는 부분
    req = urllib.request.Request(url) #검색 URL 경로 지정
    # https://api.odcloud.kr/api//15077586/v1/centers?page=1&perPage=10
    # &serviceeKey=wYSMgFdFROFGWeVY61sO%2FkEsOjQSVRIdOWKXyeFBXKMl0Xg3mr4LZ31GKCBjpRHU3joClHkaQGlhndG3uJX%2BBg%3D%3D
    try:
        response = urllib.request.urlopen(req) # URL을 통해 데이터 요청해서 결과 받음
        if response.getcode() == 200: # 200 코드 번호면 성공 400/500은 Naver 문서에서 확인 가능
            print("[%s] Url 요청 성공 : " % datetime.datetime.now())
            return(response.read().decode('utf-8'))
    except Exception as ex:
        print(ex)
        print("[%s] 오류 : %s " % datetime.datetime.now(), url)
        return None

def GetGoVSearchResult(pageValue, perPageValue) : # 사전 준비 작업 및 분류 #여기서는 두개 가져옴
    endPoint = "https://api.odcloud.kr/api/15077586/v1/centers?"
    #paraData1 = "page=" + str(pageValue) #문자열과 합치는거라 str처리해줌
    #paraData2 = "&perPage=" + str(perPageValue)
    paraData = "page=" + str(pageValue)
    paraData += "&perPage=" + str(perPageValue)
    keyValue = "&serviceKey=wYSMgFdFROFGWeVY61sO%2FkEsOjQSVRIdOWKXyeFBXKMl0Xg3mr4LZ31GKCBjpRHU3joClHkaQGlhndG3uJX%2BBg%3D%3D"

    url = endPoint + paraData + keyValue

    resultData = Get_Request_Url(url)

    if(resultData == None):
        return None
    else:
        return json.loads(resultData)

def GetGoVSearchResult2(pageValue, perPageValue) : # 사전 준비 작업 및 분류 #여기서는 두개 가져옴
    endPoint2 = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    #paraData1 = "page=" + str(pageValue) #문자열과 합치는거라 str처리해줌
    #paraData2 = "&perPage=" + str(perPageValue)
    paraData2 = "page=" + str(pageValue)
    paraData2 += "&perPage=" + str(perPageValue)
    keyValue2 = "&serviceKey=wYSMgFdFROFGWeVY61sO%2FkEsOjQSVRIdOWKXyeFBXKMl0Xg3mr4LZ31GKCBjpRHU3joClHkaQGlhndG3uJX%2BBg%3D%3D"

    url2 = endPoint2 + paraData2 + keyValue2

    resultData = Get_Request_Url(url2)

    if(resultData == None):
        return None
    else:
        return json.loads(resultData)

def Main():
    pageData = 1
    perPageData = 1000

    jsonSearchResult = GetGoVSearchResult(pageData, perPageData)
    jsonSearchResult2 = GetGoVSearchResult2(pageData, perPageData)


    with open('%s_GovData4_%s.json' % ('병원','데이터'), 'w', encoding='utf-8') as filedata:
        rJson = json.dumps((jsonSearchResult, jsonSearchResult2),
                            indent = 4,
                            sort_keys=True,
                            ensure_ascii=False)
        filedata.write(rJson)

    print('파일이름 : %s_GovData4_%s.json 저장완료' % ('병원', '데이터'))

if __name__ == '__main__':
    Main()
