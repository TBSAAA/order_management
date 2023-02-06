let countdown = 60;
let levelsUrl = "/levels/";
let rolesUrl = "/roles/";
let usersUrl = "/users/";
let orderStatusUrl = "/order_status/";
let transactionType = "/transaction_type/";
// ajax初始化添加csrftoken
$.ajaxSetup({
    beforeSend: function (xhr, setting) {
        if (!/^GET|HEAD|OPTIONS|TRACE$/.test(setting.type)) {
            xhr.setRequestHeader("X-CSRFTOKEN", $.cookie("csrftoken"));
        }
    }
});

function sendVerificationCode(obj) {
    // 验证码倒计时功能
    if (countdown === 0) {
        obj.text("获取验证码");
        obj.removeAttr("style");
        obj.css({"color": "#056de8"});
        countdown = 60;
        return;
    } else {
        obj.css({"pointer-events": "none", "color": "#989cb2"});
        obj.text(countdown + "秒重新发送");
        countdown--;
    }
    setTimeout(function () {
        sendVerificationCode(obj);
    }, 1000);
}

// 获取验证码
function getSmsCode(mobile) {
    $.ajax({
        url: '/get_sms_code/',
        type: 'post',
        dataType: 'json',
        data: {"mobile": mobile},
        success: function (data) {
        },
        error: function (err) {
        }
    });
}

function tooltips(selector, info) {
    // tooltip提示
    $(selector).each(function () {
        $(this).attr('data-toggle', 'tooltip');
        $(this).attr('data-placement', 'top');
        if (info) {
            $(this).attr("title", info);
        } else {
            $(this).attr("title", $(this).text()); // 动态设置内容为当前title的值
        }
        $(this).css("cursor", 'pointer');
    });
    $('[data-toggle="tooltip"]').tooltip();
}


function toasts(message) {
    // 弹窗
    $(".toast-info").text(message);
    $("#liveToast").toast('show');
}

function setSelectOptions(data, selector) {
    // 渲染下拉框选项
    data.forEach(function (item) {
        $(selector).append(`<option value="${item.id}">${item.title || item.name}</option>`);
    });
    $(selector).selectpicker("refresh").selectpicker('render');
}

function getRoles() {
    // 获取角色
    $.ajax({
        url: rolesUrl,
        type: "get",
        dataType: "json",
        data: null,
        success: function (data) {
            window.roles = data.data;
            data.data.forEach(function (item) {
                $("#user-search-role").append(`<option value="${item.role}">${item.title}</option>`);
            });
            $("#user-search-role").selectpicker("refresh").selectpicker('render');
            $("#user-search-role").val($("#user-search-role").attr("role_id")).selectpicker("refresh");
        }
    });
}

function getLevels() {
    // 获取级别
    $.ajax({
        url: levelsUrl,
        type: "get",
        dataType: "json",
        data: null,
        success: function (data) {
            window.levels = data.data;
            setSelectOptions(data.data, "#user-search-level");
            $("#user-search-level").val($("#user-search-level").attr("level_id")).selectpicker("refresh");
        }
    });
}

function getAdminUsers() {
    // 获取管理员
    $.ajax({
        url: usersUrl,
        type: "get",
        dataType: "json",
        data: {
            "role_id": 20
        },
        success: function (data) {
            window.adminUsers = data.data;
        }
    });
}

function getActiveUsers() {
    // 获取有效用户
    $.ajax({
        url: usersUrl,
        type: "get",
        dataType: "json",
        data: {
            "active": 1
        },
        success: function (data) {
            window.activeUsers = data.data;
            setSelectOptions(data.data, "#order-search-user");
            setSelectOptions(data.data, "#transaction-search-user");
            $("#order-search-user").val($("#order-search-user").attr("user_id")).selectpicker("refresh");
            $("#transaction-search-user").val($("#transaction-search-user").attr("user_id")).selectpicker("refresh");
        }
    });
}

function getOrderStatus() {
    // 获取订单状态
    $.ajax({
        url: orderStatusUrl,
        type: "get",
        dataType: "json",
        data: null,
        success: function (data) {
            window.orderStatus = data.data;
            setSelectOptions(data.data, "#order-search-status");
            $("#order-search-status").val($("#order-search-status").attr("status_id")).selectpicker("refresh");
        }
    });
}


function getTransactionType() {
    // 获取订单状态
    $.ajax({
        url: transactionType,
        type: "get",
        dataType: "json",
        data: null,
        success: function (data) {
            window.orderStatus = data.data;
            setSelectOptions(data.data, "#transaction-search-type");
            $("#transaction-search-type").val($("#transaction-search-type").attr("type_id")).selectpicker("refresh");
        }
    });
}

function validMobile(mobile) {
    // 校验手机号格式
    let mobile_re = /^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$/;
    return mobile_re.test(mobile);
}

function validEmail(email) {
    //  校验邮箱格式
    let email_re = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
    return email_re.test(email);
}

function validSmsCode(smsCode) {
    // 校验验证码
    let code_re = /^\d{6}$/;
    return code_re.test(smsCode);
}

function validInt(str) {
    // 校验正整数
    let int_re = /^[1-9]\d*|0$/;
    return int_re.test(str);
}

function validName(name) {
    // 校验特殊符号
    let name_re = /^[_0-9a-zA-Z\u4e00-\u9fa5]*$/;
    return name_re.test(name);
}

function validPositiveIn(stringNum) {
    let positiveInRe = /^[1-9]\d*$/;
    return positiveInRe.test(stringNum);
}

function inArray(ele, array) {
    // 判断元素是否在数组中
    if (array.indexOf(ele) > -1) {
        return true;
    }
    return false;
}

function isEmpty(ele) {
    // 判断是否为空
    if (ele.trim().length === 0) {
        return true;
    }
    return false;
}

function cleanError(selector) {
    // 清除提示信息
    $(selector).parent().find('span').text("");
    $(selector).parent().find("i").addClass("d-none");
    return $(selector);
}

function clean_error() {
    cleanError("#code-error");
    cleanError("#mobile-error");
    cleanError("#account-error");
    cleanError("#password-error");
}
function showError(selector, message) {
    // 展示提示信息
    $(selector).text(message).siblings().removeClass("d-none");
    return $(selector);
}

function show(selector) {
    // 显示
    $(selector).removeClass("d-none");
    return $(selector);
}

function hide(selector) {
    //隐藏
    $(selector).addClass("d-none");
    return $(selector);
}

function showPopConfirm(selector) {
    // 展示气泡弹窗，并返回id
    let id = $(selector).parent().attr("id");
    $(selector).next().removeClass("d-none");
    return id;
}

function hidePopConfirm(selector) {
    //隐藏气泡弹窗
    $(selector).parent().parent().addClass("d-none");
}

function RemoveEleById(id) {
    $(`[id='${id}']`).parent().parent().remove();
}

function getParams() {
    // 获取url参数
    var url = window.location.search; //获取url中"?"符后的字串
    var theRequest = new Object();
    if (url.indexOf("?") != -1) {
        var strs = url.substr(1).split("&");
        for (var i = 0; i < strs.length; i++) {
            theRequest[strs[i].split("=")[0]] = decodeURI(strs[i].split("=")[1]);
        }
    }
    return theRequest;
}

//replaceParamVal("参数名","要更换的参数值")
//替换指定传入参数的值,paramName为参数,replaceWith为新值
function replaceParamVal(paramName, replaceWith) {
    var oUrl = this.location.href.toString();
    var re = eval('/(' + paramName + '=)([^&]*)/gi');
    var nUrl = oUrl.replace(re, paramName + '=' + replaceWith);
    return nUrl;
}

var parseParam = function (param, key) {
    // 对象转url参数
    var paramStr = "";
    if (param instanceof String || param instanceof Number || param instanceof Boolean) {
        paramStr += "&" + key + "=" + encodeURIComponent(param);
    } else {
        $.each(param, function (i) {
            var k = key == null ? i : key + (param instanceof Array ? "[" + i + "]" : "." + i);
            paramStr += '&' + parseParam(this, k);
        });
    }
    return paramStr.substr(1);
};


function getRadioValue(name) {
    return $(`input:radio[name=${name}]:checked`).val();
}