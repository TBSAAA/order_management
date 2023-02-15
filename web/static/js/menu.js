$(function () {
    $(".level-1").click(function () {
        $(this).parent().siblings().find(".level-2").toggleClass("d-none");
        $(this).find(".level-2").toggleClass("d-none");
        $(this).find(".uil-angle-down").toggleClass("uil-angle-down-rotate");
    });
})
