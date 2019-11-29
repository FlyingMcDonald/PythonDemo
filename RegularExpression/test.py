import re

content = '''


<!DOCTYPE html>
<html lang="zh-CN" class="ua-linux ua-ff70 book-new-nav">
  <head>
    <meta charset="utf-8">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
  <meta http-equiv="mobile-agent" content="format=xhtml; url=http://m.douban.com/book/">
  <meta name="keywords" content="豆瓣读书,新书速递,畅销书,书评,书单"/>
  <meta name="description" content="记录你读过的、想读和正在读的书，顺便打分，添加标签及个人附注，写评论。根据你的口味，推荐适合的书给你。" />
  <meta name="verify-v1" content="EYARGSAVd5U+06FeTmxO8Mj28Fc/hM/9PqMfrlMo8YA=">
  <meta property="wb:webmaster" content="7c86191e898cd20d">
  <meta property="qc:admins" content="1520412177364752166375">

    <title>
    豆瓣读书
</title>
    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico"
      type="image/x-icon">
    <script src="https://img3.doubanio.com/f/book/0495cb173e298c28593766009c7b0a953246c5b5/js/book/lib/jquery/jquery.js"></script>
    <script>
      var Douban = {}, Book = {}
      var Do=function(){Do.actions.push([].slice.call(arguments))};Do.ready=function(){Do.actions.push([].slice.call(arguments))},Do.add=Do.define=function(o,l){Do.mods[o]=l},Do.global=function(){Do.global.mods=Array.concat(Do.global.mods,[].slice.call(arguments))},Do.global.mods=[],Do.mods={},Do.actions=[];
    </script>
    

<script src="https://img3.doubanio.com/f/book/6a411a14e088636db2bc428ec7125b476791e3fd/js/book/lib/define.js"></script>
<script>
  define.ns('Book')
  define.config({
    'jquery': '$'
  , 'piwik': 'Piwik'
  , 'mod/ga': 'Book.ga'
  , 'mod/ajax': 'Book.ajax'
  , 'mod/cookie': 'Book.cookie'
  })

  Do.add('mod/cookie', {
    path: 'https://img3.doubanio.com/f/book/6542b92d560cd64f30c9248e6c35499cc11c0d29/js/book/mod/cookie.js'
  , type: 'js'
  })

  Do.add('mod/ajax', {
    path: 'https://img3.doubanio.com/f/book/b455e168dbfaa03597d2e336c3f56e32843361c9/js/book/mod/ajax.js'
  , requires: ['mod/cookie']
  , type: 'js'
  })

  Do.add('mod/ga', {
    path: 'https://img3.doubanio.com/f/book/42544a42ebd9be4aee64b3a8c6df1a15a8c8e020/js/book/mod/ga.js'
  , type: 'js'
  })
</script>

    
<script>!function(e){var o=function(o,n,t){var c,i,r=new Date;n=n||30,t=t||"/",r.setTime(r.getTime()+24*n*60*60*1e3),c="; expires="+r.toGMTString();for(i in o)e.cookie=i+"="+o[i]+c+"; path="+t},n=function(o){var n,t,c,i=o+"=",r=e.cookie.split(";");for(t=0,c=r.length;t<c;t++)if(n=r[t].replace(/^\s+|\s+$/g,""),0==n.indexOf(i))return n.substring(i.length,n.length).replace(/\"/g,"");return null},t=e.write,c={"douban.com":1,"douban.fm":1,"google.com":1,"google.cn":1,"googleapis.com":1,"gmaptiles.co.kr":1,"gstatic.com":1,"gstatic.cn":1,"google-analytics.com":1,"googleadservices.com":1},i=function(e,o){var n=new Image;n.onload=function(){},n.src="https://www.douban.com/j/except_report?kind=ra022&reason="+encodeURIComponent(e)+"&environment="+encodeURIComponent(o)},r=function(o){try{t.call(e,o)}catch(e){t(o)}},a=/<script.*?src\=["']?([^"'\s>]+)/gi,g=/http:\/\/(.+?)\.([^\/]+).+/i;e.writeln=e.write=function(e){var t,l=a.exec(e);return l&&(t=g.exec(l[1]))?c[t[2]]?void r(e):void("tqs"!==n("hj")&&(i(l[1],location.href),o({hj:"tqs"},1),setTimeout(function(){location.replace(location.href)},50))):void r(e)}}(document);
</script>

    
  
  <link href="https://img3.doubanio.com/f/book/1604a80024fc12b4f7a3c77519ba00486636863f/css/book/master.css" rel="stylesheet" type="text/css">

  <link href="https://img3.doubanio.com/f/book/222a5c61e041638af8defc87cf97f4a863a77922/css/book/base/init.css" rel="stylesheet">
  <style type="text/css"></style>
  <script>var _head_start = new Date();</script>
  

  
  <script type='text/javascript'>
    var _vds = _vds || [];
    (function(){ _vds.push(['setAccountId', '22c937bbd8ebd703f2d8e9445f7dfd03']);
        _vds.push(['setCS1','user_id','0']);
            (function() {var vds = document.createElement('script');
                vds.type='text/javascript';
                vds.async = true;
                vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
                var s = document.getElementsByTagName('script')[0];
                s.parentNode.insertBefore(vds, s);
            })();
    })();
</script>

  
  <script type='text/javascript'>
    var _vwo_code=(function(){
      var account_id=249272,
          settings_tolerance=2000,
          library_tolerance=2500,
          use_existing_jquery=false,
          // DO NOT EDIT BELOW THIS LINE
          f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_

<div id="db-nav-book" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;book.douban.com">豆瓣读书</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;search.douban.com&#47;book/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="书名、作者、ISBN" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1001" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">
    

<div class="nav-items">
  <ul>
    <li    ><a href="https://book.douban.com/cart/"
     >购书单</a>
    </li>
    <li    ><a href="https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban"
            target="_blank"
     >电子图书</a>
    </li>
    <li    ><a href="https://market.douban.com/book?utm_campaign=book_nav_freyr&utm_source=douban&utm_medium=pc_web"
     >豆瓣书店</a>
    </li>
    <li    ><a href="https://book.douban.com/annual/2018?source=navigation"
            target="_blank"
     >2018年度榜单</a>
    </li>
    <li    ><a href="https://www.douban.com/standbyme/2018?source=navigation"
            target="_blank"
     >2018书影音报告</a>
    </li>
    <li          class=" book-cart"
    ><a href="https://market.douban.com/cart/?biz_type=book&utm_campaign=book_nav_cart&utm_source=douban&utm_medium=pc_web"
            target="_blank"
     >购物车</a>
    </li>
  </ul>
</div>

    <a href="https://book.douban.com/annual/2018?source=book_navigation" class="bookannual2018"></a>
  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'book_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= pic}}" width="40" />
            <div>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                <p>
                {{if type == "b"}}
                    {{= author_name}}
                {{else type == "a" }}
                    {{if en_name}}
                        {{= en_name}}
                    {{/if}}
                {{/if}}
                 </p>
            </div>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/a4a38a5/book/bundle.js" defer="defer"></script>





  <div id="wrapper">
    
  <!-- douban ad begin -->
  <div id="dale_book_home_top_super_banner" class="ad-placeholder" style="margin: -18px 0 0;">
  </div>
  <!-- douban ad end -->

    
  <div id="content">
    

    <div class="grid-16-8 clearfix">
      
      <div class="article">
  
  

  
  
  <div class="section books-express ">
    <div class="hd">
      
  <h2 class=''>
    <span class="">新书速递</span>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
          >更多»</a>
      </span>
  </h2>

      <div class="slide-controls">
        <ol class="slide-dots">
          <li><a data-index="1" href="#" class=""></a></li>
          <li><a data-index="2" href="#" class=""></a></li>
          <li><a data-index="3" href="#" class=""></a></li>
          <li><a data-index="4" href="#" class=""></a></li>
        </ol>
        <div class="slide-btns">
          <a href="#" class="prev">&#8249;</a>
          <a href="#" class="next">&#8250;</a>
        </div>
      </div>
    </div>
    <div class="bd">
      <div class="carousel">
        <div class="slide-list">
          
  
    <ul class="list-col list-col5 list-express slide-item">
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34860553/?icn=index-latestbook-subject" title="我们盗走星座的理由">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33507772.jpg" class=""
                  width="115px" height="172px" alt="我们盗走星座的理由">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34860553/?icn=index-latestbook-subject"
                  title="我们盗走星座的理由">我们盗走星座的理由</a>
              </div>
              <div class="author">
                （日）北山猛邦
              </div>
              <div class="more-meta">
                <h4 class="title">
                  我们盗走星座的理由
                </h4>
                <p>
                  <span class="author">
                    （日）北山猛邦
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    新星出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  《我们盗走星座的理由》由五个短篇小说组成，开启一个个纯真幻境——
暗恋学长的高中少女，为了实现恋情偷偷尝试巫术；
爱哭的小孩，醒后发现自己身处让人忘却时间和忧伤的妖精学校；
在东京打拼的失意青年，捡到一部手机，以为生活就此出现转机；
于灾难中幸免的痴情男孩，终于等来能解除心上人所中魔咒的那一天；
精通天文知识的少年，偷走天上的星星变成项链送给病危女...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27156274/?icn=index-latestbook-subject" title="德国人">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33499675.jpg" class=""
                  width="115px" height="172px" alt="德国人">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27156274/?icn=index-latestbook-subject"
                  title="德国人">德国人</a>
              </div>
              <div class="author">
                [德]埃米尔·路德维希
              </div>
              <div class="more-meta">
                <h4 class="title">
                  德国人
                </h4>
                <p>
                  <span class="author">
                    [德]埃米尔·路德维希
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    文汇出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ☆20世纪最伟大的传记作家之一为德国人作传
☆一本书读懂德国人的浪漫与暴力、理智与狂热
☆演绎德国人千年盛衰史，讲述一部不断重复悲剧和充满讽刺的历史
·
德意志帝国和德意志民族是两件不同的事情。本书叙述的是德国人的历史，而不是德国的历史。
从梦想主宰世界的卡尔大帝，发明活版印刷的 古腾堡，终身从事宗教改革的路德，发现行星规律的开普勒，狂飙运动中兴起的...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34866400/?icn=index-latestbook-subject" title="大象席地而坐">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33516881.jpg" class=""
                  width="115px" height="172px" alt="大象席地而坐">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34866400/?icn=index-latestbook-subject"
                  title="大象席地而坐">大象席地而坐</a>
              </div>
              <div class="author">
                胡迁
              </div>
              <div class="more-meta">
                <h4 class="title">
                  大象席地而坐
                </h4>
                <p>
                  <span class="author">
                    胡迁
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    译林出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  拍电影时，他叫胡波；写小说时，他叫胡迁。这两个身份如同两条平行线，一直贯穿其创作生涯，构置了两条独具魅力的创作轨迹，直到在电影《大象席地而坐》中交叠重合。本书完整收录了这部非凡遗作的三万字电影拍摄剧本，从中可以看到胡迁对文学语言和影像语言敏锐的感知力和表现力。书中还收录 了 胡迁完成于2011年却从未发表的长篇处女作《小区》：小区的下水道污水横...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34857213/?icn=index-latestbook-subject" title="亲密陷阱">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33527618.jpg" class=""
                  width="115px" height="172px" alt="亲密陷阱">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34857213/?icn=index-latestbook-subject"
                  title="亲密陷阱">亲密陷阱</a>
              </div>
              <div class="author">
                [比利时]埃丝特•佩瑞尔（Esther Perel)
              </div>
              <div class="more-meta">
                <h4 class="title">
                  亲密陷阱
                </h4>
                <p>
                  <span class="author">
                    [比利时]埃丝特•佩瑞尔（Esther Perel)
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    上海社会科学院出版社|青豆书坊
                  </span>
                </p>
                <p class="abstract">
                  
                  一部直击婚恋隐痛的震撼之作。
为什么婚后很快没了激情？
伴侣性冷淡怎么办？
为什么有了孩子之后，我们对彼此没有欲望了？
出轨/被出轨后，要离婚吗？
爱和性，哪个更重要？
为什么婚姻美满儿女双全，我却仍感到孤独？
本书以优雅的姿态和深刻的洞见，解答了上述种种婚姻与情感难题。作为一名从业35年的婚恋心理咨询师，作者已经帮助无数身处婚恋困境的伴侣。如何让浪漫的...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34648287/?icn=index-latestbook-subject" title="幻兽动物园">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33515512.jpg" class=""
                  width="115px" height="172px" alt="幻兽动物园">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34648287/?icn=index-latestbook-subject"
                  title="幻兽动物园">幻兽动物园</a>
              </div>
              <div class="author">
                [英] 利奥·鲁伊克比
              </div>
              <div class="more-meta">
                <h4 class="title">
                  幻兽动物园
                </h4>
                <p>
                  <span class="author">
                    [英] 利奥·鲁伊克比
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    后浪丨四川人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  神秘野兽之百科全书，“超动物学”之词典
近 600 个词条，逾 70 张插图
惊奇感使我们去探寻传说的真相，讲述幻兽的传奇

◎ 编辑推荐
★ 幻想野兽的动物园，“超动物学”百科全书
这个领域包含所有传说中的生物、寓言中的动物以及神话中的怪物，但不包括现代幻想作品中的转瞬即逝的 产物。从老普林尼的博物学巨著，到马可波罗的旅行笔记；从航海家的奇异见闻，到标本剥制者的...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34836249/?icn=index-latestbook-subject" title="没药花园">
                <img src="https://img9.doubanio.com/view/subject/m/public/s33488456.jpg" class=""
                  width="115px" height="172px" alt="没药花园">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34836249/?icn=index-latestbook-subject"
                  title="没药花园">没药花园</a>
              </div>
              <div class="author">
                何袜皮
              </div>
              <div class="more-meta">
                <h4 class="title">
                  没药花园
                </h4>
                <p>
                  <span class="author">
                    何袜皮
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    江苏凤凰文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  自私的欲望和扭曲的人性，或许会隐藏在阴暗处，但从不会离开社会的舞台。一些案件已经尘埃落定，却一直让人不能释怀……
《没药花园：十五个绝对真实的案件》系人类学博士、百万级热门微信公众号“没药花园”创始人及主笔何袜皮重磅推出的犯罪悬疑推理系列，这些文章多为在社会上引起大众强烈关注的罪案与悬而未决谜团的分析。其中包括美国黑色大丽花案、美国楼梯悬案...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34859246/?icn=index-latestbook-subject" title="黑色天鹅">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33516277.jpg" class=""
                  width="115px" height="172px" alt="黑色天鹅">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34859246/?icn=index-latestbook-subject"
                  title="黑色天鹅">黑色天鹅</a>
              </div>
              <div class="author">
                （日）鲇川哲也
              </div>
              <div class="more-meta">
                <h4 class="title">
                  黑色天鹅
                </h4>
                <p>
                  <span class="author">
                    （日）鲇川哲也
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    新星出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ★《周刊文春》票选“日本百大推理小说”
★日本推理文坛巨匠 两部作品同获推理作家俱乐部奖
★与横沟正史、高木彬光并称为日本战后本格三大家
★以“鲇川哲也”命名的推理文学大奖成为日本权威奖项
内容介绍
东和纺织的罢工事件正在如火如荼地展开。掌握主动权的资方即将迎来胜利，社长西之幡豪辅却惨遭杀害，尸体被弃置于行使中的列车车顶。虽然犯罪嫌疑人众多，但每个...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30317910/?icn=index-latestbook-subject" title="教父电影全剧本（全彩插图评注版）">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33519471.jpg" class=""
                  width="115px" height="172px" alt="教父电影全剧本（全彩插图评注版）">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30317910/?icn=index-latestbook-subject"
                  title="教父电影全剧本（全彩插图评注版）">教父电影全剧本（全彩插图评注版）</a>
              </div>
              <div class="author">
                [美] 珍妮·M·琼斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  教父电影全剧本（全彩插图评注版）
                </h4>
                <p>
                  <span class="author">
                    [美] 珍妮·M·琼斯
                  </span>
                  /
                  <span class="year">
                    2019-12
                  </span>
                  /
                  <span class="publisher">
                    后浪丨北京联合出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  全球男人的圣经，政坛大佬的挚爱
世界影史神作，改编自美国出版史头号畅销书
姜文、《疯狂动物城》致敬对象
《2001太空漫游》导演10刷认证
豆瓣82万人9.3高分
IMDb长期占据No.1
你真的以为自己看懂《教父》了吗？
从流行小说到传世经典
从无人看好的毒饼，到黑帮史诗
派拉蒙官方授权
完整剧本×幕后解密×独家访谈
权威译本，首度面世
正片、被删片段与花絮同步呈现，获得评论...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34464618/?icn=index-latestbook-subject" title="圣天秤星">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33516871.jpg" class=""
                  width="115px" height="172px" alt="圣天秤星">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34464618/?icn=index-latestbook-subject"
                  title="圣天秤星">圣天秤星</a>
              </div>
              <div class="author">
                [英]彼得·汉密尔顿
              </div>
              <div class="more-meta">
                <h4 class="title">
                  圣天秤星
                </h4>
                <p>
                  <span class="author">
                    [英]彼得·汉密尔顿
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    上海人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ★深受科幻迷喜爱的太空歌剧大家之作首度推出简体中文版！
★作者是豆瓣网24万网友评价、均分9.1的年度大热美剧《爱，死亡和机器人》编剧之一，曾荣获英伦科幻奖，并多次入围雨果奖、克拉克奖，擅长构建宏大的宇宙架构、浩繁的人物谱系，作品以阅读感酣畅著称。
★22 世纪，克隆技术与虫洞技术飞速发展，移民外星球已成为可能，一切看似尽善尽美，但当克隆人无法辨识自...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/33426137/?icn=index-latestbook-subject" title="米，面，鱼">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33523989.jpg" class=""
                  width="115px" height="172px" alt="米，面，鱼">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/33426137/?icn=index-latestbook-subject"
                  title="米，面，鱼">米，面，鱼</a>
              </div>
              <div class="author">
                [美]马特·古尔丁
              </div>
              <div class="more-meta">
                <h4 class="title">
                  米，面，鱼
                </h4>
                <p>
                  <span class="author">
                    [美]马特·古尔丁
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    广西师范大学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  日本是全世界食客心中的一大圣地。米其林餐厅数量居世界之首，但求匠心独运的无名小店更是数不胜数。
饮食作家马特·古尔丁走访东京、大阪、京都、福冈、广岛、北海道、能登七座日本饮食重镇，品尝每个城市的代表性食物，走访热爱并传承当地饮食文化的各色人物，将城市的历史文化也融入自己的饮食观察中。
从专业冷静的料理职人、热情如火的街头小贩，到努力在此扎根的...
                </p>
              </div>
            </div>
          </li>
    </ul>
    <ul class="list-col list-col5 list-express slide-item">
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34821347/?icn=index-latestbook-subject" title="老虎与不夜城">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33514790.jpg" class=""
                  width="115px" height="172px" alt="老虎与不夜城">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34821347/?icn=index-latestbook-subject"
                  title="老虎与不夜城">老虎与不夜城</a>
              </div>
              <div class="author">
                陈志炜
              </div>
              <div class="more-meta">
                <h4 class="title">
                  老虎与不夜城
                </h4>
                <p>
                  <span class="author">
                    陈志炜
                  </span>
                  /
                  <span class="year">
                    2019-12
                  </span>
                  /
                  <span class="publisher">
                    后浪丨四川文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  一本跨越文体的短篇小说集！
“语句像鸟翅一样旋紧，牵引读者直抵陌异之境，
眼前泛起隐现悖论的工业热雾”
深蕴迟疑与思索，写作十年作品首度出版
★ 编辑推荐
◎陈志炜是一位认真、纯粹，有时偏执的青年作者。其作品呈现一幅幅新鲜、奇异的图景，语言诗化，在国内青年作者的创作中并不多见。
◎本书从炼油厂的少年往事起跳，轻跃在夏日与梦境之间。部分作品初读觉得接近...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34821222/?icn=index-latestbook-subject" title="无尽之河：平克·弗洛伊德传">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33485533.jpg" class=""
                  width="115px" height="172px" alt="无尽之河：平克·弗洛伊德传">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34821222/?icn=index-latestbook-subject"
                  title="无尽之河：平克·弗洛伊德传">无尽之河：平克·弗洛伊德传</a>
              </div>
              <div class="author">
                马克·布莱克
              </div>
              <div class="more-meta">
                <h4 class="title">
                  无尽之河：平克·弗洛伊德传
                </h4>
                <p>
                  <span class="author">
                    马克·布莱克
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    雅众文化 | 博集天卷 | 湖南文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ◆ 从初试啼声的《黎明门前的风笛手》，到史诗级巨作《月之暗面》《愿你在此》《迷墙》，直至流淌不息的《无尽之河》 ，《无尽之河：平克·弗洛伊德传》生动再现了这支无数乐迷顶礼膜拜的乐队横跨半个世纪的音乐历程。
◆ 知名音乐文化记者马克·布莱克全新力作，获《星期日电讯报》《卫 报》《观察家报》《奥斯汀纪事报》《科克斯书评》《Q》《唱片收藏家》《经典摇滚...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34672178/?icn=index-latestbook-subject" title="你一生的故事">
                <img src="https://img9.doubanio.com/view/subject/m/public/s33516836.jpg" class=""
                  width="115px" height="172px" alt="你一生的故事">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34672178/?icn=index-latestbook-subject"
                  title="你一生的故事">你一生的故事</a>
              </div>
              <div class="author">
                [美] 特德·姜
              </div>
              <div class="more-meta">
                <h4 class="title">
                  你一生的故事
                </h4>
                <p>
                  <span class="author">
                    [美] 特德·姜
                  </span>
                  /
                  <span class="year">
                    2019-12
                  </span>
                  /
                  <span class="publisher">
                    译林出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ★ 科幻大片《降临》原著小说。
★ 美国华裔科幻奇才特德·姜代表作，得遍世界大奖的开脑洞之作。
★ 始于科学内核，收于人文关怀：如果注定失去，你会害怕拥有吗？
★ 每一个“科幻必读”书单上都有特德·姜。
特德·姜，当代最优秀的科幻小说家之一。
出道30年，仅17个短篇，却四获星云奖/四获雨果奖/三获轨迹奖/三获日本科幻大奖，此外还获得过英国科幻协会奖/斯特金奖/坎...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34851866/?icn=index-latestbook-subject" title="中国造园艺术">
                <img src="https://img9.doubanio.com/view/subject/m/public/s33528366.jpg" class=""
                  width="115px" height="172px" alt="中国造园艺术">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34851866/?icn=index-latestbook-subject"
                  title="中国造园艺术">中国造园艺术</a>
              </div>
              <div class="author">
                曹汛
              </div>
              <div class="more-meta">
                <h4 class="title">
                  中国造园艺术
                </h4>
                <p>
                  <span class="author">
                    曹汛
                  </span>
                  /
                  <span class="year">
                    2019-11-1
                  </span>
                  /
                  <span class="publisher">
                    北京出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  本书是建筑学家、园林学家曹汛先生多年研究成果的首次结集。本书收录《陆游〈钗头凤〉的错解错传和绍兴沈园的错认错定》《石涛叠山“人间孤品”，一个媕浅而粗疏的园林童话》等曹汛先生的代表性文章，材料翔实，证据充分，纠正了流传数十年、数百年甚至上千年的历史大错案。“破旧”之外更长于“立新”。本书不仅对中国古代造园艺术进行了精到的介绍，还将园林建筑纳...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34868503/?icn=index-latestbook-subject" title="捉猫故事集">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33509225.jpg" class=""
                  width="115px" height="172px" alt="捉猫故事集">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34868503/?icn=index-latestbook-subject"
                  title="捉猫故事集">捉猫故事集</a>
              </div>
              <div class="author">
                [法]马塞尔·埃梅（Marcel Aymé）
              </div>
              <div class="more-meta">
                <h4 class="title">
                  捉猫故事集
                </h4>
                <p>
                  <span class="author">
                    [法]马塞尔·埃梅（Marcel Aymé）
                  </span>
                  /
                  <span class="year">
                    2019-12
                  </span>
                  /
                  <span class="publisher">
                    北京联合出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  《捉猫故事集》是一本同时属于大人和小朋友的短篇故事集，讲述了生活在法国农庄的小姐妹俩苔尔菲娜、玛丽奈特，她们的爸爸妈妈，和一群动物们的故事。这些动物性格各异，是故事真正的主人公。他们中，有会求雨的猫、耿直善良的狗、理性的鸭子、一心苦读的牛、想要瘦身的猪，还有渴望见到雪的豹子、想要改邪归正的狼、热爱自由的鹿等等。人和动物热热闹闹相处的世界，...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34870933/?icn=index-latestbook-subject" title="人生十二法则">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33529549.jpg" class=""
                  width="115px" height="172px" alt="人生十二法则">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34870933/?icn=index-latestbook-subject"
                  title="人生十二法则">人生十二法则</a>
              </div>
              <div class="author">
                [加拿大] 乔丹•彼得森&nbsp;/&nbsp;Jordan B. Peterson
              </div>
              <div class="more-meta">
                <h4 class="title">
                  人生十二法则
                </h4>
                <p>
                  <span class="author">
                    [加拿大] 乔丹•彼得森&nbsp;/&nbsp;Jordan B. Peterson
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    浙江人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  【内容简介】
现代人欠缺的，不是知识，而是实现的能力，更准确地说，是付诸行动的心理素质。在《人生十二法则》中，著名心理学家乔丹·彼得森的将人类数千年来哲学思考、神话故事中的精神财富与心理学、生物学、神经科学等学科的前沿研究相结合，用12条*基本的人生法则，为千禧一代找到摆脱人生困境的方法。
面对十有八九不如意的人生，我们真正需要的，不是虚伪的励...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34786081/?icn=index-latestbook-subject" title="兔子洞女孩">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33514087.jpg" class=""
                  width="115px" height="172px" alt="兔子洞女孩">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34786081/?icn=index-latestbook-subject"
                  title="兔子洞女孩">兔子洞女孩</a>
              </div>
              <div class="author">
                [墨西哥] 詹妮弗·克莱门特
              </div>
              <div class="more-meta">
                <h4 class="title">
                  兔子洞女孩
                </h4>
                <p>
                  <span class="author">
                    [墨西哥] 詹妮弗·克莱门特
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    上海人民出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ★比《灿烂千阳》更透彻的人生际遇，比少年Pi更震撼的漂泊旅程。
作者花了数十 年时间倾 听那些深受墨西哥暴力影响的女性诉说，这不仅是少女蕾蒂戴的故事，更是当下墨西哥毒品阴影下女性的真实遭遇。
★全球20种语言共读。诺奖得主石黑一雄、《少年Pi的奇幻漂流》作者扬•马特尔倾 情推荐。
★“如果说查尔斯•狄更斯的《雾都孤儿》能改变立法，让贫穷的英国儿童免于苦难...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/33438831/?icn=index-latestbook-subject" title="梦的宇宙志">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33516227.jpg" class=""
                  width="115px" height="172px" alt="梦的宇宙志">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/33438831/?icn=index-latestbook-subject"
                  title="梦的宇宙志">梦的宇宙志</a>
              </div>
              <div class="author">
                [日]涩泽龙彦
              </div>
              <div class="more-meta">
                <h4 class="title">
                  梦的宇宙志
                </h4>
                <p>
                  <span class="author">
                    [日]涩泽龙彦
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    广西师范大学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ☀内容简介
本书为日本文化学者、翻译家涩泽龙彦的博物随笔集。作者自如地游走于古今东西秘闻的纵深沟壑中，在幻想与现实的错位间穿梭延展，于不同的学科分野间恣意跳跃，引经据典，凭借过人的想象力与敏锐的感观，探讨了机关人偶、怪物、天使等各种趣味话题，以物的历史讲述社会文化史。
☀名人推荐
要是没有了这个人，日本会是一个多么寂寞的国家啊。
——三岛由纪夫
我...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34856160/?icn=index-latestbook-subject" title="最后的巨人">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33499752.jpg" class=""
                  width="115px" height="172px" alt="最后的巨人">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34856160/?icn=index-latestbook-subject"
                  title="最后的巨人">最后的巨人</a>
              </div>
              <div class="author">
                [法]法兰斯瓦·普拉斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  最后的巨人
                </h4>
                <p>
                  <span class="author">
                    [法]法兰斯瓦·普拉斯
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    后浪丨北京联合出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  《欧赫贝26国幻游记》作者法兰斯瓦·普拉斯绘本代表作，博洛尼亚文学奖，国际安徒生插画奖提名，一个渺小人类与九个梦想星星的巨人的故事，给儿童与青少年的幻想文学启蒙
◎ 编辑推荐
☆《欧赫贝26国幻游记》作者法兰斯瓦·普拉斯绘本代表作
安徒生国际插画奖提名、博洛尼亚青少年文学奖得主。本书曾获法国作家协会青少年书籍大奖、法国青少年图书金球奖、比利时青少年...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34781358/?icn=index-latestbook-subject" title="史记的读法">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33506895.jpg" class=""
                  width="115px" height="172px" alt="史记的读法">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34781358/?icn=index-latestbook-subject"
                  title="史记的读法">史记的读法</a>
              </div>
              <div class="author">
                杨照
              </div>
              <div class="more-meta">
                <h4 class="title">
                  史记的读法
                </h4>
                <p>
                  <span class="author">
                    杨照
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    理想国 | 广西师范大学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ★	白岩松、俞敏洪、许宏、梁文道、许知远等人共同推荐的《史记》入门读本
★	“看理想”口碑节目完整再现，看司马迁如何精准地捕捉人性的高光时刻
★	打破《史记》的顺序，在司马迁的世界里看到历史
★	用历史式读法还原社会时代背景，用文学式读法解读视角和态度
本书是看理想的口碑节目《古今：杨照史记百讲》精编而成。作者打乱《史记》原来的篇章次序，以“历史式读法”...
                </p>
              </div>
            </div>
          </li>
    </ul>
    <ul class="list-col list-col5 list-express slide-item">
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34841937/?icn=index-latestbook-subject" title="群星">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33490619.jpg" class=""
                  width="115px" height="172px" alt="群星">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34841937/?icn=index-latestbook-subject"
                  title="群星">群星</a>
              </div>
              <div class="author">
                七月
              </div>
              <div class="more-meta">
                <h4 class="title">
                  群星
                </h4>
                <p>
                  <span class="author">
                    七月
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    人民文学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  当你凝视宇宙时，宇宙也在凝视着你。
要知道，文明之间，没有对抗，只有碾压！
【内容简介】
五年前，FAST 收到神秘信号，揭开宇宙真相的一角。
五年后，德国格拉苏蒂镇全镇蒸发，一点辐射都没留下。
如 今，十九国峰会即将在成都召开，但天府之国却面临一场灭顶之灾。
为保护一千多万市民，国安局两名干探临危受命，开始了一场前所未有的二十四小时反恐行动！
然而，他们的...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34840198/?icn=index-latestbook-subject" title="人类的终极问题">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33523533.jpg" class=""
                  width="115px" height="172px" alt="人类的终极问题">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34840198/?icn=index-latestbook-subject"
                  title="人类的终极问题">人类的终极问题</a>
              </div>
              <div class="author">
                袁越
              </div>
              <div class="more-meta">
                <h4 class="title">
                  人类的终极问题
                </h4>
                <p>
                  <span class="author">
                    袁越
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    生活·读书·新知三联书店
                  </span>
                </p>
                <p class="abstract">
                  
                  人类来自哪里？我们为什么会变老？创造力究竟是怎么来的？这三个问题是人类的终极问题，因为只有了解了人类的过去，才能看清我们的未来；只有了解了死亡的本质，才能弄清生命的意义；只有了解了创造力的来源，才能明白人类为何变成今天的样子。本书作者借助专业的科学背景、大量的阅读梳理、实地的采访调查，把目前已知的这三个问题的最佳答案和推理过程呈现出来，并...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34808267/?icn=index-latestbook-subject" title="萨拉戈萨手稿">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33492042.jpg" class=""
                  width="115px" height="172px" alt="萨拉戈萨手稿">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34808267/?icn=index-latestbook-subject"
                  title="萨拉戈萨手稿">萨拉戈萨手稿</a>
              </div>
              <div class="author">
                [波兰] 扬·波托茨基&nbsp;/&nbsp;Jean Potocki
              </div>
              <div class="more-meta">
                <h4 class="title">
                  萨拉戈萨手稿
                </h4>
                <p>
                  <span class="author">
                    [波兰] 扬·波托茨基&nbsp;/&nbsp;Jean Potocki
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    浦睿文化·湖南文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  亲爱的阿方索，
我们来到这里并非因为偶然……
我们在等你。
瓦隆卫队的年轻军官阿方索赶赴马德里加入他的军队。但他很快就发现，他被困在一家神秘的路边客栈，和形形色色的怪人待在一起：小偷、强盗、贵族、妓女与吉卜赛人。他在六十六天里记录下他们的故事。大约四十年后，这部手稿在一 个锁起来的箱子里被发现。
这部关于伪装、魔法、幻想，关于荣誉与怯懦、着魔与诱...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34808250/?icn=index-latestbook-subject" title="被弃的意象">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33519971.jpg" class=""
                  width="115px" height="172px" alt="被弃的意象">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34808250/?icn=index-latestbook-subject"
                  title="被弃的意象">被弃的意象</a>
              </div>
              <div class="author">
                [英] C·S·路易斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  被弃的意象
                </h4>
                <p>
                  <span class="author">
                    [英] C·S·路易斯
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    东方出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  本书是著名文学家、学者C.S.路易斯的最后一部学术著作。书的前身是路易斯在“二战”前后为牛津大学学生开设的“中世纪和文艺复兴诗歌导论”课程讲稿。路易斯以中世纪和文艺复兴时期的文学为主要样本，旨在勾勒其背后的思想文化形态，即作者所说的“中世纪模型”，并由此审视这个时期的文学特质。
《被弃的意象》不只是一部通识类的学术著作，更是一部智慧之书，它记载...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34873145/?icn=index-latestbook-subject" title="生肉">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33514098.jpg" class=""
                  width="115px" height="172px" alt="生肉">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34873145/?icn=index-latestbook-subject"
                  title="生肉">生肉</a>
              </div>
              <div class="author">
                [英]奥利维娅·莱恩
              </div>
              <div class="more-meta">
                <h4 class="title">
                  生肉
                </h4>
                <p>
                  <span class="author">
                    [英]奥利维娅·莱恩
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    未读·文艺家·北京联合出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  &gt;&gt;&gt; 《孤独的城市》作者首部虚构作品，生猛，幽默，一针见血。
&gt;&gt;&gt; 何为生肉？一段待汉化的视频，一批未加工的原始信息，一本拒绝精雕细琢的小说。
&gt;&gt;&gt; 捡拾信息碎片，“直播”无聊日常，一场为期七周的写作表演。作家利用推特发布写作计划，实时更新写作动态，坚持每天写作，只写不改。创作完毕，同时关闭推特账号。
&gt;&gt;&gt; 《纽约时报》盛赞：很多年后，当我们试图回想这...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34869500/?icn=index-latestbook-subject" title="被统治的艺术">
                <img src="https://img9.doubanio.com/view/subject/m/public/s33519906.jpg" class=""
                  width="115px" height="172px" alt="被统治的艺术">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34869500/?icn=index-latestbook-subject"
                  title="被统治的艺术">被统治的艺术</a>
              </div>
              <div class="author">
                [加] 宋怡明
              </div>
              <div class="more-meta">
                <h4 class="title">
                  被统治的艺术
                </h4>
                <p>
                  <span class="author">
                    [加] 宋怡明
                  </span>
                  /
                  <span class="year">
                    2019-12
                  </span>
                  /
                  <span class="publisher">
                    中国华侨出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  知名媒体人高晓松推荐，《明朝那些事儿》作者当年明月作序
哈佛大学费正清研究中心主任宋怡明教授全新力作
从明清日常政治入手，深入剖析中国文化肌理，透视“阳奉阴违”“上有政策，下有对策”“制度套利”等深植中国社会的潜规则
◎ 编辑推荐
☆ 荣获美国《选择》杂志2018年度“杰出学术著作奖”
☆ 知名媒体人高晓松、厦门大学教授郑振满、耶鲁大学教授濮德培、《逃避...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34840585/?icn=index-latestbook-subject" title="她的名字是">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33509418.jpg" class=""
                  width="115px" height="172px" alt="她的名字是">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34840585/?icn=index-latestbook-subject"
                  title="她的名字是">她的名字是</a>
              </div>
              <div class="author">
                [韩]赵南柱
              </div>
              <div class="more-meta">
                <h4 class="title">
                  她的名字是
                </h4>
                <p>
                  <span class="author">
                    [韩]赵南柱
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    中信出版集团
                  </span>
                </p>
                <p class="abstract">
                  
                  短篇小说集《她的名字是》是话题小说《82年生的金智英》的作者赵南柱时隔两年创作的新作。作者以2018年在韩国辛苦生存的她们的故事为原型，创作了27篇小说。《82年生的金智英》中没能讲完的她们的故事以多彩的形式，在《她的名字是》中更加坚定有力地展现出来。学校、家庭、社会……在充满了工作和生活的所有空间里，她们时而哭泣，时而欢笑，时而慌张的故事其实就...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34398024/?icn=index-latestbook-subject" title="诗意的宇宙">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33511724.jpg" class=""
                  width="115px" height="172px" alt="诗意的宇宙">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34398024/?icn=index-latestbook-subject"
                  title="诗意的宇宙">诗意的宇宙</a>
              </div>
              <div class="author">
                [奥]斯特凡·克莱因
              </div>
              <div class="more-meta">
                <h4 class="title">
                  诗意的宇宙
                </h4>
                <p>
                  <span class="author">
                    [奥]斯特凡·克莱因
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    中信出版集团
                  </span>
                </p>
                <p class="abstract">
                  
                  真实世界与我们看到的不同：
存在的事物比我们看得到的事物多20倍；
手被锤子砸到会感到疼，但构成锤子的原子内部几乎是空的；
两个相距几千米远、看似毫无关系的粒子，其实或许正在相互“感应”……
当物理学一步步揭开微小如粒子、宏大如宇宙的谜，人们惊讶地发现，原来我们习以为常的生活并非真相，而《诗意的宇宙》正带我们越过表象一探究竟。
有人担心，科学会把诗...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34822443/?icn=index-latestbook-subject" title="潘神的迷宫">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33488497.jpg" class=""
                  width="115px" height="172px" alt="潘神的迷宫">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34822443/?icn=index-latestbook-subject"
                  title="潘神的迷宫">潘神的迷宫</a>
              </div>
              <div class="author">
                [墨西哥] 吉尔莫·德尔·托罗&nbsp;/&nbsp;[德] 柯奈莉亚·冯克
              </div>
              <div class="more-meta">
                <h4 class="title">
                  潘神的迷宫
                </h4>
                <p>
                  <span class="author">
                    [墨西哥] 吉尔莫·德尔·托罗&nbsp;/&nbsp;[德] 柯奈莉亚·冯克
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    上海文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  【内容简介】
.
没有更美好的童话，只有更残酷的现实
等待十三年，终于看懂《潘神的迷宫》
.
1944年的西班牙笼罩在法西斯独裁的阴影下，女孩奥菲利娅幼年丧父，母亲嫁给了暴虐的法西斯军官，怀有身孕后便带着女儿来到军官在林间的驻地待产。在战争的恐怖中，奥菲利娅发现了一座地下迷宫，诡秘的潘神就在那里等着她。潘神对她说，她是地下王国公主的转世，唯有完成三项任务...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34463603/?icn=index-latestbook-subject" title="太阳与少女">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33477697.jpg" class=""
                  width="115px" height="172px" alt="太阳与少女">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34463603/?icn=index-latestbook-subject"
                  title="太阳与少女">太阳与少女</a>
              </div>
              <div class="author">
                [日]森见登美彦
              </div>
              <div class="more-meta">
                <h4 class="title">
                  太阳与少女
                </h4>
                <p>
                  <span class="author">
                    [日]森见登美彦
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    湖南文艺出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  ★日本奇幻、科幻小说大奖得主，直木奖多次入围，《达·芬奇》杂志2017年度白金之书，日本奇幻文学作家森见登美彦出道十四年的散文收录。
★《春宵苦短，少女前进吧！》《有顶天家族》《企鹅公路》《四叠半神话大系》等脑洞神作的诞生笔记。作者用可爱诙谐的笔调，记录着周围发生的一切事情——在鸭川的堤坝散步，感受京都之美，品尝波子汽水的清甜，回到四叠半的公...
                </p>
              </div>
            </div>
          </li>
    </ul>
    <ul class="list-col list-col5 list-express slide-item">
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34449345/?icn=index-latestbook-subject" title="美国式婚姻">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33527433.jpg" class=""
                  width="115px" height="172px" alt="美国式婚姻">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34449345/?icn=index-latestbook-subject"
                  title="美国式婚姻">美国式婚姻</a>
              </div>
              <div class="author">
                [美]塔亚莉·琼斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  美国式婚姻
                </h4>
                <p>
                  <span class="author">
                    [美]塔亚莉·琼斯
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    中信出版集团
                  </span>
                </p>
                <p class="abstract">
                  
                  ★击败两位布克奖得主，2019女性小说奖获奖之作！
★全美热销50万册，美国前总统奥巴马将本书列入2018夏季阅读书单
★2018奥普拉俱乐部推荐图书，奥普拉称其为“一本令我欲罢不能的书”
★获“美国豆瓣”Goodreads读者年度选择奖（2018）。目前Goodreads超过17万读者评论中，73%读者都给了四星以上好评。
★一本让我们深思结婚真正意义的小说，每个已经或即将迈...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34835543/?icn=index-latestbook-subject" title="云">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33486124.jpg" class=""
                  width="115px" height="172px" alt="云">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34835543/?icn=index-latestbook-subject"
                  title="云">云</a>
              </div>
              <div class="author">
                [日]山村暮鸟/著&nbsp;/&nbsp;小满/绘
              </div>
              <div class="more-meta">
                <h4 class="title">
                  云
                </h4>
                <p>
                  <span class="author">
                    [日]山村暮鸟/著&nbsp;/&nbsp;小满/绘
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    北京联合出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  《云》收录了山村暮鸟创作的123首诗，堪称“单纯”“童心”“东方”圆满融合的朴素之歌。作者从年轻时追求先锋、热衷技巧到历经沧桑后渐趋平和，以天真通透的心观照万事万物，以淡墨写意的风格抒写所见所感，读来仿佛能闻到一个好灵魂散发的草木清香。
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34863774/?icn=index-latestbook-subject" title="遗失的灵魂">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33524820.jpg" class=""
                  width="115px" height="172px" alt="遗失的灵魂">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34863774/?icn=index-latestbook-subject"
                  title="遗失的灵魂">遗失的灵魂</a>
              </div>
              <div class="author">
                [波兰] 奥尔加·托卡尔丘克&nbsp;/&nbsp;[波兰] 乔安娜 孔塞霍 绘
              </div>
              <div class="more-meta">
                <h4 class="title">
                  遗失的灵魂
                </h4>
                <p>
                  <span class="author">
                    [波兰] 奥尔加·托卡尔丘克&nbsp;/&nbsp;[波兰] 乔安娜 孔塞霍 绘
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    山东画报出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  故事讲述的是主人公杨，他丢失了自己的灵魂但浑然不知，直到有一天，他胸闷气短以为自己病了，后来经睿智的女医生点拨才知道，自己只顾步履匆匆的走，却把灵魂遗落在某个地方。
他遵循了女医生的建议，等到了不停追赶他的灵魂。从此，他们长久地过着幸福的生活。
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34834564/?icn=index-latestbook-subject" title="巴黎评论·诗人访谈">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33520413.jpg" class=""
                  width="115px" height="172px" alt="巴黎评论·诗人访谈">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34834564/?icn=index-latestbook-subject"
                  title="巴黎评论·诗人访谈">巴黎评论·诗人访谈</a>
              </div>
              <div class="author">
                《巴黎评论》编辑部
              </div>
              <div class="more-meta">
                <h4 class="title">
                  巴黎评论·诗人访谈
                </h4>
                <p>
                  <span class="author">
                    《巴黎评论》编辑部
                  </span>
                  /
                  <span class="year">
                    2019-11
                  </span>
                  /
                  <span class="publisher">
                    人民文学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  “作家访谈”是美国文学杂志《巴黎评论》（Paris Review）最持久、最著名的特色栏目。自一九五三年创刊号中的E.M.福斯特访谈至今，《巴黎评论》一期不落地刊登当代最伟大作家的长篇访谈，最初冠以“小说的艺术”之名，逐渐扩展到“诗歌的艺术”“批评的艺术”等，迄今已达三百篇以上，囊括了二十世纪下半叶至今世界文坛几乎所有的重要作家。作家访谈已然成为《巴黎评...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34431940/?icn=index-latestbook-subject" title="双胞胎">
                <img src="https://img1.doubanio.com/view/subject/m/public/s33511469.jpg" class=""
                  width="115px" height="172px" alt="双胞胎">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34431940/?icn=index-latestbook-subject"
                  title="双胞胎">双胞胎</a>
              </div>
              <div class="author">
                [日]藤崎彩织
              </div>
              <div class="more-meta">
                <h4 class="title">
                  双胞胎
                </h4>
                <p>
                  <span class="author">
                    [日]藤崎彩织
                  </span>
                  /
                  <span class="year">
                    2019-10-1
                  </span>
                  /
                  <span class="publisher">
                    人民文学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  每个人的人生中，都有一个形影不离的人
你们一起笑一起哭，一起失落一起疯狂
现在你们可能在一起，抑或分隔两地
曾经你懦弱、踟躇、迷茫，甚至迷失自我，只为成为他
谨以此书，献给你的他
—————————
只有钢琴作伴的孤独少女夏子，认识了不爱学习的月岛。月岛说：“你和我 就像双胞胎。”
这是一本孤独少女的成长经历。什么事也不会，只知道弹琴的少女经朋友指引，...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34848926/?icn=index-latestbook-subject" title="八千里路云和月">
                <img src="https://img9.doubanio.com/view/subject/m/public/s33499856.jpg" class=""
                  width="115px" height="172px" alt="八千里路云和月">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34848926/?icn=index-latestbook-subject"
                  title="八千里路云和月">八千里路云和月</a>
              </div>
              <div class="author">
                白先勇
              </div>
              <div class="more-meta">
                <h4 class="title">
                  八千里路云和月
                </h4>
                <p>
                  <span class="author">
                    白先勇
                  </span>
                  /
                  <span class="year">
                    2019-11-1
                  </span>
                  /
                  <span class="publisher">
                    中国友谊出版公司
                  </span>
                </p>
                <p class="abstract">
                  
                  我写作，是为了把人类无言的痛苦转换为文字。
——白先勇
1、大师白先勇暌违17年重磅新作。这是他的人生，更是填不满的文化乡愁。
先生书写一整个时代的生命轨迹与历史魂魄，独一无二的强韧胆识、细腻深情，引领读者逐渐碰触热得发烫的文化大家胸怀。苍茫之上姹紫嫣红，柔情坦荡。
2、中国文化圈鼎力推崇的大家，与鲁迅、张爱玲齐名。
章诒和、余秋雨、林青霞、许知远、...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/33474599/?icn=index-latestbook-subject" title="我们的时代">
                <img src="https://img1.doubanio.com/view/subject/m/public/s32333969.jpg" class=""
                  width="115px" height="172px" alt="我们的时代">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/33474599/?icn=index-latestbook-subject"
                  title="我们的时代">我们的时代</a>
              </div>
              <div class="author">
                [美]欧内斯特·海明威
              </div>
              <div class="more-meta">
                <h4 class="title">
                  我们的时代
                </h4>
                <p>
                  <span class="author">
                    [美]欧内斯特·海明威
                  </span>
                  /
                  <span class="year">
                    2019-12
                  </span>
                  /
                  <span class="publisher">
                    拜德雅丨西南师范大学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  - 编辑推荐 -
★海明威第一部杰作完整呈现。
★实验性&amp;创造力媲美艾略特《荒原》。
★他父母读后感到污秽、不安，庞德、威尔逊、菲茨杰拉德激赏连连。
★粗粝而壮美，口语又清新，坚实且干净，其独特的写作似有一个自成体系的有机存在。（《纽约时报》）
★欧内斯特·海明威是这样一个家伙：一位全新而诚实的非“文学的”生活抄写员——一位作家。（《时代周刊》）
- 内容简...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34834099/?icn=index-latestbook-subject" title="俄罗斯文学">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33507301.jpg" class=""
                  width="115px" height="172px" alt="俄罗斯文学">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34834099/?icn=index-latestbook-subject"
                  title="俄罗斯文学">俄罗斯文学</a>
              </div>
              <div class="author">
                [英国]卡特里奥娜·凯利
              </div>
              <div class="more-meta">
                <h4 class="title">
                  俄罗斯文学
                </h4>
                <p>
                  <span class="author">
                    [英国]卡特里奥娜·凯利
                  </span>
                  /
                  <span class="year">
                    2019-12-1
                  </span>
                  /
                  <span class="publisher">
                    译林出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  【名人评价及推荐】
“这本《俄罗斯文学》值得一读，作为‘牛津通识读本’之一种，它体现了这套名牌丛书的整体特点，即用浓缩的笔墨在短小的篇幅里给出关于一门学问的概括介绍。……对于不十分了解俄罗斯文学的读者而言，此书一册在手，便可获得关于俄罗斯文学的约略认知；而对于学习或研究 俄罗斯文学的专业读者而言，此书无疑也具有很多借鉴意义。”
——首都师范大...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/33657510/?icn=index-latestbook-subject" title="幻化">
                <img src="https://img9.doubanio.com/view/subject/m/public/s33515026.jpg" class=""
                  width="115px" height="172px" alt="幻化">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/33657510/?icn=index-latestbook-subject"
                  title="幻化">幻化</a>
              </div>
              <div class="author">
                [日]梅崎春生
              </div>
              <div class="more-meta">
                <h4 class="title">
                  幻化
                </h4>
                <p>
                  <span class="author">
                    [日]梅崎春生
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    南京大学出版社
                  </span>
                </p>
                <p class="abstract">
                  
                  小说集《幻化》收入日本第一次战后派文学家梅崎春生的三部代表作——《樱岛》《日落处》《幻化》。
中篇小说《樱岛》是以第一人称叙述的作品。二战结束前夕，海军通信兵中村兵曹调离坊津前往鹿儿岛的樱岛赴任。他在旅馆邂逅谈论“我想美丽地死去”的伤感的谷中尉，被右耳缺失的妓女追问“你会怎么死”，在樱岛的战壕里与性格乖张并恪守军规的吉良兵曹长产生激烈冲突，...
                </p>
              </div>
            </div>
          </li>
          
  
          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34839989/?icn=index-latestbook-subject" title="饭局的起源">
                <img src="https://img3.doubanio.com/view/subject/m/public/s33515500.jpg" class=""
                  width="115px" height="172px" alt="饭局的起源">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34839989/?icn=index-latestbook-subject"
                  title="饭局的起源">饭局的起源</a>
              </div>
              <div class="author">
                [英]马丁•琼斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  饭局的起源
                </h4>
                <p>
                  <span class="author">
                    [英]马丁•琼斯
                  </span>
                  /
                  <span class="year">
                    2019-10
                  </span>
                  /
                  <span class="publisher">
                    生活·读书·新知三联书店
                  </span>
                </p>
                <p class="abstract">
                  
                  剑桥大学考古系教授马丁·琼斯认为，一系列的“现代”行为为人类走出非洲提供了必备的生存策略，包括面对面地分享食物、讲故事和旅行。而考古发掘中对所有单位进行浮选、系统的植物考古学、沉积物和稳定同位素分析，将会获得更全面的人类分享食物的画面。
马丁•琼斯以讲故事的方式，为我们梳理了千万年以来，“人类”分享食物的历史。从人类近亲黑猩猩分享一只髯猴的...
                </p>
              </div>
            </div>
          </li>
    </ul>

        </div>
      </div>
    </div>
  </div>


  <!-- douban ad begin -->
  <div id="dale_book_home_left_top" class="ad-placeholder" style="margin:-30px 0 30px;"></div>
  <!-- douban app end -->

  
    
    

    <div class="section book_information">
        <div class="hd">
            
  <h2 class=''>
    <span class="">图书资讯</span>
  </h2>

            <div class="slide-controls">
                <ol class="slide-dots">
                    <li><a data-index="1" href="#"></a></li>
                    <li><a data-index="2" href="#"></a></li>
                    <li><a data-index="3" href="#"></a></li>
                    <li><a data-index="4" href="#"></a></li>
                </ol>
                <div class="slide-btns">
                    <a href="#" class="prev information-prev">&#8249;</a>
                    <a href="#" class="next information-next">&#8250;</a>
                </div>
            </div>
        </div>
        <div class="bd">
            <div class="slide-block">
                <ul class="col slide-list">
                        <li class="slide-item info-block">
                            <a href="https://www.douban.com/note/743607069/">
                                <div class="cover" style="background-image: url(https://img9.doubanio.com/view/note/l/public/p67833936.jpg)"></div>
                                <div class="content">
                                    <span class="title">《生命暗章》| 性侵看起来很遥远，其实就在身边</span>
                                    <span class="meta">东方出版社</span>
                                    <p class="abstract">她坚信：除了犯罪本身，最具破坏性的事情之一就是不让人知道。所以就有了这场对个人创伤的最具挑战性的重述。在被侵犯近十年后，李怀瑜通过自己的作品，再现了她的经历，揭露了男性暴力的残酷性与破坏性，令人印...</p>
                                </div>
                            </a>
                        </li>
                        <li class="slide-item info-block">
                            <a href="https://book.douban.com/review/10638515/">
                                <div class="cover" style="background-image: url(https://img3.doubanio.com/view/subject/l/public/s33486124.jpg)"></div>
                                <div class="content">
                                    <span class="title">山村暮鸟小传：云一般漂泊，用一生寻找自己</span>
                                    <span class="meta">乐府文化</span>
                                    <p class="abstract">“云也又如我 / 如我一样 / 全然无措 / 因为这太宽太宽的 / 没有涯际的天 / 啊老子 / 在这样的时候 / 会笑眯眯地 / 突然出现吗&#34;——山村暮鸟诗碑 山村暮鸟（1884—1924），日本明治大正时期诗人、儿童文学作家，...</p>
                                </div>
                            </a>
                        </li>
                        <li class="slide-item info-block">
                            <a href="https://book.douban.com/review/10644561/">
                                <div class="cover" style="background-image: url(https://img3.doubanio.com/view/subject/l/public/s33496154.jpg)"></div>
                                <div class="content">
                                    <span class="title">不朽的土地，灵魂的故乡</span>
                                    <span class="meta">影随茵动</span>
                                    <p class="abstract">一句“烟花三月下扬州”，让中国这座江南之城名扬中外，而“京口瓜州一水间”的京口怕是知道的人就要少了很多，京口，即今日的镇江，与扬州一水相隔，遥相对望，没有扬州的繁花热闹，反而生出一种安静闲适，这里...</p>
                                </div>
                            </a>
                        </li>
                        <li class="slide-item info-block">
                            <a href="https://book.douban.com/review/12041968/">
                                <div class="cover" style="background-image: url(https://img3.doubanio.com/view/subject/l/public/s33489085.jpg)"></div>
                                <div class="content">
                                    <span class="title">作者后记 莫失莫忘</span>
                                    <span class="meta">大鱼读品</span>
                                    <p class="abstract">有没有一个可能，是我们的社会把“亲”与“子”绑得太紧了？ 在怪兽家长的背后，不过是站着一个胆怯的、害怕犯错的人啊。 这篇并不存在于原先设定的大纲中，然而，许多友人看完草稿，一致的回应是：你该着手写你...</p>
                                </div>
                            </a>
                        </li>
                </ul>
            </div>
        </div>
    </div>


  
    

  <div class="section popular-books">
    <div class="hd">
      <h2>
        <span>最受关注图书榜</span>
        <span class="link-more">
          <a href="/chart?subcat=F&amp;icn=index-topchart-fiction">虚构类»</a>
        </span>
        <span class="link-more">
          <a href="/chart?icn=index-topchart-nonfiction">非虚构类»</a>
        </span>
      </h2>
    </div>
    <div class="bd">
      <ul class="list-col list-col2 list-summary s"
        data-dstat-areaid="61" data-dstat-mode="click,expose">
              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/34461202/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s33474235.jpg"
          alt="企鹅的忧郁" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/34461202/?icn=index-topchart-subject" class="">企鹅的忧郁</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar40 star-img">
        </span>
        <span class="average-rating">
          8.0
        </span>
      </p>
      <p class="author">
        作者：[乌克兰] 安德烈·库尔科夫（Andrej Kurkow）
      </p>
      <p class="book-list-classification">
        乌克兰文学&nbsp;/&nbsp;荒诞
      </p>
      <p class="extra-info">
        
          <span class="meta-label">有电子书</span>
      </p>
        
        <p class="reviews">
          他将乌克兰政局的荒谬，社会的破败包裹在一个悬疑色彩的黑色喜剧之下。
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/10589583/?icn=index-topchart-subject">贾木许评论</a>)
        </p>
    </div>
  </li>

              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/33440205/?icn=index-topchart-subject">
        <img src="https://img9.doubanio.com/view/subject/m/public/s33492346.jpg"
          alt="你当像鸟飞往你的山" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/33440205/?icn=index-topchart-subject" class="">你当像鸟飞往你的山</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          9.0
        </span>
      </p>
      <p class="author">
        作者：[美]塔拉·韦斯特弗
      </p>
      <p class="book-list-classification">
        传记&nbsp;/&nbsp;教育
      </p>
      <p class="extra-info">
        
      </p>
        
        <p class="reviews">
          这不是一部励志成功学，作者最不想展露的一面恰恰是成功。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/10589105/?icn=index-topchart-subject">此刻评论</a>)
        </p>
    </div>
  </li>

              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/33658616/?icn=index-topchart-subject">
        <img src="https://img1.doubanio.com/view/subject/m/public/s33317677.jpg"
          alt="克莱因壶" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/33658616/?icn=index-topchart-subject" class="">克莱因壶</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.9
        </span>
      </p>
      <p class="author">
        作者：[日]冈岛二人
      </p>
      <p class="book-list-classification">
        科幻推理&nbsp;/&nbsp;日本
      </p>
      <p class="extra-info">
        
      </p>
        
        <p class="reviews">
          三十年前的宅男畅想。
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/10602360/?icn=index-topchart-subject">慕容复评论</a>)
        </p>
    </div>
  </li>

              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/34617780/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s33475751.jpg"
          alt="鸟瞰古文明" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/34617780/?icn=index-topchart-subject" class="">鸟瞰古文明</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar50 star-img">
        </span>
        <span class="average-rating">
          9.4
        </span>
      </p>
      <p class="author">
        作者：[法] 让-克劳德·戈尔万
      </p>
      <p class="book-list-classification">
        历史&nbsp;/&nbsp;绘本
      </p>
      <p class="extra-info">
        
      </p>
        
        <p class="reviews">
          戴上VR看历史。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/10570794/?icn=index-topchart-subject">Brahms评论</a>)
        </p>
    </div>
  </li>

              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/34429342/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s33445244.jpg"
          alt="我是个年轻人，我心情不太好" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/34429342/?icn=index-topchart-subject" class="">我是个年轻人，我心情不太好</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar40 star-img">
        </span>
        <span class="average-rating">
          7.7
        </span>
      </p>
      <p class="author">
        作者：[挪威] 阿澜·卢
      </p>
      <p class="book-list-classification">
        年轻人&nbsp;/&nbsp;挪威文学
      </p>
      <p class="extra-info">
        
          <span class="meta-label">有电子书</span>
      </p>
        
        <p class="reviews">
          这本书可不是一本堆砌烦恼的吐槽书，而是一本纾解心情的正能量小册。
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/10515151/?icn=index-topchart-subject">nadja评论</a>)
        </p>
    </div>
  </li>

              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/34786067/?icn=index-topchart-subject">
        <img src="https://img1.doubanio.com/view/subject/m/public/s33496317.jpg"
          alt="伦敦人" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/34786067/?icn=index-topchart-subject" class="">伦敦人</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.7
        </span>
      </p>
      <p class="author">
        作者：[加]克莱格·泰勒
      </p>
      <p class="book-list-classification">
        纪实&nbsp;/&nbsp;伦敦
      </p>
      <p class="extra-info">
        
      </p>
        
        <p class="reviews">
          人们不停地在伦敦追逐，却又被伦敦放逐。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/10566582/?icn=index-topchart-subject">Eudaemonia评论</a>)
        </p>
    </div>
  </li>

              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/33437511/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s33320962.jpg"
          alt="自指引擎" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/33437511/?icn=index-topchart-subject" class="">自指引擎</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          9.0
        </span>
      </p>
      <p class="author">
        作者：[日]圆城塔
      </p>
      <p class="book-list-classification">
        科幻&nbsp;/&nbsp;日本
      </p>
      <p class="extra-info">
        
      </p>
        
        <p class="reviews">
          什么样的书会让译者生不如死？
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/10211114/?icn=index-topchart-subject">丁丁虫评论</a>)
        </p>
    </div>
  </li>

              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/30217954/?icn=index-topchart-subject">
        <img src="https://img1.doubanio.com/view/subject/m/public/s33477929.jpg"
          alt="告别的仪式" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/30217954/?icn=index-topchart-subject" class="">告别的仪式</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.3
        </span>
      </p>
      <p class="author">
        作者：[法]西蒙娜·德·波伏瓦
      </p>
      <p class="book-list-classification">
        萨特&nbsp;/&nbsp;存在主义
      </p>
      <p class="extra-info">
        
      </p>
        
        <p class="reviews">
          这“最后的仪式”正是死亡和告别这一反应行为的终极延长。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/10611440/?icn=index-topchart-subject">梦魇马戏团评论</a>)
        </p>
    </div>
  </li>

              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/34792357/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s33456174.jpg"
          alt="无伤时代" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/34792357/?icn=index-topchart-subject" class="">无伤时代</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.8
        </span>
      </p>
      <p class="author">
        作者：童伟格
      </p>
      <p class="book-list-classification">
        台湾文学&nbsp;/&nbsp;小说
      </p>
      <p class="extra-info">
        
      </p>
        
        <p class="reviews">
          人和人之间接近于神的救赎。
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/10485720/?icn=index-topchart-subject">不是三步评论</a>)
        </p>
    </div>
  </li>

              
  

  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/34787187/?icn=index-topchart-subject">
        <img src="https://img9.doubanio.com/view/subject/m/public/s33464676.jpg"
          alt="日本侘寂" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/34787187/?icn=index-topchart-subject" class="">日本侘寂</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.7
        </span>
      </p>
      <p class="author">
        作者：[日]大西克礼
      </p>
      <p class="book-list-classification">
        日本文化&nbsp;/&nbsp;美学
      </p>
      <p class="extra-info">
        
      </p>
        
        <p class="reviews">
          读毕如同戴上一副眼镜，回头再来欣赏体现日本美学概念的种类繁多的艺术形式，视线就变得清晰起来。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/10590280/?icn=index-topchart-subject">重尔.张望评论</a>)
        </p>
    </div>
  </li>

      </ul>
    </div>
  </div>


  <!-- douban ad begin -->
  <div id="dale_book_home_left_middle" class="ad-placeholder" style="margin:-50px 0 30px;"></div>
  <!-- douban app end -->

  
  <div class="section market-books">
    <div class="hd">
      <h2>
        <span>豆瓣书店</span>
        <span class="link-more">
          <a href="https://market.douban.com/book/?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web">查看全部»</a>
        </span>
      </h2>
    </div>
    <div class="bd">
      
      <div class="top">
        <div class="cover">
          <a href="https://market.douban.com/book/greatideas?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web">
            <div class="pic" style="background-image: url(https://img3.doubanio.com/view/freyr_page_photo/raw/public/5041.jpg)"></div>
          </a>
        </div>
        <div id="market_books_header_info" class="info">
          <p class="title">伟大的思想（全六辑）
            <span class="price">￥899.00</span>
              <span class="free_delivery">／包邮 </span>
          </p>
          <p class="desc indent-paragraph" data-row="4"> 企鹅精编“小红书”，定制版帆布袋限量送</p>
        </div>
      </div>
      <ul class="list-col list-col5">
          
          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/Saragosse?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img3.doubanio.com/view/freyr_page_photo/raw/public/4993.jpg" width="106" height="140" alt="萨拉戈萨手稿"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/Saragosse?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">萨拉戈萨手稿</a>
              </div>
              <div class="price">￥89.00</div>
            </div>
          </li>
          
          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/tedchiang?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img1.doubanio.com/view/freyr_page_photo/raw/public/4969.jpg" width="106" height="140" alt="《你一生的故事》《呼吸》"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/tedchiang?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">《你一生的故事》《呼吸》</a>
              </div>
              <div class="price">￥64.00</div>
            </div>
          </li>
          
          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/godfather?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img1.doubanio.com/view/freyr_page_photo/raw/public/5079.jpg" width="106" height="140" alt="教父电影全剧本"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/godfather?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">教父电影全剧本</a>
              </div>
              <div class="price">￥98.00</div>
            </div>
          </li>
          
          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/wuzang?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img1.doubanio.com/view/freyr_page_photo/raw/public/4939.jpg" width="106" height="140" alt="宫本武藏全传"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/wuzang?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">宫本武藏全传</a>
              </div>
              <div class="price">￥279.00</div>
            </div>
          </li>
          
          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/beauvoir?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img3.doubanio.com/view/freyr_page_photo/raw/public/4680.jpg" width="106" height="140" alt="告别的仪式"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/beauvoir?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">告别的仪式</a>
              </div>
              <div class="price">￥58.00</div>
            </div>
          </li>
      </ul>
    </div>
  </div>


    <div class="section ebook-area"></div>

    <div id="reviews" class="section" ></div>

</div>
      <div class="aside">
        
  <!-- douban ad begin -->
  <div id="dale_book_home_top_right" class="s ad-placeholder"
    data-dstat-areaid="51" data-dstat-mode="click,expose"
    style="margin-top: 30px;"></div>
  <!-- douban ad end -->

  <!-- douban ad begin -->
  <div id="dale_book_home_top_right2" class="ad-placeholder"></div>
  <!-- douban ad end -->

  

  

  
  <h2 class=''>
    <span class="">热门标签</span>
      <span class="link-more">
        <a class="" href="/tag/?view=type&amp;icn=index-sorttags-all"
          >所有热门标签»</a>
      </span>
  </h2>

  <ul class="hot-tags-col5 s" data-dstat-areaid="54" data-dstat-mode="click,expose">
      
    

    <li>
        <ul class="clearfix">
            <li class="tag_title">
                文学
            </li>
            <li>
                <a href="/tag/小说" class="tag">小说</a>
            </li>
            <li>
                <a href="/tag/随笔" class="tag">随笔</a>
            </li>
            <li>
                <a href="/tag/日本文学" class="tag">日本文学</a>
            </li>
            <li class="last">
                  <a href="/tag/散文" class="tag">散文</a>
            </li>
            <li>
                <a href="/tag/诗歌" class="tag">诗歌</a>
            </li>
            <li>
                <a href="/tag/童话" class="tag">童话</a>
            </li>
            <li>
                <a href="/tag/名著" class="tag">名著</a>
            </li>
            <li class="last">
                  <a href="/tag/港台" class="tag">港台</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#文学" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>

      
    

    <li>
        <ul class="clearfix">
            <li class="tag_title">
                流行
            </li>
            <li>
                <a href="/tag/漫画" class="tag">漫画</a>
            </li>
            <li>
                <a href="/tag/推理" class="tag">推理</a>
            </li>
            <li>
                <a href="/tag/绘本" class="tag">绘本</a>
            </li>
            <li class="last">
                  <a href="/tag/青春" class="tag">青春</a>
            </li>
            <li>
                <a href="/tag/科幻" class="tag">科幻</a>
            </li>
            <li>
                <a href="/tag/言情" class="tag">言情</a>
            </li>
            <li>
                <a href="/tag/奇幻" class="tag">奇幻</a>
            </li>
            <li class="last">
                  <a href="/tag/武侠" class="tag">武侠</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#流行" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>

      
    

    <li>
        <ul class="clearfix">
            <li class="tag_title">
                文化
            </li>
            <li>
                <a href="/tag/历史" class="tag">历史</a>
            </li>
            <li>
                <a href="/tag/哲学" class="tag">哲学</a>
            </li>
            <li>
                <a href="/tag/传记" class="tag">传记</a>
            </li>
            <li class="last">
                  <a href="/tag/设计" class="tag">设计</a>
            </li>
            <li>
                <a href="/tag/建筑" class="tag">建筑</a>
            </li>
            <li>
                <a href="/tag/电影" class="tag">电影</a>
            </li>
            <li>
                <a href="/tag/回忆录" class="tag">回忆录</a>
            </li>
            <li class="last">
                  <a href="/tag/音乐" class="tag">音乐</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#文化" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>

      
    

    <li>
        <ul class="clearfix">
            <li class="tag_title">
                生活
            </li>
            <li>
                <a href="/tag/旅行" class="tag">旅行</a>
            </li>
            <li>
                <a href="/tag/励志" class="tag">励志</a>
            </li>
            <li>
                <a href="/tag/教育" class="tag">教育</a>
            </li>
            <li class="last">
                  <a href="/tag/职场" class="tag">职场</a>
            </li>
            <li>
                <a href="/tag/美食" class="tag">美食</a>
            </li>
            <li>
                <a href="/tag/灵修" class="tag">灵修</a>
            </li>
            <li>
                <a href="/tag/健康" class="tag">健康</a>
            </li>
            <li class="last">
                  <a href="/tag/家居" class="tag">家居</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#生活" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>

      
    

    <li>
        <ul class="clearfix">
            <li class="tag_title">
                经管
            </li>
            <li>
                <a href="/tag/经济学" class="tag">经济学</a>
            </li>
            <li>
                <a href="/tag/管理" class="tag">管理</a>
            </li>
            <li>
                <a href="/tag/商业" class="tag">商业</a>
            </li>
            <li class="last">
                  <a href="/tag/金融" class="tag">金融</a>
            </li>
            <li>
                <a href="/tag/营销" class="tag">营销</a>
            </li>
            <li>
                <a href="/tag/理财" class="tag">理财</a>
            </li>
            <li>
                <a href="/tag/股票" class="tag">股票</a>
            </li>
            <li class="last">
                  <a href="/tag/企业史" class="tag">企业史</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#经管" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>

      
    

    <li>
        <ul class="clearfix">
            <li class="tag_title">
                科技
            </li>
            <li>
                <a href="/tag/科普" class="tag">科普</a>
            </li>
            <li>
                <a href="/tag/互联网" class="tag">互联网</a>
            </li>
            <li>
                <a href="/tag/编程" class="tag">编程</a>
            </li>
            <li class="last">
                  <a href="/tag/交互设计" class="tag">交互设计</a>
            </li>
            <li>
                <a href="/tag/算法" class="tag">算法</a>
            </li>
            <li>
                <a href="/tag/通信" class="tag">通信</a>
            </li>
            <li>
                <a href="/tag/神经网络" class="tag">神经网络</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#科技" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>

  </ul>

    

'''
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
for result in results:
    print(result)