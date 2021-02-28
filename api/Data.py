# -*- coding: utf-8 -*-
# @Author: zhazhafang
# @Blog: http://blog.zhazhafang.cn
import urllib.request,urllib.error,urllib.parse
import json
def download(access_token,dir_path=None,file_type=None,file_order=None,page=1,count=15):
    """
    获取部分个人信息
    :param access_token: 用户授权凭证
    :return:
    """
    url='https://openapi.yiban.cn/data/download'
    data = {
        "access_token":access_token,
        "dir_path":dir_path,
        "file_type":file_type,
        "file_order":file_order,
        "page":page,
        "count":count
    }
    url = "%s?%s" % (url, urllib.parse.urlencode(data))
    msg = None
    try:
        msg = urllib.request.urlopen(url).read()
    except urllib.request.HTTPError as e:
           # print e.code
        if e.code == 400:
            print("access_token 已过期")
            return msg
    msg = json.loads(msg)
    if msg['status']=='error':
        return msg
    return msg

def upload(access_token,file_name,file_tmp,share_type=None,share_content=None):
    """
    获取指定用户基本信息。

    """
    url = 'https://openapi.yiban.cn/data/uploadr'
    data = urllib.parse.urlencode({
        "access_token": access_token,
        "file_name":file_name,
        "file_tmp":file_tmp,
        "share_type":share_type,
        "share_content":share_content
    })
    url = "%s?%s" % (url, data)
    msg = None
    try:
        msg = urllib.request.urlopen(url).read()
    except urllib.request.HTTPError as e:
           # print e.code
        if e.code == 400:
            print("access_token 已过期")
            return msg
    msg = json.loads(msg)
    if msg['status']=='error':
        return msg
    return msg

class YibanException(Exception):
    def __init__(self, message):
        self.msg = message