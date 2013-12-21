#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json, re
import urllib, urllib2

def IndexHandler(request):
    return HttpResponse('Hello World! I am IndexHandler!')
	
	
def TypeHandler(request):
    return HttpResponse('Hello World! I am TypeHandler!')
	
def SearchHandler(request):
    searchUrl = 'http://soso.music.qq.com/fcgi-bin/music_search_new_platform'
    getDataDict = {
        'format': 'jsonp',
        'inCharset': 'GB2312',
        'outCharset': 'UTF-8',
        'w': request.GET.get('keyword', '').encode('utf-8'),
        'p': request.GET.get('p', '1').encode('utf-8'),
    }
    params = urllib.urlencode(getDataDict)
    req = urllib2.Request('%s?%s' % (searchUrl, params), None)
    returnRawJson = urllib2.urlopen(req).read()
    cleanJson = re.match('MusicJsonCallback(.*)', returnRawJson)
    cleanJson = json.loads(cleanJson.group(1).strip('()'))

    statusCode = cleanJson['code']
    statusMess = cleanJson['message']
    if not statusCode == 0: return HttpResponse(json.dumps({
        'code': statusCode,
        'message': statusMess,
    })) #RETURN ERROR

    pageCount = cleanJson['data']['song']['curpage']
    musicList = cleanJson['data']['song']['list']

    return HttpResponse(json.dumps({
        'list': [{
            'musicTitle': musicItem['fsong'],
            'musicID': re.split('[@|]{1,2}', musicItem['f'])[0],
            'singer': musicItem['fsinger'],
            'singerImg': '',
            'album': re.split('[@|]{1,2}', musicItem['f'])[5],
            'albumImg': '',
        } for musicItem in musicList],
        'code': 0,
        'message': statusMess,
        'type': 'anime',
    }))
        