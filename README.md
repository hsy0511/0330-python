# 0330-python
# 파이썬 Web Scraping
Web Scraping은 웹사이트에서 html을 읽어와 필요한 데이터를 긁어 온다

Web Scraping은 크게 웹페이지를 읽어오는 것과
읽어온 html 문서에서 필요한 데이터만 뽑아내는 과정으로 나눌 수 있다.
## http에서 get, post, put, delete 의미
![image](https://user-images.githubusercontent.com/104752580/228726740-e6a34c1a-502a-41e9-a47c-f4d82cc71d45.png)
###### ※ idempotent : 연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질을 의미한다.
## requests - 웹페이지 읽어오기

Web Scraping을 사용하기 위해서는 requests 패키지를 다운받아야 한다.
```
pip install requests
```

requests.get, requests.post, requests.put, requests.delete 사용하여 인코딩 기능을 제공한다.

데이터를 딕셔너리로 만들어 사용하면 Requests에서 자동 인코딩 해준다.

데이터가 정상적으로 읽어 들어오면 Response 객체에서 200을 리턴한다.

requests.get(url)을 사용하면 해당 웹페이지 호출 결과를 가진 Response 객체를 가진다.
###### ※ Response은 응답 즉, 전달받은 것을 의미한다.
### 예제 1
```python
import requests

resp = requests.get('http://httpbin.org/get') # 문자열로 데이터를 읽어옴
print(resp.text)
resp = requests.put('http://httpbin.org/put') # <Response [200]>
print(resp)
resp = requests.delete('http://httpbin.org/delete') # <Response [200]>
print(resp)
dic = {"id": 1, "name": "Kim", "age": 10}
resp = requests.post('http://httpbin.org/post', data=dic) # 데이터를 딕셔너리로 자동 인코딩 해줌
print(resp.text)
```
![image](https://user-images.githubusercontent.com/104752580/228740415-20fbc580-c4b6-4f3b-82f8-8b20230a7e08.png)

## Response와 관련된 속성
status_code 속성은 http status 결과를 체크한다.

text는 Response 데이터를 문자열로 리턴한다.

content는 Response 데이터를 바이트로 리턴한다.

raise_for_status() 메서드는 Response 에서 오류가 발생하면 호출하여 프로그램을 중단 시킨다.

### 예제 2
```python
resp = requests.get( 'http://daum.net' )

if (resp.status_code == requests.codes.ok): 
    html = resp.text # resp.status_code 가 정상적으로 실행됐을 때 데이터를 문자열로 리턴한다.
    html = resp.content # resp.status_code 가 정상적으로 실행됐을 때 데이터를 바이트로 리턴한다.
    print(html)
```
![image](https://user-images.githubusercontent.com/104752580/228740214-ba851e52-036a-4233-be01-dd15e44b77ea.png)

## 한글 깨짐
웹을 호출할 때 간혹 한글이 깨지는 경우가 있는데 해결방법은 Response의 인코딩 속성을 변경하면 된다.

requests에서 웹 호출을 했을 때 Response 객체에 호출 결과가 담기는데, Response의 text 속성은 str 타입이기 때문에

requests 모듈에서 자동 인코딩을 해준다. 즉, requests는 인코딩 방식을 추측하여 Response 객체의 인코딩 속성 값을

지정하고, text 속성을 엑세스 할 때 인코딩 속성을 사용하는 것이다. 
### 예제 3
```python 
import requests
 
resp = requests.get('http://www.korearace.com/Iframe/loginMain.asp') # korearace 사이트를 읽어드린다.
resp.raise_for_status() # Response 에서 오류가 발생하면 프로그램을 중단 시킨다.

print(resp.encoding) # 어떤 인코딩이 쓰이고 있는지 출력한다.

resp.encoding='euc-kr' # 인코딩을 euc-kr로 변환하여 한글 인코딩으로 변환하여 한글이 안깨지게 한다.

print(resp.encoding) # 어떤 인코딩이 쓰이고 있는지 출력한다.
print(resp.text) # Response 데이터를 문자열로 읽어드린다.
```
![image](https://user-images.githubusercontent.com/104752580/228740069-3fdad3eb-bde7-4407-ad8c-b0fe2026021d.png)

korearace 사이트는 ISO-8859-1(영어를 포함한 많은 외국어 한글은 포함이 안됨)을 사용하고 있어서 한글이 깨진다.

이때는 test 속성을 읽기 전에 Response의 인코딩 속성을 변경하면 된다.

한글 인코딩(euc-kr)을 Response 객체에 미리 지정한 후 text 속성을 읽으면 된다.
## BeautifulSoup 웹페이지 파싱
웹 페이지를 파싱하기 위해서는 BeautifulSoup 모듈을 다운로드 받고 사용해야 한다.

BeautifulSoup 모듈을 import 해야되는데 여기서 BeautifulSoup 모듈명은 bs4이다.

import 완료 후에는 bs4.BeautifulSoup 생성자를 호출하여  BeautifulSoup 객체를 생성한다.
```python
import bs4
 
html = "url"
bs = bs4.BeautifulSoup(html, 'html.parser') # 응답받은 HTML 내용을 BeautifulSoup 클래스의 객체 형태로 반환합니다
print(bs)
```

### 예제 4
```python
# -*- coding: utf-8 -*- 
# 파이썬 2에서는 기본 인코딩이 ascii 라서 한글을 디코딩할 수 없어서 한글 등 utf-8로 인코딩 해주어야 할 때 명시해 준다.
(ascii는 알파벳을 사용하는 대표적인 문자 인코딩이다)
# 파이썬 3에서는 기본 인코딩이 utf-8 라서 기본적으로 해주지 않아도 된다.

import requests, bs4
 
resp = requests.get('http://naver.com/') # 네이버 홈페이지를 읽어드린다.
resp.raise_for_status() # Response에서 오류가 발생하면 프로그램을 중지시킨다.
html = resp.text # response 데이터를 문자열로 변환한다.
 
bs = bs4.BeautifulSoup(html, 'html.parser') # 응답받은 HTML 내용을 BeautifulSoup 클래스의 객체 형태로 변환한다.
tags = bs.select('#header > div.special_bg > div > div.logo_area > h1 > a') # 특정한 css태그를 selector로 찾아서 긁어온다.
title = tags[0].getText() # 인덱스 0번째 있는 값을 문자열로 리턴한다.
print(title) # 문자열로 리턴한 데이터를 출력한다.
```
![image](https://user-images.githubusercontent.com/104752580/228739918-b72b3fd9-cf27-4e7e-8183-131c184cb3de.png)

select() 메서드는 Beautifulsoup 객체에서 특정 html 태그를 찾기 위해서 사용한다.
(select() 메서드의 파라미터는 css 태그에서 selector로 지정하면된다 )

이때 select() 메서드에서 리턴된 결과는 리스트인데 리턴된 리스트를 문자열로 리턴하기 위해서는 getText()를 사용하고,
특정 태그 값만 리턴 하고 싶을때는 get을 사용한다.
