#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / USER_AGENTS
活动名称: User-agent
Author: SheYu09
'''
from uuid import uuid4
from time import time, sleep, localtime, strftime
from random import random, sample, randint, uniform

def userAgent():
	ios = f'10.{randint(0, 5)}.{randint(0, 5)}'
	uuid = ''.join((str(uuid4())+str(uuid4())).split('-'))[:40]
	iosVer = f'{randint(13, 15)}.{randint(0, 5)}.{randint(0, 5)}'
	iosV = iosVer.replace('.', '_')
	model = f'iPhone{randint(8, 13)},{randint(0, 4)}'
	appBuild = f'1680{randint(1, 99)}'
	return f"jdapp;iPhone;{ios};{iosVer};{uuid};M/5.0;appBuild/{appBuild};jdSupportDarkMode/0;lang/zh_CN;model/{model};addressid/{int(uniform(1,2)*1e8)};hasOCPay/0;hasUPPay/0;supportBestPay/0;pushNoticeIsOpen/1;pv/273.6;apprpd/;ref/JDLTSubMainPageViewController;psq/5;ads/;psn/{uuid}|{appBuild};jdv/0|iosapp|t_335139774|liteshare|Qqfriends|{int(time()*1e3)}|{int(time())+13};adk/;app_device/IOS;{model}|IOS|{iosVer}|{ios}|{appBuild}|{uuid}|a;Mozilla/5.0 (iPhone; CPU iPhone OS {iosV} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1;"
