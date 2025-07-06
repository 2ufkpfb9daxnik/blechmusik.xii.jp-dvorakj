var _____WB$wombat$assign$function_____ = function(name) {return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name)) || self[name]; };
if (!self.__WB_pmw) { self.__WB_pmw = function(obj) { this.__WB_source = obj; return this; } }
{
  let window = _____WB$wombat$assign$function_____("window");
  let self = _____WB$wombat$assign$function_____("self");
  let document = _____WB$wombat$assign$function_____("document");
  let location = _____WB$wombat$assign$function_____("location");
  let top = _____WB$wombat$assign$function_____("top");
  let parent = _____WB$wombat$assign$function_____("parent");
  let frames = _____WB$wombat$assign$function_____("frames");
  let opener = _____WB$wombat$assign$function_____("opener");

$(function() {
    $("p:empty").remove();
});


$(function() {
//    var header = '<div class="navbar navbar-inverse navbar-static-top" id="header"><div class="container"><a class="navbar-brand" href="/">blechmusik.xii.jp</a><ul class="nav navbar-nav"><li class="active"><a href="/"><i class="fa fa-home"></i> Home</a></li><li><a href="/about/">About</a></li><li><a href="#contact">Contact</a></li></ul><form class="navbar-form pull-right" method="get" id="search_box" action="https://web.archive.org/web/20220930111726/https://www.google.co.jp/search"><input type="hidden" name="hl" value="ja"><input class="form-control" type="text" name="q" placeholder="search" value="" style="width: 250px;"><input type="submit" name="btng" value="Search" class="btn btn-small"><input type="hidden" name="domains" value="blechmusik.xii.jp"><input type="hidden" id="search1" name="sitesearch" value="blechmusik.xii.jp" checked="checked"></form></div></div>';
    var header = '<nav class="navbar navbar-expand-lg navbar-light bg-light" id="header">'
    			+ '<div class="container"><div class="collapse navbar-collapse" id="navbar">'
    			+ '<ul class="navbar-nav mr-auto"><li class="nav-item"><a class="nav-link" href="/">Home</a></li></ul>'
    			+ '<form class="form-inline" role="form" method="get" id="search_box" action="https://web.archive.org/web/20220930111726/https://www.google.co.jp/search"><input type="hidden" name="hl" value="ja" /><input class="form-control" type="text" name="q" placeholder="サイト内を検索" value="" /><input type="hidden" name="domains" value="blechmusik.xii.jp" /><input type="hidden" id="search1" name="sitesearch" value="blechmusik.xii.jp" checked="checked" /><button type="submit" value="Search" class="btn btn-success"> 検索</button></form>'
    			+ '</div></div></nav>';

    // <html lang="ja">
    $("html").attr("lang", "ja");

    $("h1").before(header);
    $("h1").after('<div id="last_updated">　<i class="fa fa-clock-o fa-lg"> Last Updated: '
    			+ '<span> </span' + '></div' + '><ul class="breadcrumb"' + '></ul' + '>');

    // 中央部分を .container で囲む
    $("nav#header").nextAll().wrapAll('<div class="container" id="content"></div>');
});




// breadcrumb: generate a new breadcrumb list
$(function() {
    // パンくずリストを取得
    var breadcrumb = $("span.breadcrumb-links").html();
    // wilikiのトップページならばh1のテキストを取得
    if (null == breadcrumb) {
        breadcrumb = $("h1").text();
    }
    // パンくずリストの表示箇所を変更
    var breadcrumb_links = '<a href="/">Home</a>:' + breadcrumb;
    var breadcrumb_links_arr = breadcrumb_links.split(":");
    for (var i = 0; i < breadcrumb_links_arr.length; i++) {
        if (i == (breadcrumb_links_arr.length - 1)) {
            breadcrumb_links_arr[i] = '<li class="active">' + breadcrumb_links_arr[i] + '</li>';
        } else {
            breadcrumb_links_arr[i] = "<li>" + breadcrumb_links_arr[i] + "</li>";
        }

    }

    // bootstrap用パンくずリストとして区切り文字を追加する
    $("ul.breadcrumb").append(breadcrumb_links_arr.join(' <span class="divider">　/　</span> '));

    // remove the original breadcrumb
    $("span.breadcrumb-links").remove();
});


// last updated: move last modified (last updated) from bottom to top 
$(function() {
    var last_updated = $("div[align='right']").last().text();
    $("div[align='right']").last().text("");
    $("div[align='right']:empty").remove();

    // edit ページの場合は更新日時が表示されない
    // 更新日時が全く表示されていなければ、更新日時を表示するスペースを取り除く
    if ("" == last_updated) {
        $("h1 + div").replaceWith("<div></div>");
    } else {
        // 更新日時を取得
        var date_of_last_updated = last_updated.split(" ")[3].replace(/\//g, "-");

        $("div#last_updated span").text(date_of_last_updated);
    }
});


// wiliki-tools: make div#wiliki_tools from div.right
$(function() {
    $("div[align='right']").attr("id", "wiliki_tools");
    $("div[align='right']").removeAttr("align");
});

$(function() {
    // remove extra hr
    $("div#wiliki_tools + hr").remove();
});


// for edit ================================================================================


// textarea の拡張
$(function() {
    $("textarea").addClass("input-block-level");
    $("textarea").addClass("form-control");
    // $("textarea").attr("rows", "30");
    $("textarea").removeAttr("cols");

    $("textarea").each(function(){
        var name_attr = $(this).attr("name");
        $(this).attr("id", name_attr);
        });

    $("textarea#content").attr("rows", 30);
    $("textarea#logmsg").attr("rows", 1);
});


// definition list
$(function() {
    $("dl").addClass("dl-horizontal");
});

// emphasis
$(function() {
    $("em").addClass("text-success");
    $("strong").addClass("text-warning");
});


// link for download -> button
$(function() {
    $("a[href$='dvorakj/download'], a[href$='dvorakj/download-src']").each(function() {
        var url = $(this).parent().html().match(/<a href="(.+?)">/)[1];
        var text = $(this).parent().text();

        var new_button = '<p>'
        // + '<button class="btn btn-large btn-primary">'
        // + '<a href="' + url + '" style="color:white">' + text + 'をダウンロードする</a>'
            + '<a href="' + url + '" class="btn btn-large btn-primary" style="color:white">'
            + '<i class="fa fa-download fa-lg"></i> '
            + text
            + 'をダウンロードする</a>'
        // + '</button>'
            + '</p>';

        // link text -> button text
        $(this).parent().parent().before(new_button);
        $(this).parent().remove();
    });
});



// descriptions of delete line, [[$$use-mathjax]], [[$$include pagename]]
$(function() {
    $("p").each(function(){
        if ("No HTML." == $(this).text()) {
            $(this)
            .after("<p>Surround words by three plus signs (＋＋＋foo＋＋＋) to <del>delete</del>.</p>")
            .after("<p>[[$$use-mathjax]] turns on MathJax.</p>")
            .after("<p>[[$$include pagename]] includes the page of that 'pagename'.</p>");
        }
    });

    // changing +++test+++ to <del>test</del>
    var match_pattern = /\+\+\+(.+?)\+\+\+/g;
    $("p, li").each(function(){
        if ($(this).html().match(match_pattern)) {
            var result = $(this).html().replace(/\+\+\+(.+?)\+\+\+/g, "<del>$1</del>");
            $(this).html(result);
        }
    });
});



// text formatting rules
$(function() {
    $("h2").each(function(){
        if ("Text Formatting Rules" == $(this).text())
        {
            $(this).prev().nextAll().wrapAll("<div class='alert alert-info'></div>");
        };
    });
});

// end for edit ================================================================================


// breadcrumb ======================================================================
// "miscellaneous memo" -> "misc"
$(function() {
    $("ul.breadcrumb li a").each(function(){
        if ("miscellaneous memo" == $(this).text()) {
            $(this)
            .attr("href", "./")
            .text("misc");
        }
    });
});



// h2 and h3 ======================================================================
// descriptions of delete line, [[$$use-mathjax]], [[$$include pagename]]
$(function() {
    $("h2").each(function(){
        $(this).addClass("alert alert-success");
    });
    
    $("h3").each(function(){
        $(this).addClass("alert alert-info");
    });
});


// margin for h2
$(function() {
    $("h2:first").each(function() {
            $(this).css("margin-top", "5%");
        });
    $("h2:not(:first)").each(function() {
            $(this).css("margin-top", "10%");
        });
});


// ================================================================================

$(function() {
    // ヘッダーとフッター以外を div.body-content と div.row  で囲む
    $("div#content > *").wrapAll("<div class='body-content'><div class='row'><div id='entry' class='entry'></div></div></div>");
});


//  div#entry の直後に目次表示用スペースを確保する
$(function() {
    $("div.entry").after("<div id='toc'></b>");
});


// table
$(function() {
    // td => th
    $('td').each(function(){
        var txt = $(this).html();
        if (txt.match(/^\* /g)) {
            $(this).replaceWith("<th>" + txt.replace(/^\* (.+)/g, "$1") + "</th>");
        }
    });

    $("div#entry table").addClass("table table-bordered table-striped table-condensed");
    $("div#entry table th").addClass("warning");
    $("div#entry table th").addClass("text-success text-center");
});



}
/*
     FILE ARCHIVED ON 11:17:26 Sep 30, 2022 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 04:37:53 Jul 06, 2025.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.528
  exclusion.robots: 0.018
  exclusion.robots.policy: 0.008
  esindex: 0.008
  cdx.remote: 8.244
  LoadShardBlock: 60.307 (3)
  PetaboxLoader3.datanode: 77.573 (4)
  load_resource: 891.188
  PetaboxLoader3.resolve: 819.134
*/