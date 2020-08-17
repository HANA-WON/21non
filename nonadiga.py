import requests
from bs4 import BeautifulSoup
# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        ###키:밸류 모양의 딕셔너리/ 'User-Agent'는 이름표로 위조하는거야. 모질라.. 로 시작하는 밸류는 크롬을 의미하는거야. 즉 이 라인은 크롬이야!라는 이름표.
data = requests.get('http://adiga.kr/PageLinkAll.do?link=/kcue/ast/eip/eis/inf/selctninf/EipSelctnInfGnrl.do&p_menu_id=PG-EIP-06001', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

newstitle = soup.select('#tbSelctnInfList > tbresult > tr')
for title in newstitle:
    ntitle = title.select_one('tt > a')
    print(ntitle.text)