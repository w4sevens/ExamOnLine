$(function(){
    $(".mysidebar>li>div").click(function(){
        // alert('你点击了标签');
        // alert($(this).html())
        $(this).siblings('ul').removeClass('hide').slideDown();
        $(this).parent().siblings('li').children('ul').slideUp();
    });

});