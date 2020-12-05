$("button[name=getVerifyBt]").bind("click", function () {
    var self = this;
    var userPhoneEl = $("input[name=phoneNum]");
    var userPhone = $.trim(userPhoneEl.val());
    if (userPhone == "") {
        alert("请填写号码！");
        return;
    }
    $.get("/getPhoneVerifyCode/" + userPhone + "/")
        .success(function (msg) {
            console.info(msg);
            var ddEl = $(self).siblings("dd.showTag");
            if (msg == "ok") {
                ddEl.find("span").hide();
                ddEl.find("span[name=success]").show();
            } else {
                ddEl.find("span").hide();
                ddEl.find("span[name=error]").show();
            }
        })
        .error(function (msg) {
            console.info(msg);
        });
    var step = 60;
    $(this).attr("disabled", true);
    $(this).html("重新发送" + step);
    var interThread = setInterval(function () {
        step -= 1;
        $(self).html("重新发送" + step);
        if (step <= 0) {
            $(self).removeAttr("disabled");
            $(self).html("获取验证码");
            clearInterval(interThread);
        }
    }, 1000);


});