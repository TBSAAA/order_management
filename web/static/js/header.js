$(function () {
    $(".avatar-home").mouseenter(function () {
        $(".user-options").removeClass("d-none");
    });
    $(".user-all").mouseleave(function () {
        $(".user-options").addClass("d-none");
    });
});