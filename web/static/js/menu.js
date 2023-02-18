$(function () {
    $(".level-1").click(function () {
        $(this).find(".level-2").toggleClass("d-none");
        // $(this).siblings().find(".level-2").addClass("d-none");

        $(this).find(".uil-angle-down").toggleClass("uil-angle-down-rotate");
    });
})
