# requests에서 한글 깨짐 
'''
웹을 호출할 때 간혹 한글이 깨지는 경우가 있는데 해결방법은 Response의 인코딩 속성을 변경하면 된다.
requests에서 웹 호출을 했을 때 Response 객체에 호출 결과가 담기는데, Response의 text 속성은 str 타입이기 때문에
requests 모듈에서 자동 인코딩을 해준다. 즉, requests는 인코딩 방식을 추측하여 Response 객체의 인코딩 속성 값을
지정하고, text 속성을 엑세스 할 때 인코딩 속성을 사용하는 것이다. 

korearace 사이트는 ISO-8859-1(영어를 포함한 많은 외국어 한글은 포함이 안됨)을 사용하고 있어서 한글이 깨진다.
이때는 test 속성을 읽기 전에 Response의 인코딩 속성을 변경하면 된다.
한글 인코딩(euc-kr)을 Response 객체에 미리 지정한 후 text 속성을 읽으면 된다.
'''

import requests
 
resp = requests.get('http://www.korearace.com/Iframe/loginMain.asp') # korearace 사이트를 읽어드린다.
resp.raise_for_status() # Response 에서 오류가 발생하면 프로그램을 중단 시킨다.

print(resp.encoding) # 어떤 인코딩이 쓰이고 있는지 출력한다.

resp.encoding='euc-kr' # 인코딩을 euc-kr로 변환하여 한글 인코딩으로 변환하여 한글이 안깨지게 한다.

# print(resp.encoding) # 어떤 인코딩이 쓰이고 있는지 출력한다.
print(resp.text) # Response 데이터를 문자열로 읽어드린다.













