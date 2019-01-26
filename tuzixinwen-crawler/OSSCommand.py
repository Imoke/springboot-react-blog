#!/usr/bin/python
# -*- coding:UTF-8 -*-
# Author: wangmiansen
# Date: 2018-12-14

import oss2
import requests
import datetime
import time
import configparser
from Logger import *

logger = Logger()
conf = configparser.ConfigParser()
conf.read('application.cfg')

class OSSCommand(object):

    def __init__(self):
        self.AccessKeyId = conf.get('oss', 'AccessKeyId')
        self.AccessKeySecret = conf.get('oss', 'AccessKeySecret')
        self.Endpoint = conf.get('oss', 'Endpoint')
        self.BucketName = conf.get('oss', 'BucketName')

    # 连接OSS
    def connectOSS(self):
        try:
            auth = oss2.Auth(self.AccessKeyId, self.AccessKeySecret)
            self.bucket = oss2.Bucket(auth, self.Endpoint, self.BucketName)
        except Exception as e:
            logger.getErrorLog('OSSCommand-upload-上传OSS失败,原因：%s' % (e))

    # 上传
    def upload(self,url,objectName):
        try:
            try:
                input = requests.get(url)
            except Exception as e:
                logger.getErrorLog('OSSCommand-upload-读取链接失败,原因：%s'%(e))
            self.bucket.put_object(objectName,input)
            logger.getDebugLog('OSSCommand-upload-上传OSS成功')
        except Exception as e:
            logger.getErrorLog('OSSCommand-upload-上传OSS失败,原因：%s' % (e))

if __name__ == '__main__':
    oSSCommand = OSSCommand()
    oSSCommand.connectOSS()
    url = "https://img.huxiucdn.com/article/cover/201812/13/071817172246.jpg?imageView2/1/w/710/h/400/|imageMogr2/strip/interlace/1/quality/85/format/jpg"
    objectName = 'images/article/%s/%s.jpg' % (datetime.datetime.now().strftime('%Y/%m/%d'),int(round(time.time()*1000)))
    user_avatar = 'images/user/%s/%s.jpg' % (datetime.datetime.now().strftime('%Y/%m/%d'),int(round(time.time()*1000)))
    oSSCommand.upload(url,objectName)
    oSSCommand.upload(url,user_avatar)
    print(objectName)