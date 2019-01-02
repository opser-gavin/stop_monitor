#!/usr/bin/env python
#coding=utf-8

import urllib2
import urllib
import json
import sys
import time

localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def sendDingDingMessage(url, data):
        req = urllib2.Request(url)
        req.add_header("Content-Type", "application/json; charset=utf-8")
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = opener.open(req, json.dumps(data)).read()
        return response

urlport = sys.argv[1]
service = sys.argv[2]

if __name__ == '__main__':
        url = 'https://oapi.dingtalk.com/robot/send?access_token=c71b100e4184f5cf56cde402c8bf11ddf95a5a767a3e117634f72c723bb3004a'
	#url = 'https://oapi.dingtalk.com/robot/send?access_token=178bc431d76bb815d3d25bdbd0d48ad4ad62af67755c9307ba7ce1286a338d24'

        btns = [{"title": "关闭报警", "actionURL": "http://your.domain.com:7000/stop/%s/?service=%s" % (urlport,service)}]
                 #{"title": "重启服务", "actionURL": "https://www.domain.com"}]
        data = {"msgtype": "actionCard","actionCard":
                {"title": 'alert',
                 "text": "%s: < %s > is down ! [%s]" % (urlport,service,localtime),
                 "hideAvatar": 0,
                 "btnOrientation": 1,
                  "btns": btns
                 }
                }
        success = sendDingDingMessage(url,data)
        print(success)
