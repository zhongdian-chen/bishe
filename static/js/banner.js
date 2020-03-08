$('.opensyn').click(function () {
    if ($(this)[0].innerText === "（展开）"){
        $('.syntext')[0].innerText = "{{ films_info.syncpsis }}"
        $(this)[0].innerText = "（折叠）"
    }else if ($(this)[0].innerText === "（折叠）"){
        $('.syntext')[0].innerText = "{{ films_info.syncpsis|truncatechars:35 }}"
        $(this)[0].innerText = "（展开）"
    }
});