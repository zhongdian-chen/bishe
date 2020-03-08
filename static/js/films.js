function to_cele(){
    if ($('.to_cele').siblings()[1].innerText==='演职人员'){
        $('.title1').addClass('active');
        $('.title2').removeClass('active')
    }
    $('.tab-content-container').load('/tab_celebrity.html')
    $("html,body").animate({scrollTop: $("#BUY").offset().top}, 500);
}

function to_img(){
    if ($('.to_img').siblings()[1].innerText==='图集'){
        $('.title2').addClass('active');
        $('.title1').removeClass('active')
    }
    $('.tab-content-container').load('/tab_img.html')
    $("html,body").animate({scrollTop: $("#BUY").offset().top}, 500);
}

$(document).ready(function(){
    $('.tab-content-container').load('/tab_celebrity.html');
});
$('.tab-title').click(function () {
    $(this).addClass('active');
    $(this).siblings().removeClass('active');
    if ($(this)[0].innerHTML==='演职人员'){
        $('.tab-content-container').load('/tab_celebrity.html')
    }else if ($(this)[0].innerHTML==='图集'){
        $('.tab-content-container').load('/tab_img.html')
    }
});