# BeautifulSoup 웹페이지 파싱
''' 
웹 페이지를 파싱하기 위해서는 BeautifulSoup 모듈을 다운로드 받고 사용해야 한다.
BeautifulSoup 모듈을 import 해야되는데 여기서 BeautifulSoup 모듈명은 bs4이다.
import 완료 후에는 bs4.BeautifulSoup 생성자를 호출하여  BeautifulSoup 객체를 생성한다.
'''
import bs4
 
html = "url"
bs = bs4.BeautifulSoup(html, 'html.parser') # 응답받은 HTML 내용을 BeautifulSoup 클래스의 객체 형태로 반환합니다
print(bs)

# 예제
# -*- coding: utf-8 -*- 
# 파이썬 2에서는 기본 인코딩이 ascii 라서 한글을 디코딩할 수 없어서 한글 등 utf-8로 인코딩 해주어야 할 때 명시해 준다.(ascii는 알파벳을 사용하는 대표적인 문자 인코딩이다)
# 파이썬 3에서는 기본 인코딩이 utf-8 라서 기본적으로 해주지 않아도 된다
 
import requests, bs4
 
resp = requests.get('http://naver.com/') # 네이버 홈페이지를 읽어드린다.
resp.raise_for_status() # Response에서 오류가 발생하면 프로그램을 중지시킨다.
html = resp.text # response 데이터를 문자열로 변환한다.
 
bs = bs4.BeautifulSoup(html, 'html.parser') # 응답받은 HTML 내용을 BeautifulSoup 클래스의 객체 형태로 변환한다.
tags = bs.select('#header > div.special_bg > div > div.logo_area > h1 > a') # 특정한 css태그를 selector로 찾아서 긁어온다.
title = tags[0].getText() # 인덱스 0번째 있는 값을 문자열로 리턴한다.
print(title) # 문자열로 리턴한 데이터를 출력한다.

'''
select() 메서드는 Beautifulsoup 객체에서 특정 html 태그를 찾기 위해서 사용한다.
(select() 메서드의 파라미터는 css 태그에서 selector로 지정하면된다 )
이때 select() 메서드에서 리턴된 결과는 리스트인데 리턴된 리스트를 문자열로 리턴하기 위해서는 getText()를 사용하고,
특정 태그 값만 리턴 하고 싶을때는 get을 사용한다.
'''