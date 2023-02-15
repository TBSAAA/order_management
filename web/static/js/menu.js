$(function () {
    $(".parent").click(function () {
        $(this).parent().siblings().find(".children").toggleClass("d-none");
        $(this).find(".children").toggleClass("d-none");
    });
})
