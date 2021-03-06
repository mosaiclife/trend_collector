#-*- coding: utf-8 -*-
import re
import json

str = '''<script type="text/javascript">
var Test = [
{ "keyword":"a","type":"+","value":"34" }
, { "keyword":"b","type":"+","value":"88" }
, { "keyword":"c","type":"+","value":"38" }
, { "keyword":"d","type":"+","value":"6" }
, { "keyword":"e","type":"+","value":"9" }
, { "keyword":"f","type":"+","value":"9" }
, { "keyword":"g","type":"+","value":"140" }
, { "keyword":"h","type":"+","value":"21" }
, { "keyword":"i","type":"+","value":"8" }
, { "keyword":"j","type":"+","value":"4" }
];
var IssueObj = [
{ keyword:"이광섭",type:"+",value:"34" }
, { keyword:"블랙앤화이트스토리",type:"+",value:"88" }
, { keyword:"최두호",type:"+",value:"38" }
, { keyword:"박효신",type:"+",value:"6" }
, { keyword:"홍찬미",type:"+",value:"9" }
, { keyword:"이보영",type:"+",value:"9" }
, { keyword:"황선",type:"+",value:"140" }
, { keyword:"남태현",type:"+",value:"21" }
, { keyword:"경차유류세환급",type:"+",value:"8" }
, { keyword:"리디아고",type:"+",value:"4" }
];
var SisaIssueObj = [
{ keyword:"경기도 사회통합부지사",type:"new",value:"0" }
, { keyword:"박근혜 전주",type:"+",value:"1" }
, { keyword:"경차 유류세 환급방법",type:"+",value:"78" }
, { keyword:"누리과정 예산",type:"-",value:"-7" }
, { keyword:"익산택시기사 살인사건",type:"+",value:"1" }
, { keyword:"문재인 모병제",type:"+",value:"319" }
, { keyword:"연가 보상비",type:"new",value:"0" }
, { keyword:"차명거래금지법",type:"+",value:"17" }
, { keyword:"임각수 괴산군수",type:"new",value:"0" }
, { keyword:"전북 창조경제혁신센터",type:"new",value:"0" }
];
var EnterNewsObj = [
{ keyword:"이지연 이병헌",type:"new",value:"0" }
, { keyword:"k팝스타4",type:"-",value:"-2" }
, { keyword:"개그맨 이광섭",type:"+",value:"20" }
, { keyword:"송일국 세쌍둥이",type:"new",value:"0" }
, { keyword:"곽진언 하지원",type:"-",value:"-8" }
, { keyword:"김수현",type:"+",value:"34" }
, { keyword:"규현 쩍벌",type:"new",value:"0" }
, { keyword:"런닝맨 외계인",type:"+",value:"5" }
, { keyword:"강남 왕따",type:"new",value:"0" }
, { keyword:"k팝스타4 나하은",type:"new",value:"0" }
];
var SportsNewsObj = [
{ keyword:"양현종 포스팅",type:"new",value:"0" }
, { keyword:"최두호 보너스",type:"+",value:"336" }
, { keyword:"lpga 박인비",type:"+",value:"15" }
, { keyword:"박주영",type:"new",value:"0" }
, { keyword:"리디아 고 우승",type:"-",value:"-22" }
, { keyword:"강정호 포스팅 금액",type:"new",value:"0" }
, { keyword:"성남 우승",type:"+",value:"280" }
, { keyword:"김경언",type:"-",value:"-20" }
, { keyword:"김기태",type:"new",value:"0" }
, { keyword:"김동주",type:"+",value:"36" }
];'''


#values = re.findall(r'var Test.*?= \s*(.*?);', str, re.DOTALL | re.MULTILINE)
#print values[0]
#data = json.loads(values[0])
#print data[0]['keyword']
#print data[1]['keyword']
#print data[2]['keyword']

values = re.findall(r'var IssueObj.*?= \s*(.*?);', str, re.DOTALL | re.MULTILINE)
data = values[0]

data = re.sub(r'keyword:',' "keyword":',data)
data = re.sub(r'type:',' "type":',data)
data = re.sub(r'value:',' "value":',data)

print data

data = json.loads(data)


for i in data:
	print i['keyword']+' '+i['type']+' '+i['value']