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

// JavaScript による日付・時刻・時間の計算・演算のまとめ - hoge256ブログ
// http://www.hoge256.net/2007/08/64.html
/**
 * 2つの日付の差を求める関数
 * year1 1つのめ日付の年
 * month1 1つめの日付の月
 * day1 1つめの日付の日
 * year2 2つのめ日付の年
 * month2 2つめの日付の月
 * day2 2つめの日付の日
 */
function compareDate(year1, month1, day1, year2, month2, day2) {
    var dt1 = new Date(year1, month1 - 1, day1);
    var dt2 = new Date(year2, month2 - 1, day2);
    var diff = dt1 - dt2;
    var diffDay = diff / 86400000;//1日は86400000ミリ秒
    return diffDay;
}


function result_of_comparingDate(date1, date2) {
    var date1arr = date1.split("-");
    var date2arr = date2.split("-");
    
    var day = Math.abs(compareDate(date1arr[0], date1arr[1], date1arr[2], date2arr[0], date2arr[1], date2arr[2]));


    switch (day) {
        case 0:
            return "今日";
            break;
        case 1:
            return "昨日";
            break;
        default:
            break;
    }

    if (day < 31) {
        return day + "日前";
    }

    if (day < 365) {
        return Math.floor(day / 30) + "ヶ月前";
    }

    
    return Math.floor(day / 365) + "年前";
}


$(function() {
    // 更新日時の表示箇所を変更する
    // last_updated を文字列で取得
    var date_of_last_updated = $("div#last_updated span").text();



    // 更新日時が表示されている場合に限り、更新日時の情報を書き換える
    if ("" == date_of_last_updated) {
        return;
    }

    // // 更新日時を取得
    // var date_of_last_updated = last_updated.split(" ")[3].replace(/\//g, "-");
    // // 2013/06/16 => 2013-06-16

    // ウェブページを開いた当日の日付を取得
    var date = new Date();
    var yy = date.getFullYear();
    var mm = ('0' + (date.getMonth() + 1)).slice(-2);
    var dd = ('0' + date.getDate()).slice(-2);
    var date_of_today = [yy, mm, dd].join("-");

    var diff_of_date = result_of_comparingDate(date_of_last_updated, date_of_today);
    

    // last updated: 2014年01月21日 （618日前）
    $("div#last_updated span").text(date_of_last_updated.replace(/(\d{4})-(\d{2})-(\d{2})/g, "$1年$2月$3日") + " （" + diff_of_date + "）");

    
    // "last updated" という文字列を
    // 日本語の「最終更新日」という文字列に変換する
    // このページの最終更新日：　 2014年01月21日 （618日前）
    $("div#last_updated").html($("div#last_updated").html().replace(/last.+:/g, "最終更新日：　"));

});


}
/*
     FILE ARCHIVED ON 15:31:53 Mar 28, 2024 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 04:36:51 Jul 06, 2025.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 1.397
  exclusion.robots: 0.019
  exclusion.robots.policy: 0.009
  esindex: 0.013
  cdx.remote: 6.164
  LoadShardBlock: 71.338 (3)
  PetaboxLoader3.datanode: 3043.245 (4)
  load_resource: 4797.59
  PetaboxLoader3.resolve: 1285.262
*/