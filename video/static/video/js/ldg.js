var timeout = 500;
var closetimer = 0;
var ddmenuitem = 0;

function mopen(id) {
	mcancelclosetime();
	if (ddmenuitem) ddmenuitem.style.visibility = 'hidden';
	ddmenuitem = document.getElementById(id);
	ddmenuitem.style.visibility = 'visible'
}
function mclose() {
	if (ddmenuitem) ddmenuitem.style.visibility = 'hidden'
}
function mclosetime() {
	closetimer = window.setTimeout(mclose, timeout)
}
function mcancelclosetime() {
	if (closetimer) {
		window.clearTimeout(closetimer);
		closetimer = null
	}
}
document.onclick = mclose;

function checkAll(str, checked) {
	//var a = document.getElementsByName(str);
	var a=$("#"+str).find("li input");
	var n = a.length;
	for (var i = 0; i < n; i++) {
		a[i].checked = checked
	}
}
/**老大哥copy代码QQ：788 47 023*/
$(function(){
	InitCopy();
	$(".copy1").each(function(){
		$(this).click(function(){
			var id=$(this).parent().attr("id");
			var copystr= GetCopyStr(id,1);
			CopyText(copystr);
		});
	});
	$(".copy2").each(function(){
		$(this).click(function(){
			var id=$(this).parent().attr("id");
			var copystr= GetCopyStr(id,2);
			CopyText(copystr);
		});
	});
	$(".copy3").each(function(){
		$(this).click(function(){
			var id=$(this).parent().attr("id");
			var copystr= GetCopyStr(id,3);
			CopyText(copystr);
		});
	});
});
function GetCopyStr(str,type) {
	var a=$("#"+str).find("li input");
	var n = a.length;
	var ldgcopystr = "";
	var suf=$("#"+str).find(".suf").text();
	if(suf=="迅雷下载"){suf="down";}
	for (var i = 0; i < n; i++) {
		if (a[i].checked) {
			if(type==2)
			{
				ldgcopystr += a[i].parentNode.innerText;
			}else if(type==3)
			{
				ldgcopystr += a[i].parentNode.innerText+"$"+suf;
			}else
			{
				ldgcopystr += a[i].value;
			}
			ldgcopystr += "<br/>";
		}
	}
	return ldgcopystr;

}
function InitCopy()
{
        var self = this;
        var element = document.body;
        var oDiv = document.createElement('div');
        oDiv.innerHTML = "ldg";
        oDiv.id = 'copyContent';
        oDiv.style.opacity = 0;
        oDiv.style.position = 'fixed';
        oDiv.style.zIndex = '-9999';
        element.appendChild(oDiv);
}
function CopyText(copytext){
        var self = this;
        var info = "";
        var flag;
        var ua = self.ua;
        try{
			
            var content = document.getElementById('copyContent');
			content.innerHTML=copytext;
            var selection = window.getSelection();
            var range = document.createRange();
            range.selectNodeContents(content);
            selection.removeAllRanges();
            selection.addRange(range);
            var resultCopy = document.execCommand('Copy', false, null);
            if(resultCopy || ua.indexOf("UCBrowser") > -1){
                flag = true;
            }else{
                flag = false;
            }

        }catch(e){
            flag = false;
        }
		if(flag)
		{
			alert("复制成功");
		}else{
			alert("复制失败,请手动选中复制");
		}
        return flag;
}