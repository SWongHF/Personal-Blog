document.addEventListener("DOMContentLoaded", function () {
  $(document.body).css({ marginBottom: $(".footer").innerHeight() + "px" });
  window.addEventListener("resize", () => {
    $(document.body).css({ marginBottom: $(".footer").innerHeight() + "px" });
  });
});
