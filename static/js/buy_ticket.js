window.onload=function () {
    $('.buy')[0].innerHTML='其他电影推荐';
    $('.buy').attr('href','/films');
};

var now = new Date();
var time1 = now.getFullYear() + "/" +(now.getMonth()+1)+"/"+now.getDate();
var time2 = now.getFullYear() + "/" +(now.getMonth()+1)+"/"+(now.getDate()+1);
$('.time1')[0].innerText=time1;
$('.time2')[0].innerText=time2;