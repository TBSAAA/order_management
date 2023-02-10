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
    let url = '/register/';
    let account = $("#account").val().replace(' ', '');
    let password = $("#password").val().replace(' ', '');
    let password_again = $("#password-again").val().replace(' ', '');
    if (!account) {
        show_error("#account-error", "Please enter your phone number or email");
        return undefined;
    }
    if (!password) {
        show_error("#password-error", "please enter password");
        return undefined;
    }
    if (!verify_email(account)) {
        show_error("#account-error", 'The email format is wrong, please re-enter the correct email!');
        return undefined;
    }
    if (!verify_password(password)) {
        show_error("#password-error", 'Minimum 8 characters, maximum 32 characters, only letters and numbers');
        return undefined;
    }
    if (!verify_password_again(password, password_again)) {
        show_error("#password-again-error", 'The two passwords are inconsistent, please re-enter!');
        return undefined;
    }
    data = {
        'account': btoa(account),
        'password': btoa(password)
    };
    clean_error();
    submit(url, data);
}


function verify_email(email) {
    regexp = new RegExp('[\\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\\w!#$%&\'*+/=?^_`{|}~-]+)*@(?:[\\w](?:[\\w-]*[\\w])?\.)+[\\w](?:[\\w-]*[\\w])?');
    return regexp.test(email);
}

function verify_password(password) {
    // 密码最少8位，最多32位，可以包含任意字母、数字，特殊符号。
    regexp = new RegExp('^[a-zA-Z0-9]{8,32}$');
    return regexp.test(password);
}

function verify_password_again(password, password_again) {
    return password === password_again;
}
function clean_error() {
    hide_error("#account-error");
    hide_error("#password-error");
    hide_error("#password-again-error");
}

function show_error(selector, message) {
    $(selector).text(message).siblings().removeClass("d-none");
    return $(selector);
}

function hide_error(selector) {
    $(selector).parent().find('span').text("");
    $(selector).parent().find("i").addClass("d-none");
    return $(selector);
}

$(function () {
    $('#pwd-login').click(pwd_login);
    $(document).ready(function () {
        $('input').keydown(function (event) {
            var k = event.which;
            if (k === 13) {
                pwd_login();
            }
        });
    });
});
