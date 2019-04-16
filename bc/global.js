/**
 * 时间对象的格式化;
 */
Date.prototype.format = function (format) {
    /*
     * eg:format="yyyy-MM-dd hh:mm:ss";
     */
    var o = {
        "M+": this.getMonth() + 1, // month
        "d+": this.getDate(), // day
        "h+": this.getHours(), // hour
        "m+": this.getMinutes(), // minute
        "s+": this.getSeconds(), // second
        "q+": Math.floor((this.getMonth() + 3) / 3), // quarter
        "S": this.getMilliseconds()
        // millisecond
    }

    if (/(y+)/.test(format)) {
        format = format.replace(RegExp.$1, (this.getFullYear() + "").substr(4
            - RegExp.$1.length));
    }

    for (var k in o) {
        if (new RegExp("(" + k + ")").test(format)) {
            format = format.replace(RegExp.$1, RegExp.$1.length == 1
                ? o[k]
                : ("00" + o[k]).substr(("" + o[k]).length));
        }
    }
    return format;
}
var config = {
    DEBUG: false,
    ToastTimeLength: 1500
};
var Tools = {
    error: function (str) {
        if (typeof(str) == "string") {
            alert(str);
        }
    },
    success: function (str) {
        if (typeof(str) == "string") {
            alert(str);
        }
    },
    toast: function (str) {
        if (typeof(str) == "string") {
            alert(str);
        }
    },
    log: function (str) {
        if (config.DEBUG) {
            console.log(str);
        }
    },
    sleep: function (numberMillis) {
        var now = new Date();
        var exitTime = now.getTime() + numberMillis;
        while (true) {
            now = new Date();
            if (now.getTime() > exitTime)
                return;
        }
    },
    formatDate: function (str) {
        str = parseInt(str);
        var now = new Date(str);
        var year = now.getFullYear();
        var month = now.getMonth() + 1;
        var date = now.getDate();
        var hour = now.getHours();
        var minute = now.getMinutes();
        var second = now.getSeconds();

        money = month < 10 ? '0' + month : month;
        date = date < 10 ? '0' + date : date;
        hour = hour < 10 ? '0' + hour : hour;
        minute = minute < 10 ? '0' + minute : minute;
        second = second < 10 ? '0' + second : second;
        return year + "-" + month + "-" + date + " " + hour + ":" + minute + ":" + second;
    },
    formatDateChinese: function (str) {
        str = parseInt(str);
        var now = new Date(str);
        var year = now.getFullYear();
        var month = now.getMonth() + 1;
        var date = now.getDate();
        var hour = now.getHours();
        var minute = now.getMinutes();
        var second = now.getSeconds();
        return year + "年" + month + "月" + date + "日" + hour + "时" + minute + "分" + second + "秒";
    },
    diffDateChinese: function (time1, time2) {
        var total = (time2 - time1) / 1000;
        var hour = Math.floor(total / (60 * 60));
        var minute = Math.floor((total - hour * 60 * 60) / 60);
        var second = Math.floor(total % 60);
        return hour + "时" + minute + "分" + second + "秒";
    },
    null2Str: function (str) {
        return str || '';
    },
    parseInt: function (str) {
        return parseInt(str, 10);
    }
}

var ajaxRequest = function (obj) {
    var data = new Array();
    if (typeof obj.data != "undefined") {    //typeof 可以用来检测给定变量的数据类型，可能的返回值：1. 'undefined' --- 这个值未定义
        data = obj.data;
    }

    var requestStr = obj.url;
    if (requestStr.indexOf("?") > 0) {   //indexOf() 方法可返回某个指定的字符串值在字符串中首次出现的位置
        requestStr += "&";
    } else {
        requestStr += "?";
    }

    var type;
    if (typeof obj.type == 'undefined') {
        type = 'POST';
    } else {
        type = obj.type;
    }

    var dataType;
    if (typeof obj.dataType == 'undefined') {
        dataType = 'json';
    } else {
        dataType = obj.dataType;
    }

    requestStr += "timestamp=" + new Date().getTime();
    $.ajax({
        type: type,
        url: requestStr,
        dataType: dataType,
        data: data,
        timeout: 60000,
        success: function (json) {
            Tools.log(requestStr + "-success:");
            Tools.log(json);

            if (typeof(obj.success) == "function") {
                obj.success(json);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            Tools.log(requestStr + "-error");
            Tools.log({
                "XMLHttpRequest": XMLHttpRequest,
                "textStatus": textStatus,
                "errorThrown": errorThrown
            });

            if (textStatus == 'timeout') {
                // Tools.toast("操作超时，请联系管理员");
            } else {
                // Tools.toast("服务器异常，请联系管理员");
            }

            if (typeof(obj.error) == "function") {
                obj.error(XMLHttpRequest, textStatus, errorThrown);
            }
        },
        beforeSend: function () {
            Tools.log(requestStr + "-beforeSend");
            if (typeof(obj.beforeSend) == "function") {
                obj.beforeSend();
            }
        },
        complete: function () {
            Tools.log(requestStr + "-complete");
            if (typeof(obj.complete) == "function") {
                obj.complete();
            }
        }
    });
}

function add(a, b) {
    var c, d, e;
    try {
        c = a.toString().split(".")[1].length;
    } catch (f) {
        c = 0;
    }
    try {
        d = b.toString().split(".")[1].length;
    } catch (f) {
        d = 0;
    }
    return e = Math.pow(10, Math.max(c, d)), (mul(a, e) + mul(b, e)) / e;
}

function sub(a, b) {
    var c, d, e;
    try {
        c = a.toString().split(".")[1].length;
    } catch (f) {
        c = 0;
    }
    try {
        d = b.toString().split(".")[1].length;
    } catch (f) {
        d = 0;
    }
    return e = Math.pow(10, Math.max(c, d)), (mul(a, e) - mul(b, e)) / e;
}

function mul(a, b) {
    var c = 0,
        d = a.toString(),
        e = b.toString();
    try {
        c += d.split(".")[1].length;
    } catch (f) {
    }
    try {
        c += e.split(".")[1].length;
    } catch (f) {
    }
    return Number(d.replace(".", "")) * Number(e.replace(".", "")) / Math.pow(10, c);
}

function div(a, b) {
    var c, d, e = 0,
        f = 0;
    try {
        e = a.toString().split(".")[1].length;
    } catch (g) {
    }
    try {
        f = b.toString().split(".")[1].length;
    } catch (g) {
    }
    return c = Number(a.toString().replace(".", "")), d = Number(b.toString().replace(".", "")), mul(c / d, Math.pow(10, f - e));
}
function getRequest(url) {
    var theRequest = [];
    if (url.indexOf("?") != -1) {   //如果要检索的字符串值没有出现，则该方法返回 -1
        var str = url.substr(url.indexOf("?") + 1);
        strs = str.split("&");
        for (var i = 0; i < strs.length; i++) {
            theRequest.push({
                key: strs[i].split("=")[0],
                value: unescape(strs[i].split("=")[1])
            });
        }
    }
    return theRequest;
}
// 获取万、千、百、十、个固定位数的个数所组成5位所有组合
function getNewArrs(wanA, qianA, baiA, shiA, geA) {
    var wArr = [], qArr = [], bArr = [], sArr = [], gArr = [];
    wArr = wanA;
    qArr = qianA;
    bArr = baiA;
    sArr = shiA;
    gArr = geA;
    var tempArr = [];
    for (var w = 0; w < wArr.length; w++) {
        for (var q = 0; q < qArr.length; q++) {
            for (var b = 0; b < bArr.length; b++) {
                for (var s = 0; s < sArr.length; s++) {
                    for (var g = 0; g < gArr.length; g++) {
                        tempArr.push(wArr[w] + "" + qArr[q] + "" + bArr[b] + "" + sArr[s] + "" + gArr[g]);
                    }
                }
            }
        }
    }
    return tempArr;
}

// 获取千、百、十、个固定位数的个数所组成4位所有组合
function getFourNewArrs(qianA, baiA, shiA, geA) {
    var qArr = [], bArr = [], sArr = [], gArr = [];
    qArr = qianA;
    bArr = baiA;
    sArr = shiA;
    gArr = geA;
    var tempArr = [];
    for (var q = 0; q < qArr.length; q++) {
        for (var b = 0; b < bArr.length; b++) {
            for (var s = 0; s < sArr.length; s++) {
                for (var g = 0; g < gArr.length; g++) {
                    tempArr.push(qArr[q] + "" + bArr[b] + "" + sArr[s] + "" + gArr[g]);
                }
            }
        }
    }
    return tempArr;
}


//去掉数组重复
Array.prototype.uniqueArr = function () {
    var temp = new Array();
    this.sort();
    for(i = 0; i < this.length; i++) {
        if( this[i] == this[i+1]) {
            continue;
        }
        temp[temp.length]=this[i];
    }
    return temp;
}

// 获取百、十、个固定位数的个数所组成(后三直选--后三组合)
function getHszhNewArrs(baiA, shiA, geA) {
    var bArr = [], sArr = [], gArr = [];
    bArr = baiA;
    sArr = shiA;
    gArr = geA;
    var tempArr = [];
    for (var b = 0; b < bArr.length; b++) {
        for (var s = 0; s < sArr.length; s++) {
            for (var g = 0; g < gArr.length; g++) {
                tempArr.push(bArr[b] + "" + sArr[s] + "" + gArr[g]);
                tempArr.push(sArr[s] + "" + gArr[g]);
                tempArr.push(gArr[g]);
            }
        }
    }
    return tempArr;
}

// 判断一个字符串是否都为数字
function isAllNaN(str) {
    for (var i = 0; i < str.length; i++) {
        if (isNaN(str.charAt(i))) {
            return 0;
        }
    }
    return 1;
}

/**
 * 获得从m中取n的所有组合
 */
function getFlagArrs(arr, num) {
    if (arr.length < num) {
        return [];
    }
    var list = [];
    var sb = "";
    var b = new Array();
    for (var i = 0; i < arr.length; i++) {
        if (i < num) {
            b[i] = "1";
        } else
            b[i] = "0";
    }

    var point = 0;
    var nextPoint = 0;
    var count = 0;
    var sum = 0;
    var temp = "1";
    while (true) {
        // 判断是否全部移位完毕
        for (var i = b.length - 1; i >= b.length - num; i--) {
            if (b[i] == "1")
                sum += 1;
        }
        // 根据移位生成数据
        for (var i = 0; i < b.length; i++) {
            if (b[i] == "1") {
                point = i;
                sb += arr[point];
                sb += " ";
                count++;
                if (count == num)
                    break;
            }
        }
        // 往返回值列表添加数据
        list.push(sb);

        // 当数组的最后num位全部为1 退出
        if (sum == num) {
            break;
        }
        sum = 0;

        // 修改从左往右第一个10变成01
        for (var i = 0; i < b.length - 1; i++) {
            if (b[i] == "1" && b[i + 1] == "0") {
                point = i;
                nextPoint = i + 1;
                b[point] = "0";
                b[nextPoint] = "1";
                break;
            }
        }
        // 将 i-point个元素的1往前移动 0往后移动
        for (var i = 0; i < point - 1; i++)
            for (var j = i; j < point - 1; j++) {
                if (b[i] == "0") {
                    temp = b[i];
                    b[i] = b[j + 1];
                    b[j + 1] = temp;
                }
            }
        // 清空 StringBuffer
        sb = "";
        count = 0;
    }
    for (var i = 0; i < list.length; ++i) {
        list[i] = $.trim(list[i]);
    }
    return list;
}

function windowOpenBlank(url) {
    window.open(url, '_blank');
}

// function openGcdt(url) {
//     goSubUrl(CONFIG.BASEURL + "ssc/gcdt/" + url + ".html");
// }
//
// // 读取子页面
// function getPage(url) {
//     showLoading();
//     $("#rightContent").attr("src", url);
// }
//
// // 读取子页面
// function goSubUrl(url, params) {
//     var turl = url + "?timestamp=" + (new Date()).getTime();
//     var surl = CONFIG.BASEURL + "ssc/gcdt/LHC.html#url=" + url;
//
//     if (typeof params != 'undefined') {
//         var tmp = params.split("&");
//         $.each(tmp, function (index, value) {
//             turl += "&" + value.key + "=" + value.value;
//             surl += "&" + value.key + "=" + value.value;
//         });
//     }
//     window.parent.location.href = surl;
//     getSubPage();
// }
//
// function getSubPage() {
//     var surl = window.parent.location.href.toString();
//     var paramArr = surl.split("#");
//     var turl = "";
//     var tparam = "?timestamp=" + (new Date()).getTime();
//     if (paramArr) {
//         paramArr = paramArr[1];
//         if (paramArr) {
//             paramArr = paramArr.split("&");
//
//             $.each(paramArr, function (index, value) {
//                 var tmp = value.split("=");
//                 var key = tmp[0];
//                 var v = tmp[1];
//
//                 if (key == "url") {
//                     turl = v;
//                 } else {
//                     tparam += "&" + key + "=" + v;
//                 }
//             });
//         }
//     }
//
//     if (!turl) {
//         turl = CONFIG.BASEURL + "ssc/gcdt/gcdt.html";
//     }
//     getPage(turl + tparam);
// }

function windowOpen(url, title, width, height) {
    var top = (window.screen.height - 30 - height) / 2; //获得窗口的垂直位置;
    var left = (window.screen.width - 10 - width) / 2; //获得窗口的水平位置;
    var win = window.open(url, title, 'height=' + height + ',innerHeight=' + height + ',width=' + width + ',innerWidth=' + width + ',top=' + top + ',left=' + left + ',fullscreen=1,toolbar=no,menubar=no,scrollbars=auto,resizeable=no,location=no,status=no');
    win.focus();
}

// 生肖号码计算
var sx = ["猴", "鸡", "狗", "猪", "鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊"];
var sxArr = [];
// var startIndex = (new Date('<fmt:formatDate value="${serverTime}" pattern="yyyy-MM-dd HH:mm:ss"/>')).getFullYear() % 12;
var date = new Date();
var year = date.getFullYear();  //表示年份的四位数字
if (date.getTime() < (new Date('2018-2-16 00:00:00')).getTime()) {
    year = 2017;
}
var startIndex = year % 12;
for (var i = startIndex, count = 0; count < 12; i = (i + 1) % 12, ++count) {
    sxArr[count] = {
        name: sx[i],
        number: null
    };
}
sxArr[0].number = [1, 13, 25, 37, 49];
sxArr[1].number = [12, 24, 36, 48];
sxArr[2].number = [11, 23, 35, 47];
sxArr[3].number = [10, 22, 34, 46];
sxArr[4].number = [9, 21, 33, 45];
sxArr[5].number = [8, 20, 32, 44];
sxArr[6].number = [7, 19, 31, 43];
sxArr[7].number = [6, 18, 30, 42];
sxArr[8].number = [5, 17, 29, 41];
sxArr[9].number = [4, 16, 28, 40];
sxArr[10].number = [3, 15, 27, 39];
sxArr[11].number = [2, 14, 26, 38];
function getSxName(value) {
    for (var i = 0; i < sxArr.length; ++i) {
        var name = sxArr[i].name;
        for (var j = 0; j < sxArr[i].number.length; ++j) {
            if (sxArr[i].number[j] == parseInt(value)) {
                return name;
            }
        }
    }
    return "";
}
function getSxValue(name) {
    for (var i = 0; i < sxArr.length; ++i) {
        var sxName = sxArr[i].name;
        if (name == sxName) {
            return sxArr[i].number;
        }
    }
    return [];
}

// 红绿蓝
var hongboArr = [1, 2, 7, 8, 12, 13, 18, 19, 23, 24, 29, 30, 34, 35, 40, 45, 46];
var lanboArr = [3, 4, 9, 10, 14, 15, 20, 25, 26, 31, 36, 37, 41, 42, 47, 48];
var lvboArr = [5, 6, 11, 16, 17, 21, 22, 27, 28, 32, 33, 38, 39, 43, 44, 49];
function getBose(value) {
    for (var i = 0; i < hongboArr.length; ++i) {
        if (hongboArr[i] == parseInt(value)) {
            return 0;
        }
    }
    for (var j = 0; j < lanboArr.length; ++j) {
        if (lanboArr[j] == parseInt(value)) {
            return 1;
        }
    }
    for (var i = 0; i < lvboArr.length; ++i) {
        if (lvboArr[i] == parseInt(value)) {
            return 2;
        }
    }
}
function toFixed(value, scale, isUp) {
    if (isUp) {
        return value.toFixed(scale);
    } else {
        for (var i = 0; i < scale; ++i) {
            value *= 10;
        }
        value = parseInt(value);
        for (var i = 0; i < scale; ++i) {
            value /= 10;
        }
        return value.toFixed(scale);
    }
}

function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null)return unescape(r[2]);
    return null;
}

function FC3D_Auto(num , type){
    var zh = parseInt(num[0])+parseInt(num[1])+parseInt(num[2]);
    if(type==0){
        return zh;
    }

    if(type==1 || type==2 || type==3){//第一~三球大小

        if(type==1)qnum = parseInt(num[0]);
        if(type==2)qnum = parseInt(num[1]);
        if(type==3)qnum = parseInt(num[2]);

        if(qnum>=5){
            return '<font class="color-red">大</font>';
        }else{
            return '小';
        }
    }

    if(type==4 || type==5 || type==6){
        if(type==4)qnum = parseInt(num[0]);
        if(type==5)qnum = parseInt(num[1]);
        if(type==6)qnum = parseInt(num[2]);

        if(qnum%2==0){
            return '<font class="color-red">双</font>';
        }else{
            return '单';
        }
    }

    if(type==7){//总和大小
        if(zh>=14){
            return '<font class="color-red">总和大</font>';
        }else{
            return '总和小';
        }
    }

    if(type==8){//总和双单
        if(zh%2==0){
            return '<font class="color-red">总和双</font>';
        }else{
            return '总和单';
        }
    }

    if(type==9){
        if(parseInt(num[0])>parseInt(num[2])){
            return '<font class="color-red">龙</font>';
        }
        if(parseInt(num[0])<parseInt(num[2])){
            return '虎';
        }
        if(parseInt(num[0])==parseInt(num[2])){
            return '和';
        }
    }

    if(type==10){
        var n1=parseInt(num[0]);
        var n2=parseInt(num[1]);
        var n3=parseInt(num[2]);
        if((n1==0 || n2==0 || n3==0) && (n1==9 || n2==9 || n3==9)){
            if(n1==0){
                n1=10;
            }
            if(n2==0){
                n2=10;
            }
            if(n3==0){
                n3=10;
            }
        }

        if(n1==n2 && n2==n3){
            return "豹子";
        }else if((n1==n2) || (n1==n3) || (n2==n3)){
            return "对子";
        }else if((n1==10 || n2==10 || n3==10) && (n1==9 || n2==9 || n3==9) && (n1==1 || n2==1 || n3==1)){
            return "顺子";
        }else if( ( (Math.abs(n1-n2)==1) && (Math.abs(n2-n3)==1) ) || ((Math.abs(n1-n2)==2) && (Math.abs(n1-n3)==1) && (Math.abs(n2-n3)==1)) ||((Math.abs(n1-n2)==1) && (Math.abs(n1-n3)==1)) ){
            return "顺子";
        }else if((Math.abs(n1-n2)==1) || (Math.abs(n1-n3)==1) || (Math.abs(n2-n3)==1)){
            return "半顺";
        }else{
            return "杂六";
        }
    }

    if(type==11){
        return Math.max(Math.abs(parseInt(num[0])-parseInt(num[1])),Math.abs(parseInt(num[0])-parseInt(num[2])),Math.abs(parseInt(num[1])-parseInt(num[2])));
    }
}

//北京赛车PK拾开奖函数
function Pk10_Auto(num , type,lotteryVersion){
    var zh = parseInt(num[0])+parseInt(num[1]);
    if(type==1){
        return zh;
    }
    if(type==2){
        if(lotteryVersion != 'v2' && lotteryVersion != 'v5' && lotteryVersion =='v2_1') {
            if(zh==11){
                return '和';
            }
        }
        if(zh>11){
            return '<font class="color-red">大</font>';
        }else{
            return '小';
        }
    }
    if(type==3){
        if(lotteryVersion != 'v2' && lotteryVersion != 'v5' && lotteryVersion =='v2_1') {
            if(zh==11){
                return '和';
            }
        }
        if(zh%2==0){
            return '<font class="color-red">双</font>';
        }else{
            return '单';
        }
    }
    if(type==4){
        if(parseInt(num[0])>parseInt(num[9])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==5){
        if(parseInt(num[1])>parseInt(num[8])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==6){
        if(parseInt(num[2])>parseInt(num[7])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==7){
        if(parseInt(num[3])>parseInt(num[6])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==8){
        if(parseInt(num[4])>parseInt(num[5])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
}

//幸运飞艇开奖函数
function XYFT_Auto(num , type){
    var zh = parseInt(num[0])+parseInt(num[1]);
    if(type==1){
        return zh;
    }
    if(type==2){
        if(zh>11){
            return '<font class="color-red">大</font>';
        }else{
            return '小';
        }
    }
    if(type==3){
        if(zh%2==0){
            return '<font class="color-red">双</font>';
        }else{
            return '单';
        }
    }
    if(type==4){
        if(parseInt(num[0])>parseInt(num[9])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==5){
        if(parseInt(num[1])>parseInt(num[8])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==6){
        if(parseInt(num[2])>parseInt(num[7])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==7){
        if(parseInt(num[3])>parseInt(num[6])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==8){
        if(parseInt(num[4])>parseInt(num[5])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
}

//北京快乐8
function Kl8_Auto(num , type){
    // console.log(num)


    // for(var j=0;j<num.length;j++){
    //     var zh=parseInt(num[j]);
    // }

    var zh = parseInt(num[0])+parseInt(num[1])+parseInt(num[2])+parseInt(num[3])+parseInt(num[4])+parseInt(num[5])+parseInt(num[6])+parseInt(num[7])+parseInt(num[8])+parseInt(num[9])+parseInt(num[10])+parseInt(num[11])+parseInt(num[12])+parseInt(num[13])+parseInt(num[14])+parseInt(num[15])+parseInt(num[16])+parseInt(num[17])+parseInt(num[18])+parseInt(num[19]);
    if(type==0){
        return zh;
    }

    if(type==1){//总和大小
        if(zh>810){
            return '<font class="color-red">总和大</font>';
        }else if(zh<810){
            return '总和小';
        }else if(zh==810){
            return '总和810';
        }
    }

    if(type==2){//总和双单
        if(zh%2==0){
            return '<font class="color-red">总和双</font>';
        }else{
            return '总和单';
        }
    }

    if(type==3){//上中下盘
        var compare =(parseInt(num[0])>40?1:-1)+(parseInt(num[1])>40?1:-1)+(parseInt(num[2])>40?1:-1)+(parseInt(num[3])>40?1:-1)+(parseInt(num[4])>40?1:-1)+(parseInt(num[5])>40?1:-1)+(parseInt(num[6])>40?1:-1)+(parseInt(num[7])>40?1:-1)+(parseInt(num[8])>40?1:-1)+(parseInt(num[9])>40?1:-1)+(parseInt(num[10])>40?1:-1)+(parseInt(num[11])>40?1:-1)+(parseInt(num[12])>40?1:-1)+(parseInt(num[13])>40?1:-1)+(parseInt(num[14])>40?1:-1)+(parseInt(num[15])>40?1:-1)+(parseInt(num[16])>40?1:-1)+(parseInt(num[17])>40?1:-1)+(parseInt(num[18])>40?1:-1)+(parseInt(num[19])>40?1:-1);

        if(compare>0){
            return '下盘';
        }else if(compare<0){
            return '上盘';
        }else if(compare==0){
            return '中盘';
        }
    }

    if(type==4){//奇偶和盘
        var compare =(parseInt(num[0])%2==0?1:-1)+(parseInt(num[1])%2==0?1:-1)+(parseInt(num[2])%2==0?1:-1)+(parseInt(num[3])%2==0?1:-1)+(parseInt(num[4])%2==0?1:-1)+(parseInt(num[5])%2==0?1:-1)+(parseInt(num[6])%2==0?1:-1)+(parseInt(num[7])%2==0?1:-1)+(parseInt(num[8])%2==0?1:-1)+(parseInt(num[9])%2==0?1:-1)+(parseInt(num[10])%2==0?1:-1)+(parseInt(num[11])%2==0?1:-1)+(parseInt(num[12])%2==0?1:-1)+(parseInt(num[13])%2==0?1:-1)+(parseInt(num[14])%2==0?1:-1)+(parseInt(num[15])%2==0?1:-1)+(parseInt(num[16])%2==0?1:-1)+(parseInt(num[17])%2==0?1:-1)+(parseInt(num[18])%2==0?1:-1)+(parseInt(num[19])%2==0?1:-1);

        if(compare>0){
            return '偶盘';
        }else if(compare<0){
            return '奇盘';
        }else if(compare==0){
            return '和盘';
        }
    }
}

//重庆时时彩开奖函数
//$type 1总和 2和大小 3和单双 4龙虎和 5前三 6中三 7后三 8斗牛 9梭哈
function Ssc_Auto(num , type){
    var zh = parseInt(num[0])+parseInt(num[1])+parseInt(num[2])+parseInt(num[3])+parseInt(num[4]);
    if(type==1){
        return zh;
    }
    if(type==2){
        if(zh>=23){
            return '<font class="color-red">大</font>';
        }
        if(zh<=22){
            return '小';
        }
    }
    //11选五总和大小
    if(type==12){
        if(zh>30){
            return '<font class="color-red">大</font>';
        }
        if(zh<30){
            return '小';
        }
        if(zh=30){
            return '和';
        }
    }
    if(type==3){
        if(zh%2==0){
            return '<font class="color-red">双</font>';
        }else{
            return '单';
        }
    }
    if(type==4){
        if(parseInt(num[0])>parseInt(num[4])){
            return '<font class="color-red">龙</font>';
        }
        if(parseInt(num[0])<parseInt(num[4])){
            return '虎';
        }
        if(parseInt(num[0])==parseInt(num[4])){
            return '和';
        }
    }
    if(type==5){

        var n1=parseInt(num[0]);
        var n2=parseInt(num[1]);
        var n3=parseInt(num[2]);
        if((n1==0 || n2==0 || n3==0) && (n1==9 || n2==9 || n3==9)){
            if(n1==0){
                n1=10;
            }
            if(n2==0){
                n2=10;
            }
            if(n3==0){
                n3=10;
            }
        }

        if(n1==n2 && n2==n3){
            return "豹子";
        }else if((n1==n2) || (n1==n3) || (n2==n3)){
            return "对子";
        }else if((n1==10 || n2==10 || n3==10) && (n1==9 || n2==9 || n3==9) && (n1==1 || n2==1 || n3==1)){
            return "顺子";
        }else if( ( (Math.abs(n1-n2)==1) && (Math.abs(n2-n3)==1) ) || ((Math.abs(n1-n2)==2) && (Math.abs(n1-n3)==1) && (Math.abs(n2-n3)==1)) ||((Math.abs(n1-n2)==1) && (Math.abs(n1-n3)==1)) ){
            return "顺子";
        }else if((Math.abs(n1-n2)==1) || (Math.abs(n1-n3)==1) || (Math.abs(n2-n3)==1)){
            return "半顺";
        }else{
            return "杂六";
        }
    }
    if(type==6){
        var n1=parseInt(num[1]);
        var n2=parseInt(num[2]);
        var n3=parseInt(num[3]);
        if((n1==0 || n2==0 || n3==0) && (n1==9 || n2==9 || n3==9)){
            if(n1==0){
                n1=10;
            }
            if(n2==0){
                n2=10;
            }
            if(n3==0){
                n3=10;
            }
        }

        if(n1==n2 && n2==n3){
            return "豹子";
        }else if((n1==n2) || (n1==n3) || (n2==n3)){
            return "对子";
        }else if((n1==10 || n2==10 || n3==10) && (n1==9 || n2==9 || n3==9) && (n1==1 || n2==1 || n3==1)){
            return "顺子";
        }else if( ( (Math.abs(n1-n2)==1) && (Math.abs(n2-n3)==1) ) || ((Math.abs(n1-n2)==2) && (Math.abs(n1-n3)==1) && (Math.abs(n2-n3)==1)) ||((Math.abs(n1-n2)==1) && (Math.abs(n1-n3)==1)) ){
            return "顺子";
        }else if((Math.abs(n1-n2)==1) || (Math.abs(n1-n3)==1) || (Math.abs(n2-n3)==1)){
            return "半顺";
        }else{
            return "杂六";
        }
    }
    if(type==7){
        var n1=parseInt(num[2]);
        var n2=parseInt(num[3]);
        var n3=parseInt(num[4]);
        if((n1==0 || n2==0 || n3==0) && (n1==9 || n2==9 || n3==9)){
            if(n1==0){
                n1=10;
            }
            if(n2==0){
                n2=10;
            }
            if(n3==0){
                n3=10;
            }
        }

        if(n1==n2 && n2==n3){
            return "豹子";
        }else if((n1==n2) || (n1==n3) || (n2==n3)){
            return "对子";
        }else if((n1==10 || n2==10 || n3==10) && (n1==9 || n2==9 || n3==9) && (n1==1 || n2==1 || n3==1)){
            return "顺子";
        }else if( ( (Math.abs(n1-n2)==1) && (Math.abs(n2-n3)==1) ) || ((Math.abs(n1-n2)==2) && (Math.abs(n1-n3)==1) && (Math.abs(n2-n3)==1)) ||((Math.abs(n1-n2)==1) && (Math.abs(n1-n3)==1)) ){
            return "顺子";
        }else if((Math.abs(n1-n2)==1) || (Math.abs(n1-n3)==1) || (Math.abs(n2-n3)==1)){
            return "半顺";
        }else{
            return "杂六";
        }
    }


    if(type==8){//斗牛

        function cal(cards) {

            var s = 0;
            var dict = {};
            for (var i = 0; i < cards.length; i++) {
                var ci = cards[i];
                s += ci;
                dict[ci] = dict[ci] === undefined ? 1 : dict[ci] + 1;
            };
            var point = s % 10;

            var exists = false;
            for (var i in dict) {
                var other = (10 + point - i) % 10;
                if (dict[other]) {
                    if ((other == i && dict[other] >= 2) || (other!=i&&dict[other] >= 1)) {
                        exists = true;
                        break;
                    }
                }

            }
            return exists && point==0 ? "牛牛" : exists && point!=0 ? "牛"+point : "没牛";
        }
        var num1=parseInt(num[0]);
        var num2=parseInt(num[1]);
        var num3=parseInt(num[2]);
        var num4=parseInt(num[3]);
        var num5=parseInt(num[4]);

        return cal([num1,num2,num3,num4,num5])
   }


    if(type==9){//梭哈
        var n11=parseInt(num[0]);
        var n22=parseInt(num[1]);
        var n33=parseInt(num[2]);
        var n44=parseInt(num[3]);
        var n55=parseInt(num[4]);

        var n1=n11
        var n1=n22
        var n1=n33
        var n1=n44
        var n1=n55



        num=[n11,n22,n33,n44,n55]


        if(n11==n22 && n22==n33 && n33==n44 && n44==n55){
            return "五条";
        }

        var array=[n11,n22,n33,n44,n55];
        for(i=0;i<5;i++){
            j=i+1;
            for(ii=j;ii<5;ii++){
                jj=ii+1;
                for(iii=jj;iii<5;iii++){
                    jjj=iii+1;
                    for(iiii=jjj;iiii<5;iiii++){
                        if(array[i]==array[ii] && array[ii]==array[iii] && array[iii]==array[iiii]) return "四条";
                    }
                }
            }
        }

        for(i=0;i<5;i++){
            j=i+1;
            for(ii=j;ii<5;ii++){
                jj=ii+1;
                for(iii=jj;iii<5;iii++){
                    if(num[i]==num[ii] && num[ii]==num[iii] )
                    {
                        var target32=num[i];
                        array.splice(array.indexOf(target32),1)
                        array.splice(array.indexOf(target32),1)
                        array.splice(array.indexOf(target32),1)

                        // foreach (array as key => value) {
                        //     if(key==i)unset(array[key]);
                        //     if(key==ii)unset(array[key]);
                        //     if(key==iii)unset(array[key]);
                        // }
                        var arr=new Array();
                        array.forEach(function(value,index,array){
                            arr[index]=value;
                        })
                        // foreach (array as key => value) {
                        //     arr[]=value;
                        // }
                        if(arr[0]==arr[1]) return "葫芦";
                    }
                }
            }
        }

        n1=parseInt(num[0]);n1==10?0:n1;
        n2=n1+1;n2==10?0:n2;
        n3=n2+1;n3==10?0:n3;
        n4=n3+1;n4==10?0:n4;
        n5=n4+1;n5==10?0:n5;
        if(n1==num[0] && n2==num[1] && n3==num[2] && n4==num[3] && n5==num[4] )
        {
            return "顺子";
        }


        for(i=0;i<5;i++){
            j=i+1;
            for(ii=j;ii<5;ii++){
                jj=ii+1;
                for(iii=jj;iii<5;iii++){
                    if(array[i]==array[ii] && array[ii]==array[iii] ) return "三条";
                }
            }
        }

        array=[n11,n22,n33,n44,n55];
        for(i=0;i<5;i++){
            j=i+1;
            for(ii=j;ii<5;ii++){
                if(num[i]==num[ii]){
                    var target2=num[i];
                    //console.log(target2);
                    array.splice(array.indexOf(target2),1);
                    array.splice(array.indexOf(target2),1);
                    //console.log(array)

                    //array.forEach(function(value,index,array){
                    //    if(index==i){
                    //        array.splice(index,1);
                    //    };
                    //    if(index==ii){
                    //        array.splice(index,1);
                    //    };
                    //})

                    // foreach (array as key => value) {
                    //     if(key==i)unset(array[key]);
                    //     if(key==ii)unset(array[key]);
                    // }
                    var arr=new Array();
                    array.forEach(function(value,index,array){
                        arr[index]=value;
                    })
                    //console.log(arr)
                    // foreach (array as key => value) {
                    //     arr[]=value;
                    // }
                    for(vi=0;vi<3;vi++){
                        vj=vi+1;
                        for(vii=vj;vii<3;vii++){
                            if(arr[vi]==arr[vii]) return "两对";
                        }
                    }
                }
            }
        }

        array=[n11,n22,n33,n44,n55];

        for(i=0;i<5;i++){
            j=i+1;
            for(ii=j;ii<5;ii++){
                if(array[i]==array[ii]){
                    return "一对";
                }
            }
        }

        return "散号";

    }//梭哈

}

//广东快乐十分开奖函数
function G10_Auto(num , type){
    var zh = parseInt(num[0])+parseInt(num[1])+parseInt(num[2])+parseInt(num[3])+parseInt(num[4])+parseInt(num[5])+parseInt(num[6])+parseInt(num[7]);
    if(type==1){
        return zh;
    }
    if(type==2){
        if(zh>=85 && zh<=132){
            return '<font class="color-red">大</font>';
        }
        if(zh>=36 && zh<=83){
            return '小';
        }
        if(zh==84){
            return '和';
        }
    }
    if(type==3){
        if(zh%2==0){
            return '<font class="color-red">双</font>';
        }else{
            return '单';
        }
    }
    if(type==4){
        var num=zh.toString();
        var zhws = num.charAt(num.length-1);
        if(zhws>=5){
            return '<font class="color-red">尾大</font>';
        }else{
            return '尾小';
        }
    }
    if(type==5){
        if(parseInt(num[0])>parseInt(num[7])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==6){
        if(parseInt(num[1])>parseInt(num[6])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==7){
        if(parseInt(num[2])>parseInt(num[5])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
    if(type==8){
        if(parseInt(num[3])>parseInt(num[4])){
            return '<font class="color-red">龙</font>';
        }else{
            return '虎';
        }
    }
}
//快3
function k3_Auto(num , type){
    var zh = parseInt(num[0])+parseInt(num[1])+parseInt(num[2]);
    if(type==0){
        return zh;
    }

    if(type==7){//总和大小
        if(zh>=11){
            return '<font class="color-red">总和大</font>';
        }else{
            return '总和小';
        }
    }

    if(type==8){//总和双单
        if(zh%2==0){
            return '<font class="color-red">总和双</font>';
        }else{
            return '总和单';
        }
    }

}
function PC_Auto(num , type){
    var zh = parseInt(num[0])+parseInt(num[1])+parseInt(num[2]);
    if(type==1){
        return zh;
    }
}
function dragMagic (obj,title){
    //点击box后，box跟着鼠标走
    title=title||obj;


    title.onmousedown=function(ev){
        var ll=$(obj).offset().left;
        var tt=$(obj).offset().top;
        $(".kuang1").css("position","static");
        $(obj).css({left:ll,right:"auto",top:tt,bottom:"auto"})

//            return;
        //记录偏移
        ev=ev||window.event
        var distanceX=ev.clientX-obj.offsetLeft;
        var distanceY=ev.clientY-obj.offsetTop;

        //鼠标移动后获得值后赋值；
        document.onmousemove=function(ev){
            var l;
            var t;
            ev=ev||window.event;
            l=ev.clientX-distanceX;
            t=ev.clientY-distanceY;
            sH=document.documentElement.clientHeight;
            sW=document.documentElement.clientWidth;
            if(l<0){
                l=0;
            };
            if(l>sW-obj.offsetWidth){
                l=sW-obj.offsetWidth;
            };
            if(t<0){
                t=0;
            };
            if(t>sH-obj.offsetHeight){
                t=sH-obj.offsetHeight;
            };

            obj.style.left=l+"px";
            obj.style.top=t+"px";
        };
        //鼠标抬起
        obj.onmouseup=function(){
            document.onmousemove=null;
        };
        return false;
    };
    //解决鼠标移出界面时候的bug
    document.onmouseup=function(){
        document.onmousemove=null;
    };

}


