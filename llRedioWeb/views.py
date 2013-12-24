#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
import json, re
import urllib, urllib2

def IndexHandler(request):
    return render(request, 'llRedioWeb/index.html', None)
	
	
def TypeHandler(request):
    return HttpResponse('Hello World! I am TypeHandler!')
	
def MusicHandler(request):
    url = "http://ws.stream.qqmusic.qq.com/C200"
    vkey = "A430C496F97CC9BD1F901A5F17087E09A0BF9A77370AC40B882B6B82214E3A6D"
    guid = "950085250"
    return HttpResponse(json.dumps({
        "code": 0,
        "url": "%s%s.m4a?vkey=%s&guid=%s" % (url, request.GET.get('musicMid', ''), vkey, guid)
    }))
	
def SearchHandler(request):
    searchUrl = 'http://soso.music.qq.com/fcgi-bin/music_search_new_platform'
    singImgUrl = 'http://imgcache.qq.com/music/photo/mid_singer_300/%s/%s/%s.jpg'
    getDataDict = {
        'format': 'jsonp',
        'inCharset': 'GB2312',
        'outCharset': 'UTF-8',
        'w': request.GET.get('keyword', '').encode('utf-8'),
        'p': request.GET.get('p', '1').encode('utf-8'),
    }
    params = urllib.urlencode(getDataDict)
    #print params
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
            'musicMid':  re.split('[@|]{1,2}', musicItem['f'])[-3],
            'singer': musicItem['fsinger'],
            'singerImg': singImgUrl % (musicItem['singerMID'][-2], \
                         musicItem['singerMID'][-1], musicItem['singerMID']),
            'album': re.split('[@|]{1,2}', musicItem['f'])[5],
            'albumImg': '',
        } for musicItem in musicList],
        'code': 0,
        'message': statusMess,
        'type': 'anime',
    }))
        