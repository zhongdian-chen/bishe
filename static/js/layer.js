// {#弹出层的样式变化#}
$(function(){
    $(".btn1").click(function() {
        $("#layer-mask").show();
        $("#layer-pop").show();
        $("#layer-close").click(function(){
            $("#layer-mask").hide();
            $("#layer-pop").hide();
        });
    });
});