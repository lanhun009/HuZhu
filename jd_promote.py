#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_promote
活动名称: 热爱奇旅
Author: SheYu09
cron: 0 1,3,5,7,8,9,10,11,13,15,16,17,19,20,21,23 * * * jd_promote.py
new Env('京东 -*- 热爱奇旅')
'''
import os
from GetJDUser import *
s.headers['User-Agent'] = userAgent()
requests.packages.urllib3.disable_warnings()

def re_es():
	exit() if len(es) == 1 else es.remove(es[0])

def JD_API_PARAMS():
	s.params = {
		'functionId': '',
		'client': 'm',
		'clientVersion': -1,
		'appid': 'signed_wh5',
		'body': {}
	}
	s.headers['Referer'] = 'https://wbbny.m.jd.com/'

def JD_API_MONGO_PARAMS():
	s.params = {
		'appid': 'wh5',
		'functionId': '',
		'clientVersion': '1.0.0',
		'body': {}
	}
	s.headers['Referer'] = 'https://h5.m.jd.com/'

def JD_API_BODY(e, t, p):
	g = log()
	s.body = {
		'taskId': t,
		'taskToken': e,
		'actionType': 1,
		'ss': dumps({
			'extraData': {
				'log': g['log'],
				'sceneid': 'RAhomePageh5'
			},
			'secretp': p,
			'random': g['random']
		})
	}

def JD_API_PK_BODY(p, e=False):
	g = log()
	s.body = {
		'ss': dumps({
			'extraData': {
				'log': g['log'],
				'sceneid': e and 'RAZXh5' or 'RAhomePageh5'
			},
			'secretp': p,
			'random': g['random']
		}, separators=(',', ':')),
	}

def JD_API_MONGO_BODY(e=False):
	g = log()
	s.body = {
		'taskToken': '',
		e and 'taskId' or 'actId': ''.join(sample(string.ascii_letters+string.digits, 32)),
		'appId': '1GVRR' + '{2}'.format(*tnm()).split('&')[0].lower(),
		e and 'actionType' or 'channelId': e and 0 or 1,
	}
	if e: s.body['safeStr'] = dumps({
		'random': g['random'],
		'sceneid': 'RAGJSYh5',
		'log': g['log']
	})

class Scripts(object):
	def __enter__(self):
		r = s.post('https://api.m.jd.com/client.action', verify=False)
		return r.json() if r.content else ''

	def __exit__(self, exc_type, exc_val, exc_tb):
		return True 

def JD_API_HOST():
	with Scripts() as e:
		return e

def promote_sign(p):
	JD_API_PARAMS()
	JD_API_PK_BODY(p)
	s.params['functionId'] = stack()[0][3]
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	e = JD_API_HOST()
	if e['data']['success']:
		print('签到成功,获得' + re_key("'score': '(.*?)'", str(e)) + '金币', '\n')
	else:
		print('签到失败\n')

def getBadgeAward(e):
	JD_API_PARAMS()
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.params['body'] = dumps({
		'awardToken': e
	}, separators=(',', ':'))
	e = JD_API_HOST()
	print('开启宝箱,获得' + re_key("'score': '(.*?)'", str(e)) + '金币', '\n')

def collectScore(e, t, p):
	JD_API_PARAMS()
	JD_API_BODY(e, t, p)
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	e = JD_API_HOST()
	print(e['data']['bizMsg'], '\n')
	sleep(s.t)

def queryVkComponent(e):
	s.params = {
		'functionId': stack()[0][3],
		'client': 'wh5',
		'body': dumps({
			'businessId': 'babel',
			'componentId': '0d216ebae59b400182162fda7cdfa996',
			'taskParam': dumps({
				'biz': 'babel',
				'taskToken': e
			}, separators=(',', ':')),
			'businessId': 'shop'
		}, separators=(',', ':'))
	}
	e = JD_API_HOST()
	try: print(e['msg'], '\n')
	except: print(e, '\n')

def qryViewkitCallbackResult(e):
	s.params = {
		'functionId': stack()[0][3],
		'client': 'wh5',
		'body': dumps({
			'dataSource': 'newshortAward',
			'method': 'getTaskAward',
			'reqParams': dumps({
				'taskToken': e
			}, separators=(',', ':'))
		}, separators=(',', ':'))
	}
	print(JD_API_HOST()['toast']['subTitle'], '\n')
	sleep(s.t)

def getFeedDetail(e):
	JD_API_PARAMS()
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.params['body'] = dumps({
		'taskId': e
	}, separators=(',', ':'))
	e = JD_API_HOST()
	try:
		return e['data']['result']['addProductVos'][0]['productInfoVos']
	except:
		try:
			return e['data']['result']['taskVos'][0]['browseShopVo']
		except:
			print('未知错误...\n')

def bindWithVender(e, t):
	s.params = {
		'appid': 'jd_shop_member',
		'functionId': stack()[0][3],
		'body': dumps({
			'venderId': t,
			**e,
			'bindByVerifyCodeFlag': 1
		}, separators=(',', ':'))
	}
	r = JD_API_HOST()
	print(r['message'], '\n')

def promote_raise(p):
	JD_API_PARAMS()
	JD_API_PK_BODY(p)
	s.params['functionId'] = stack()[0][3]
	s.body['scenceId'] = 3
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	e = JD_API_HOST()['data']['success']
	if e: print('升级成功\n')
	return e

def getHomeData(i):
	s.headers['Cookie'] = i
	if GetJDUser(): return
	print(f"开始【京东账号{ckList.index(i)+1}】{s.userLevel}级 {s.levelName}: {s.nickName}\n")
	JD_API_PARAMS()
	s.params['functionId'] = 'promote_' + stack()[0][3]
	try:
		secretp = JD_API_HOST()['data']['result']['homeMainInfo']['secretp']
		print(secretp, '\n')
		return secretp
	except:
		print('黑号了...\n')
		return False

def getTaskDetail(i):
	p = getHomeData(i)
	if not p: return
	if localtime().tm_hour == 10:
		promote_sign(p)
	T = True
	while T:
		T = False
		JD_API_PARAMS()
		s.params['functionId'] = 'promote_' + stack()[0][3]
		e = JD_API_HOST()
		for i in e['data']['result']['lotteryTaskVos'][0]['badgeAwardVos']:
			if i['status'] == 3:
				getBadgeAward(i['awardToken'])
		for i in e['data']['result']['taskVos']:
			if i['status'] == 2: continue
			t = i['taskId']
			if i['taskType'] in [3, 6, 7, 9, 26]:
				if i['taskType'] == 7:
					v = 'browseShopVo'
				else:
					v = 'shoppingActivityVos'
				for u in i[v]:
					try:
						print(u['title'], '\n')
					except:
						try:
							print(u['shopName'], '\n')
						except:
							print(u['adRemark'], '\n') # adRemark
					if u['status'] == 1:
						T = True
						collectScore(u['taskToken'], t, p)
						queryVkComponent(u['taskToken'])
				if i['taskType'] not in [3, 26]:
					sleep(10)
					for i in i[v]:
						if i['status'] == 1:
							T = True
							qryViewkitCallbackResult(i['taskToken'])
			elif i['taskType'] == 0:
				if i['status'] != 2:
					if t == 31:
						JD_API_PARAMS()
						s.params['functionId'] = 'promote_pk_getHomeData'
						print(JD_API_HOST()['msg'], '\n')
					print(i['taskName'], '\n')
					T = True
					collectScore(i['simpleRecordInfoVo']['taskToken'], t, p)
			elif i['taskType'] in [2, 5]:
				u = 1
				for i in getFeedDetail(i['taskId']):
					if i['status'] == 1:
						try:
							print('加购', i['skuName'], '\n')
						except:
							print(i['adRemark'], '\n')
						T = True
						collectScore(i['taskToken'], t, p)
						if u >= 4: break
						u += 1
			elif i['taskType'] in [21]:
				for u in i['brandMemberVos']:
					if u['status'] == 1:
						print(u['title'], '\n')
						T = True
						bindWithVender(u['ext'], u['vendorIds'])
				for i in i['brandMemberVos']:
					if i['status'] == 1:
						T = True
						collectScore(i['taskToken'], t, p)
	while promote_raise(p):
		promote_raise(p)
	JD_API_PARAMS()
	s.params['functionId'] = 'promote_' + stack()[0][3]
	e = JD_API_HOST()['data']['result']
	et = e['taskVos'][0]
	if et['status'] == 1 and et['taskType'] == 14:
		i = e['inviteId']
		print('助力码:', i, '\n')
		es.append(i)

def promote_collectScore(i):
	p = getHomeData(i)
	if not p: return
	JD_API_PARAMS()
	JD_API_PK_BODY(p)
	s.params['functionId'] = stack()[0][3]
	s.body['actionType'] = '0'
	s.body['inviteId'] = es[0]
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	e = JD_API_HOST()['data']['bizMsg']
	print(e, '\n')
	if '爆棚' in e:
		re_es()

def collectAutoScore(i):
	p = getHomeData(i)
	if not p: return
	JD_API_PARAMS()
	JD_API_PK_BODY(p)
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	e = JD_API_HOST()
	t = re_key("'produceScore': '(.*?)'", str(e))
	print('获得' + t + '金币', '\n') if t else print(e['data']['bizMsg'], '\n')

def pk_getMsgPopup():
	JD_API_PARAMS()
	s.params['functionId'] = 'promote_' + stack()[0][3]
	e = JD_API_HOST()['data']['bizMsg']
	print(e, '\n')
	if '火爆' in e:
		return True

def pk_getHomeData(i):
	s.headers['Cookie'] = i
	if GetJDUser(): return
	print(f"开始【京东账号{ckList.index(i)+1}】{s.userLevel}级 {s.levelName}: {s.nickName}\n")
	if pk_getMsgPopup(): return
	JD_API_PARAMS()
	s.params['functionId'] = 'promote_' + stack()[0][3]
	e = JD_API_HOST()
	if re_key("'groupNum': (.*?),", str(e)) != '30':
		groupJoinInviteId = re_key("'groupJoinInviteId': '(.*?)'", str(e))
		print(groupJoinInviteId, '\n')
		es.append(groupJoinInviteId)
	else:
		print('该团队已经满员了\n')

def pk_joinGroup(i):
	p = getHomeData(i)
	if not p: return
	JD_API_PARAMS()
	JD_API_PK_BODY(p, True)
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.body['inviteId'] = es[0]
	s.body['confirmFlag'] = 1
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	j = JD_API_HOST()['data']['bizMsg']
	print(j, '\n')
	if '满员' in j:
		re_es()

def pk_divideScores(p):
	JD_API_PARAMS()
	JD_API_PK_BODY(p, True)
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	print(JD_API_HOST()['data']['bizMsg'], '\n')

def pk_getAmountForecast():
	JD_API_PARAMS()
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	print(JD_API_HOST()['data']['bizMsg'], '\n')

def pk_getExpandDetail(i):
	p = getHomeData(i)
	if not p: return
	JD_API_PARAMS()
	JD_API_PK_BODY(p, True)
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	if '领取' in JD_API_HOST()['data']['bizMsg']: return
	pk_divideScores(p)
	pk_getAmountForecast()
	JD_API_PARAMS()
	JD_API_PK_BODY(p, True)
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	e = JD_API_HOST()
	if re_key("'status': (.*?),", str(e)) == '1': 
		inviteId = re_key("'inviteId': '(.*?)'", str(e))
		if inviteId:
			print(inviteId, '\n')
			es.append(inviteId)
	else:
		pk_receiveAward()

def pk_collectPkExpandScore(i):
	p = getHomeData(i)
	if not p: return
	JD_API_PARAMS()
	JD_API_PK_BODY(p, True)
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.body['inviteId'] = es[0]
	s.body['actionType'] = '0'
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	j = JD_API_HOST()['data']['bizMsg']
	print(j, '\n')
	if '足够' in j:
		pk_receiveAward()
		re_es()

def pk_receiveAward():
	JD_API_PARAMS()
	s.params['functionId'] = 'promote_' + stack()[0][3]
	e = JD_API_HOST()
	t = re_key("'value': '(.*?)'", str(e))
	if t:
		print('获得红包:', t, '\n')
	else:
		print(e['data']['bizMsg'])

def mongo_getHomeData(i):
	p = getHomeData(i)
	if not p: return
	JD_API_MONGO_PARAMS()
	JD_API_MONGO_BODY()
	s.params['functionId'] = 'promote_' + stack()[0][3]
	s.params['body'] = dumps(s.body, separators=(',', ':'))
	e = JD_API_HOST()
	for i in e['data']['result']['taskVos']:
		t = i['taskId']
		if i['taskType'] in [12] and i['status'] == 1:
			print(i['taskName'], '\n')

def start():
	global Names, ckList, es
	print("🔔热爱奇旅, 开始!\n")
	s.t = 0.1
	es = list()
	Names = Name()
	ckList = jdCookie()
	s.name = split('[_.]', os.path.basename(__file__))
	if localtime().tm_hour == 8 and localtime().tm_min == 0:
		[pk_getHomeData(i) for i in [i for i in ckList if re_pin(i) in Names]]
		es and [pk_joinGroup(i) for i in ckList[10:]]
	elif localtime().tm_hour == 20 and localtime().tm_min == 0:
		[pk_getExpandDetail(i) for i in [i for i in ckList if re_pin(i) in Names]]
		es and [pk_collectPkExpandScore(i) for i in ckList[10:]]
	elif localtime().tm_hour in [10, 16] and localtime().tm_min == 0:
		[getTaskDetail(i) for i in [i for i in ckList if re_pin(i) in Names]]
		es and [promote_collectScore(i) for i in ckList[10:]]
	else:
		[collectAutoScore(i) for i in [i for i in ckList if re_pin(i) in Names]]

if __name__ == '__main__':
	start()