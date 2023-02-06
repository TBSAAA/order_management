let countdown = 60;
var submit = function (url, data) {
    $.ajax({
        url: url,
        dataType: 'json',
        type: 'post',
        data: data,
        success: function (data) {
            alert(data['content']);
            if (data['status_code'] === 1) {
                location.href = url === '/api/login' ? '/challenge/' : '/login/';
            }
        },
        error: function (e) {
            console.log(e);
            alert('submit data failed');
        }
    });
};

function pwd_login() {
    clean_error();
    let url = '/login/';
    let account = $("#account").val().replace(' ', '');
    let password = $("#password").val().replace(' ', '');
    if (!account) {
        show_error("#account-error", "Please enter your phone number or email");
        return undefined;
    }
    if (!password) {
        show_error("#password-error", "please enter password");
        return undefined;
    }
    if (/^\d+$/.test(account)) {
        if (!valid_mobile(account)) {
            show_error("#account-error", "Mobile number is incorrect");
            return undefined;
        }
    } else {
        if (!verify_email(account)) {
            show_error("#account-error", 'The email format is wrong, please re-enter the correct email!');
            return undefined;
        }
    }
    data = {
        'account': btoa(account),
        'password': btoa(password)
    };
    submit(url, data);
}


function sms_login() {
    clean_error();
    let url = '/login/';
    let code = $("#code").val().replace(' ', '');
    let mobile = $("#mobile").val().replace(' ', '');
    if (!mobile) {
        show_error("#mobile-error", "Please enter phone number");
        return undefined;
    }
    if (!code) {
        show_error("#code-error", "please enter verification code");
        return undefined;
    }
    if (!valid_mobile(mobile)) {
        show_error("#mobile-error", 'Mobile number is incorrect');
        return undefined;
    }
    if (!valid_sms_code(code)) {
        show_error("#code-error", "Verification code is incorrect");
        return undefined;
    }
    data = {
        'code': btoa(code),
        'mobile': btoa(mobile)
    };
    submit(url, data);
}

function get_code() {
    let url = '/get_code/';
    let mobile = $("#mobile").val().replace(' ', '');
    if (!mobile) {
        show_error("#mobile-error", "Please enter phone number");
        return undefined;
    }
    if (!valid_mobile(mobile)) {
        show_error("#mobile-error", 'Mobile number is incorrect');
        return undefined;
    }
    data = {
        'mobile': btoa(mobile)
    };
    timer(countdown);
    submit(url, data);

}

// Verification code countdown function
function timer(timeout) {
    let $code = $(".code");
    console.log('iamhere');
    // restore input box
   $("#code").removeAttr("disabled").text('');
    let reminder = setInterval(function () {
        $code.text(timeout + "s");
        $code.css({"pointer-events": "none", "color": "#989cb2"});
        console.log(timeout);
        timeout--;
        if (timeout < 0) {
            console.log('iamhere--aaaa');
            clearInterval(reminder);
            $code.text("get code");
            $code.removeAttr("style");
            $code.css({"color": "#056de8"});
        }
    }, 1000);
}

function verify_email(email) {
    regexp = new RegExp('[\\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\\w!#$%&\'*+/=?^_`{|}~-]+)*@(?:[\\w](?:[\\w-]*[\\w])?\.)+[\\w](?:[\\w-]*[\\w])?');
    return regexp.test(email);
}

function valid_mobile(mobile) {
    regexp = new RegExp('^04[0-9]{8}$');
    return regexp.test(mobile);
}

function valid_sms_code(smsCode) {
    regexp = new RegExp('^\d{6}$');
    return regexp.test(smsCode);
}

function clean_error() {
    hide_error("#code-error");
    hide_error("#mobile-error");
    hide_error("#account-error");
    hide_error("#password-error");
}

function show_error(selector, message) {
    $(selector).text(message).siblings().removeClass("d-none");
    return $(selector);
}

function show(selector) {
    $(selector).removeClass("d-none");
    return $(selector);
}

function hide(selector) {
    $(selector).addClass("d-none");
    return $(selector);
}

function hide_error(selector) {
    $(selector).parent().find('span').text("");
    $(selector).parent().find("i").addClass("d-none");
    return $(selector);
}

$(function () {
    $(".pwd").click(function () {
        console.log("pwd");
        hide(".sms-login");
        show(".pwd-login");
        clean_error();
        // $(".error").text("");
        $(".pwd").css("color", "#056de8");
        $(".sms").css("color", "#000");

    });

    $(".sms").click(function () {
        hide(".pwd-login");
        show(".sms-login");
        clean_error();
        // $(".error").text("");
        $(".sms").css("color", "#056de8");
        $(".pwd").css("color", "#000");

    });

    $('#pwd-login').click(pwd_login);
    $('#sms-login').click(sms_login);
    $(".code").click(get_code);

    $(document).ready(function () {
        $('input').keydown(function (event) {
            var k = event.which;
            if (k === 13) {
                console.log("enter");
            }
        });
    });
});
