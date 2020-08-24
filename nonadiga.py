import requests
import requests

url = "http://adiga.kr/kcue/ast/eip/eis/inf/selctninf/EipSelctnInfGnrlList.do?p_menu_id=undefined"

payload = 'chk_rcrr=20&chk_slcty=04&cur_year=2021&dgnss_at=Y&dtl_rcbkSerch=N&dtl_serch=N&lst_lgcl_cd=&lst_mdcl_cd=&lst_smcl_cd=&pageIndex=1&pageSize=15&sch_year=2021&sel_area=&sel_rcrr=20&sel_selctn_nm=&sel_slcty=04&sers=&this_sch_year=2021&univ_sort=UP&uv_type=on'
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

response = requests.request("POST", url, headers=headers, data = payload)

import json
response_json = json.loads(response.text.encode('utf8'))
print(response_json)


# print(response.text.encode('utf8'))     여기 이거 대신 여진님이 올려주시는 코드를 대신 쓸것



# from bs4 import BeautifulSoup
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# form = {
#     'pageIndex': 1,         #pageIndex=1
#     'pageSize': 15,
#     'dtl_serch': 'N',
#     'dtl_rcbkSerch': 'N',
#     'sel_slcty': '04',
#     'univ_se_cd': '10',
#     'univ_sort': 'UP',
#     'dgnss_at': 'Y',
#     'sch_year': '2021',
#     'this_sch_year': '2021',
#     'cur_year': '2021',
#     'chk_slcty': '04',
#     'chk_search_area': 'all',
#
#
# &pageSize=15&dtl_serch=N&dtl_rcbkSerch=N&sel_rcrr=20&sel_area=&sel_sers=&sel_slcty=04&sel_selctn_nm=&cho_area=&cho_univ=&btn_list_sort=&lm_cd=&univ_cd=&rcu_cd=&send_searchKeyword=&univ_se_cd=10&stdr_sch_year=&lst_rcrr_cd=&lst_slcty_cd=&lst_selctn_nm_cd=&lst_area_cd=&univ_sort=UP&area_sort=&lst_lgcl_grp=&lst_mdcl_grp=&lst_smcl_grp=&lst_subjct_grp=&send_sch_year=&send_univ_cd=&send_rcrr_cd=&send_selctn_grp_cd=&send_rcu_sn=&send_rcu_cd=&send_sers_cd=&send_csat_imtexm=&dgnss_at=Y&sch_year=2021&this_sch_year=2021&bfyr_at=&send_univ_nm=&subjct_keyword=&univ_keyword=&main_search_at=&gnrlKeyword=&area=&sers=&rcrr=20&cur_year=2021&searchUnivKeyword=&chk_rcrr=20&chk_slcty=04&chk_selctnNm=&chk_area=&searchKeyword=&lst_lgcl_cd=&lst_mdcl_cd=&lst_smcl_cd=&chk_search_area=all&sel_csat_imtexm=
#
#
# }
# data = requests.post(
#     'http://adiga.kr/kcue/ast/eip/eis/inf/selctninf/EipSelctnInfGnrlList.do?p_menu_id=undefined',
#     headers=headers,
#     json=form,
# )
# print(data)
# response_json = data.json()  # 응답 JSON을 딕셔너리로 저장
# print(response_json)
# #
# soup = BeautifulSoup(data.text, 'html.parser')
#
# trs = soup.select('#tbResult > tr')
#
# for tr in trs:
# 	university = tr.select_one( '#tr > td > a')
#     major = tr.select_one( ' '  )
#     persons
#     c_rate
#
# 	print(university.text)