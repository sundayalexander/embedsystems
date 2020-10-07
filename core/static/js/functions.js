!function (t) {
    "use strict";

    function n() {
        t(".parallax").each(function () {
            var n = t(this), a = t(window).scrollTop(), o = a * i, o = +o.toFixed(2);
            n.hasClass("fs") ? n.css("transform", "translate3d(-50%,-" + (50 - .15 * o) + "%,0)") : n.css("transform", "translate3d(0," + o + "px,0)")
        })
    }

    function a() {
        var n = t(window).height(), a = t(window).scrollTop(), o = a + n;
        t.each(e, function () {
            var n = t(this), i = n.outerHeight(), e = n.offset().top - 100, s = e + i;
            s >= a && e <= o ? n.addClass("in-view") : n.removeClass("in-view")
        })
    }

    t("a[href!=#][data-toggle!=tab][data-toggle!=collapse][target!=_blank][class!=anchor]").addClass("smooth"), t(".smooth-transition").animsition({
        linkElement: ".smooth",
        inDuration: 500,
        outDuration: 500
    });
    var o = t(".masonry");
    o.imagesLoaded(function () {
        o.packery({itemSelector: ".item"})
    }), t(".filter-container .btn").on("click", function (n) {
        t(".filters").toggleClass("open"), n.preventDefault()
    }), t(".filter").on("click", function (n) {
        var a = t(this).parent().parent().attr("data-target"), i = t(this).attr("data-toggle");
        t(".filter.active").removeClass("active"), t(this).addClass("active"), t(a).find(".item:not(" + i + ")").css({
            transition: "all .25s",
            transform: "scale(0)",
            opacity: "0"
        }), setTimeout(function () {
            t(a).find(".item:not(" + i + ")").hide(0), t(a).find(i).show(0).css({
                transform: "scale(1)",
                opacity: "1"
            }), o.packery("layout")
        }, 250)
    }), t(".nav-btn").on("click", function (n) {
        n.stopPropagation(), t("body").toggleClass("menu-active"), (t(".nav-container").hasClass("fullscreen") || t(".nav-container").hasClass("classic")) && (t(".nav-container").fadeToggle(), t("body").toggleClass("fs-menu-active")), t(".nav-container").hasClass("top") && t(window).width() < 992 && (t(".nav-container").fadeToggle(), t("body").toggleClass("fs-menu-active")), t(".nav-container").hasClass("sidebar") && t("body").toggleClass("sb-menu-active")
    }), t(".nav-container").on("click", function (t) {
        t.stopPropagation()
    }), t("html").on("click", function () {
        t("body").removeClass("menu-active sb-menu-active fs-menu-active")
    }), t(".dropdown").on("click", function (n) {
        t(this).toggleClass("hover").siblings().removeClass("hover")
    }), t(window).on("resize", function () {
        setTimeout(function () {
            o.packery("layout"), window.requestAnimationFrame(a)
        }, 1500)
    }), t(".anchor").on("click", function (n) {
        n.preventDefault(), n.stopPropagation(), t("body").removeClass("menu-active");
        var a = t(this).attr("href");
        t("html,body").animate({scrollTop: t(a).offset().top - 48 + "px"})
    });
    var i = .15;
    t(window).on("scroll", function () {
        window.requestAnimationFrame(n)
    });
    var e = t(".item");
    t(".cart-toggle").on("click", function () {
        t(".cart-container").fadeToggle()
    }), t(".add-to-cart").on("click", function (n) {
        n.stopPropagation(), t(".cart-container").fadeIn(), n.preventDefault()
    }), t(".cart").on("click", function (t) {
        t.stopPropagation()
    }), t("html").on("click", function () {
        t(".cart-container").fadeOut()
    }), t(window).on("scroll resize", function () {
        window.requestAnimationFrame(a), t(".anchor").each(function () {
            var n = "#" + t(".in-view").attr("id");
            n == t(this).attr("href") && (t(".anchor").removeClass("active"), t(this).addClass("active"))
        })
    }), t(window).load(function () {
        window.requestAnimationFrame(a)
    }), t(window).bind("pageshow", function (t) {
        t.originalEvent.persisted && window.location.reload()
    })
}(jQuery);

function notify(type, content, timeout) {
    new Noty({
        type: type,
        text: content,
        layout: 'topRight',
        theme: 'metroui',
        animation: {
            open: 'animated bounceIn',
            close: 'animated bounceOut'
        },
        timeout: timeout
    }).show()
}