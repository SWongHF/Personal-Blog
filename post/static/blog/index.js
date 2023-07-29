var rem = function (count) {
  var unit = $("html").css("font-size");
  if (typeof count !== "undefined" && count > 0) return parseInt(unit) * count;
  else return parseInt(unit);
};
document.addEventListener("DOMContentLoaded", function () {
  var body = document.querySelector("body");
  $(document.body).css({
    marginBottom: $(".footer").innerHeight(),
  });
  if ($(".intro-header").outerHeight(true) === undefined) {
    $(".appcontent").css({
      minHeight:
        $(document).outerHeight(true) -
        $(".navbar").outerHeight(true) -
        $(".footer").outerHeight(true),
    });
  } else {
    $(".appcontent").css({
      minHeight:
        $(document).outerHeight(true) -
        $(".navbar").outerHeight(true) -
        $(".intro-header").outerHeight(true) -
        $(".footer").outerHeight(true),
    });
  }
  if ($(document.body).width() >= 767) {
    $(".hbox").addClass("hbox-auto-sm");
    $(".hbox #blog_info").css({
      paddingTop: rem(5),
    });
  } else {
    $(".hbox").addClass("hbox-auto-xs");
    $(".hbox #sidebar").addClass("p-5");
    $(".hbox #blog_info").css({
      paddingTop: 0,
    });
    $(".appcontent").css({
      minHeight: "none",
    });
  }

  window.addEventListener("resize", () => {
    $(document.body).css({
      marginBottom: $(".footer").innerHeight(),
    });
    if ($(".intro-header").outerHeight(true) === undefined) {
      $(".appcontent").css({
        minHeight:
          $(document).outerHeight(true) -
          $(".navbar").outerHeight(true) -
          $(".footer").outerHeight(true),
      });
    } else {
      $(".appcontent").css({
        minHeight:
          $(document).outerHeight(true) -
          $(".navbar").outerHeight(true) -
          $(".intro-header").outerHeight(true) -
          $(".footer").outerHeight(true),
      });
    }
    if ($(document.body).width() >= 767) {
      $(".hbox").addClass("hbox-auto-sm");
      $(".hbox").removeClass("hbox-auto-xs");
      $(".hbox #sidebar").removeClass("p-5");
      $(".hbox #blog_info").css({
        paddingTop: rem(5),
      });
    } else {
      $(".hbox").removeClass("hbox-auto-sm");
      $(".hbox").addClass("hbox-auto-xs");
      $(".hbox #sidebar").addClass("p-5");
      $(".hbox #blog_info").css({
        paddingTop: 0,
      });
      $(".body").css({
        minHeight: "none",
      });
    }
  });
});
