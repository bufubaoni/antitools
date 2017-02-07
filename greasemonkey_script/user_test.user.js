// ==UserScript==
// @name        user_test
// @namespace   test
// @description just test script
// @include     https://www.zhihu.com
// @version     1
// @grant       none
// ==/UserScript==
// @require  //cdn.bootcss.com/jquery/3.1.1/jquery.min.js

var home_entry = $("div.HomeEntry,div#zh-home-list-title");
home_entry.css("display","none");
var body_content = $("div.zg-wrap.zu-main.clearfix ")
body_content.css("padding-top","5px")
$("body").css("overflow","hidden");
var content_html = $("div[role='main']");
content_html.css("width","100%");

var question_list = $("#js-home-feed-list>div.feed-item>div.feed-item-inner>div.avatar,"+
"#js-home-feed-list>div.feed-item>div.feed-item-inner>div.feed-main>div>div.expandable.entry-body,"+
"#js-home-feed-list>div.feed-item>div.feed-item-inner>div.feed-main>div>div.feed-meta");
question_list.css("display","none");

var zh_main_content = $("div.zu-main-content>div.zu-main-content-inner");
zh_main_content.css("margin-right","900px");

$(window).off("scroll");
zh_main_content.css("overflow-y","auto");
zh_main_content.css("height",$(window).height()+"px");

var zh_right_bar = $("div.zu-main-sidebar");
zh_right_bar.css("margin-left","-870px");
zh_right_bar.css("width","870px");
zh_right_bar.css("height",$(window).height()+"px");
zh_right_bar.css("overflow-y","auto");

zh_right_bar.empty();

$(document).ajaxSuccess(function() {
  var todo2 = $("h2.feed-title>a.question_link");
  todo2.css("color","red");
  var todo = $("h2.feed-title>a.post-link");
  todo.css("color","red");
});

var question_list_title = $("div.feed-item-inner");

question_list_title.on("click",function(){
  zh_right_bar.empty();
  zh_right_bar.append("<p>"+$("div.feed-main>div.feed-content>div.expandable.entry-body>div.zm-item-rich-text>textarea",this).text()+"</p>");
})