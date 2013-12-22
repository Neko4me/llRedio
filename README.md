llRedio
=======
##更新日志
####2013/12/22

    写了许多代码，包括后端的Search以及前端的音乐控制的class。暂时结构还没分出来，都集成在一个HTML里。
    现在遇到一个瓶颈就是无法播放wma的音频文件。以至于mp3的文件呢是3M+的，在Chrome的network下竟然直接挂了（403错误），Opera下下载到1M也就挂了。一边加载一边播放的方式还搞不定，难道要集成Flash进去么?(残念
    想不出解决办法之前也不想做了。现在有的细节还没做好，比如hover到歌手的头像上出来的暂停按钮还不是居中的(暂时也不知道怎么写下去..
    啊，欢迎贡献代码。求帮助QuQ

一个Django框架下的开源在线听歌平台。   

###坑
llRedio基于Django，<del>主要是我要练手一下Django REST Freamwork。</del>    
当然用不用Django REST Freamwork方式来做我也不知道。最近期末考试也没时间。   
所以先挖一个坑好了。

###后端构建
llRedio的Django后端分为几个功能。   

+ 根据歌手播放歌曲，不随机（不会）   
+ 根据心情播放歌曲，提供几种心情选择   
+ 播放一个专辑的歌曲   
+ 根据歌单播放，即是什么动漫类等

以上功能根据实际情况决定是否实现。   
返回json格式大体如下：   

    {
        type: "type", //表示哪几类
        detail: "anime",
        page: 1, //歌曲页数，下一次获取时page+1
        musicList: [
            {
                "musicID": 1700787,
                "musicTitle": "六兆年と一夜物語",
                "musicUrl": "http://xxxxxx.qqmusic.com/196k/1700787.mp3",
                "singer": "VOCALOID",
                "album": "EXIT TUNES PRESENTS Vocaloconnection feat. 初音ミク"
            },
            {
                "musicID": xxxxx,
                "musicTitle": "xxxxxxxxxxxx",
                "musicUrl": "http://xxxxxx.qqmusic.com/196k/xxxxxxx.mp3",
                "singer": "xxxxx",
                "album": "xxxxxxxxxxxxxxxxxxxxxxx"
            }
        ]
        
    }


请求后端json如下：

    {
        type: "type",
        detail: "nc", //脑残类
        page: 0,　//大概不会分页，具体再说吧
    }


    {
        type: "singer",
        detail: "初音ミク",
        page: 2,
    }
    

    {
        type: "album",
        detail: "梦游计",
        page: 2,
    }

###前端构建
llRedio的前端要做的很！精！致！    
支持Chrome/Opera/FireFox/IE11。   

首先要精心挑选一堆图片，根据心情（或者歌单种类）切换。   
大概分为如下：   

+ 脑残类（国产系, nc）   
+ 动漫类（日语系, anime）   
+ 风景类（纯音乐, onlymusic）   

加入大量webkit的动画效果。   
技术选型是基于HTML5+CSS3+基于jQuery。    

###吐槽

+ <del>实际上我只想做动漫类的</del>    
+ <del>期末快挂科了</del>    
+ <del>大概这个项目不会夭折</del>   
