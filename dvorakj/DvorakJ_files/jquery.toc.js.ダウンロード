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

$(function(){
	var data = ['<span class="badge badge-secondary">目次</span>'];
	
	var id = "";
	var text = "";
	var numForRepeat = 0;
	var spaces = "";
	
	$('h2, h3, h4, h5').each(function(){
		// h2 なら 0回, h3 なら 1回, ...
		numForRepeat = $(this).prop("tagName").slice(-1) - 2;
		spaces = '    '.repeat(numForRepeat);

		id = $(this).attr('id');
		text = $(this).text();

		data.push(spaces + "    " + "<a href='#" +  id + "'>" + text + "</a>");
	});
	
    $("h2:first").before("<pre id='toc'>" + data.join("\n") + "</pre>");
    $("#toc").css("background-color", "#f4f4f4");
});


$(function () {
	$("#entry").wrap("<div class='container'><div class='row'><div class='col-md-10 offset-md-1 col-lg-10 offset-lg-1'></div></div></div>");
});



}
/*
     FILE ARCHIVED ON 05:18:32 Nov 07, 2022 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 04:36:20 Jul 06, 2025.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.466
  exclusion.robots: 0.017
  exclusion.robots.policy: 0.008
  esindex: 0.011
  cdx.remote: 27.708
  LoadShardBlock: 97.152 (3)
  PetaboxLoader3.datanode: 167.461 (5)
  load_resource: 324.881 (2)
  PetaboxLoader3.resolve: 215.873 (2)
*/