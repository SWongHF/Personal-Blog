document.addEventListener("DOMContentLoaded", function () {
  var gif = document.querySelector("#responsive-gif");
  var body = document.querySelector("div.body");
  var slider = document.querySelector(".sliderContainer");
  $(document.body).css({ marginBottom: $(".footer").innerHeight() + "px" });
  slider.style.width = body.clientWidth * 0.6 + "px";
  gif.style.width = body.clientWidth * 0.6 + "px";
  gif.style.height = gif.style.width * 0.75 + "px";
  window.addEventListener("resize", () => {
    $(document.body).css({ marginBottom: $(".footer").innerHeight() + "px" });
    gif.style.width = body.clientWidth * 0.6 + "px";
    gif.style.height = gif.style.width * 0.75 + "px";
    slider.style.width = body.clientWidth * 0.6 + "px";
  });
});
