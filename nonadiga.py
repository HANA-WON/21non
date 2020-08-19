import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('http://adiga.kr/PageLinkAll.do?link=/kcue/ast/eip/eis/inf/selctninf/EipSelctnInfGnrl.do&p_menu_id=PG-EIP-06001', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#tbResult > tr')

for tr in trs:
	university = tr.select_one( '#tr > td > a')
    major = tr.select_one( ' '  )
    persons
    c_rate

	print(university.text)
