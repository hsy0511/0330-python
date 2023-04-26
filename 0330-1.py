# 파이썬 web scraping
'''
Web Scraping은 웹사이트에서 html을 읽어와 필요한 데이터를 긁어 온다
Web Scraping은 크게 웹페이지를 읽어오는 것과
읽어온 html 문서에서 필요한 데이터만 뽑아내는 과정으로 나눌 수 있다.

'''

# Web Scraping을 사용하기 위해서는 requests 패키지를 다운받아야 한다.
# requests.get, requests.post, requests.put, requests.delete 사용하여 인코딩 기능을 제공한다.
# 데이터를 딕셔너리로 만들어 사용하면 requests에서 자동 인코딩 해준다.
# 데이터가 정상적으로 읽어 들어오면 response 객체에서 200을 리턴한다.
# requests.get(url)을 사용하면 해당 웹페이지 호출 결과를 가진 response 객체를 가진다.


import requests

'''resp = requests.get('http://httpbin.org/get') # 문자열로 데이터를 읽어옴
print(resp.text)'''
'''resp = requests.put('http://httpbin.org/put') # <Response [200]>
print(type(resp))'''
'''resp = requests.delete('http://httpbin.org/delete') # <Response [200]>
print(resp)
dic = {"id": 1, "name": "Kim", "age": 10}
resp = requests.post('http://httpbin.org/post', data=dic) # 데이터를 딕셔너리로 자동 인코딩 해줌
print(resp.text)'''





resp = requests.get( 'http://daum.net' )

if (resp.status_code == requests.codes.ok): 
    html = resp.text # resp.status_code 가 정상적으로 실행됐을 때 데이터를 문자열로 리턴한다.
    print(html)
    
'''
Response와 관련된 여러 속성
status_code 속성은 http status 결과를 체크한다.
text는 Response 데이터를 문자열로 리턴한다.
content는 Response 데이터를 바이트로 리턴한다.
'''
# Response 에서 오류가 발생하면 raise_for_status() 메서드를 호출하여 프로그램을 중단 시킨다.
