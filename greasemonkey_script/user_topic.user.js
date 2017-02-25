// ==UserScript==
// @name        user_test
// @namespace   test
// @description just test script
// @include     https://www.zhihu.com
// @version     1
// @require  //cdn.bootcss.com/jquery/3.1.1/jquery.min.js
// @require  //cdn.bootcss.com/jquery-dateFormat/1.0/jquery.dateFormat.min.js
// @grant none
// ==/UserScript==


String.prototype.format = function() {
    var formatted = this;
    for( var arg in arguments ) {
        formatted = formatted.replace("{" + arg + "}", arguments[arg]);
    }
    return formatted;
};

var topic = function (offset,limit,topics){
  $.ajax({
    method:"GET",
    url:"/followed_topics?offset={0}&limit={1}".format(offset, limit),
  }).done(topics)
};
//隐藏话题列表的最佳答案内容
var topic_title_list_display = function(){
  var topic_title_list = $("div.feed-content>div.entry-body");
  topic_title_list.css("display","none")
} 

var layout = function(width){
  //填满空间
  var content_html = $("div[role='main']");
  content_html.css("width","100%");
  //顶部空白
  var body_content = $("div.zhi.js-topic-feed-page.topic-feed-page");
  body_content.css("padding-top","5px");
  body_content.css("height",$("body").height()-20+"px");
  //左侧导航栏
  var zh_left_bar = $("div.zu-main-content>div.zu-main-content-inner");
  zh_left_bar.css("margin-right","{0}px".format(width));


 
  var zh_footer = $("#zh-footer");
  zh_footer.css("display","none")
  zh_left_bar.css("overflow-y","auto");
  zh_left_bar.css("height","100%");
  zh_left_bar.css("height",$(window).height()-45-5+"px");
  //右侧内容栏
  var right_bar_width = width - 30
  var zh_right_bar = $("div.zu-main-sidebar");
  zh_right_bar.css("margin-left","-{0}px".format(right_bar_width));
  zh_right_bar.css("width","{0}px".format(right_bar_width));
  zh_right_bar.css("height",$(window).height()-45-5+"px");

  zh_right_bar.css("overflow-y","auto");
  $("body").css("overflow","hidden");
  zh_right_bar.empty();

  
}
var item_layout = "";
var item_avatar = '<div class="avatar"><a data-hovercard="p$b${0}" class="zm-item-link-avatar" href="/people/{0}" target="_blank" ><img src="{1}" alt="摄影" class="side-topic-avatar"></a></div>';
var item_vote = '<div class="zm-votebar" data-za-module="VoteBar" style="display: inherit; margin-top:45px"><button class="up" aria-pressed="false" title="赞同"><i class="icon vote-arrow"></i><span class="count">{0}</span><span class="label sr-only">赞同</span></button><button class="down" aria-pressed="false" title="反对，不会显示你的姓名"><i class="icon vote-arrow"></i><span class="label sr-only">反对，不会显示你的姓名</span></button></div>';
var item_author = '<div class="zm-item-answer-author-info"><span class="summary-wrapper"><span class="author-link-line"><a class="author-link" data-hovercard="p$b${0}" target="_blank" href="/people/{0}">{1}</a><span class="icon icon-badge-best_answerer icon-badge" data-tooltip="s$b${2}"></span></span><span class="badge-summary"><a href="/people/{0}#hilightbadge" target="_blank">{3}</a></span></span></div>';
var item_expanded = '<p class="visible-expanded" style="display:inherit;"><a itemprop="url" class="answer-date-link meta-item" target="_blank" href="/question/{0}/answer/{1}">发布于 {2}</a></p>'



//详细信息显示
var question_display = function(data){
  var zh_right_bar = $("div.zu-main-sidebar");
  zh_right_bar.append("<div class='zu-main-feed-con navigable'><div id='zh_right_bar' class='topstory clearfix'></div></div>");
  data.map(function(currentValue,index){
    var item = $("#zh_right_bar");
    var item_time = new Date(currentValue.updated_time*1000);
    item.append("<div class='feed-item folding feed-item-hook'>"+
    "<div class='feed-item-inner myclass'>{0}<div class='feed-main'><div class='feed-content'><div> </div><div class='expandable entry-body'>{1}{2}<div class='zm-item-rich-text expandable js-collapse-body'>{3}{4}{5}</div></div></div></div></div>".format(
      item_avatar.format(currentValue.author.url_token,currentValue.author.avatar_url),item_vote.format(currentValue.voteup_count),
      item_vote.format(currentValue.voteup_count),
      item_author.format(currentValue.author.url_token,currentValue.author.name,currentValue.author.badge[0],currentValue.author.headline),
      currentValue.content,
      item_expanded.format(currentValue.question.id,currentValue.id,item_time.getFullYear()+'-'+item_time.getMonth()+'-'+item_time.getDay()))+"</div>");    
    })
    var zh_right_bar = $("div.zu-main-sidebar");
    zh_right_bar.on("scroll",function(){
    $("img.lazy").lazyload();
  })
}

//获取问题内容
var question = function(url_token){
  $.ajax({
    method:"GET",
    url:"/api/v4/questions/{0}/answers".format(url_token),
    data:{sort_by:"default",
    include:'data[*].is_normal,is_sticky,collapsed_by,suggest_edit,comment_count,collapsed_counts,reviewing_comments_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,mark_infos,created_time,updated_time,relationship.is_author,voting,is_thanked,is_nothelp,upvoted_followees;data[*].author.is_blocking,is_blocked,is_followed,voteup_count,message_thread_token,badge[?(type=best_answerer)].topics',
    limit:20,
    offset:0}
  }).done(function(data){
    //pagging(totals,next),data
    console.log(data);
    question_display(data.data);
  })
}
//绑定方法
var question_click = function(){
  var question_list = $("div.feed-main>div.feed-content>h2");
  question_list.on('click',function(){
    console.log($("a",this).attr("href"));
    var _href = $("a",this).attr("href");
    var url_token = _href.split("/")[2];
    
    //加载第一页
    question(url_token);

  })
}
$(document).ready(function(){
  
  //clearn body
  // var body = $(document.body);
  // body.empty();

  //top
  layout(900);
  topic_title_list_display();
  question_click();
  // topic(20,80,function(data){
  //   console.log(data);
  //   topic_display(data.payload);
  // });
  
})

