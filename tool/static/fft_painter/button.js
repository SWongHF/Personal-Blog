function button(sp) {
  var sliderValue = document.getElementById("slider-number");
  $(".active").toggleClass("active");
  $(`.button${Math.round(sp * 10)}`).toggleClass("active");
  if (sp === 0.5) mode = "slow";
  else if (sp === 1.0) mode = "fast";
  else if (sp === 2.0) mode = "medium";
  else {
    mode = "fast";
  }
  document.getElementById("responsive-gif").src =
    `../../static/fft_painter/fft${Math.round(
      parseFloat(sliderValue.textContent) * 10
    )}` +
    mode +
    ".gif";
}
