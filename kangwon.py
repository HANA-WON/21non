import requests

url = "http://adiga.kr/kcue/ast/eip/eis/inf/selctninf/EipSelctnInfGnrlList.do?p_menu_id=undefined"

payload = 'area=&area_sort=&bfyr_at=&btn_list_sort=&chk_area=&chk_rcrr=20&chk_search_area=09&chk_selctnNm=&chk_slcty=04&cho_area=09&cho_univ=&cur_year=2021&dgnss_at=Y&dtl_rcbkSerch=N&dtl_serch=N&gnrlKeyword=&lm_cd=&lst_area_cd=&lst_lgcl_cd=&lst_lgcl_grp=&lst_mdcl_cd=&lst_mdcl_grp=&lst_rcrr_cd=&lst_selctn_nm_cd=&lst_slcty_cd=&lst_smcl_cd=&lst_smcl_grp=&lst_subjct_grp=&main_search_at=&pageIndex=1&pageSize=15&rcrr=20&rcu_cd=&sch_year=2021&searchKeyword=&searchUnivKeyword=&sel_area=&sel_csat_imtexm=&sel_rcrr=20&sel_selctn_nm=&sel_sers=&sel_slcty=04&send_csat_imtexm=&send_rcrr_cd=&send_rcu_cd=&send_rcu_sn=&send_sch_year=&send_searchKeyword=&send_selctn_grp_cd=&send_sers_cd=&send_univ_cd=&send_univ_nm=&sers=&stdr_sch_year=&subjct_keyword=&this_sch_year=2021&univ_cd=&univ_keyword=&univ_se_cd=10&univ_sort=UP&uv_type=on'
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': 'WMONID=5z4Xp_Jx2F3; JSESSIONID=K3l6s8dIEQHKhj70XaXEEeHJkY9n2133FZlOOomr0GS1yjacVQqnJcDewt0Jb5hO.amV1c19kb21haW4vbXM0'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
