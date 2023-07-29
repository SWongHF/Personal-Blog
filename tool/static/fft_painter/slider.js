function slider() {
  var customSlider = document.getElementById("customSlider");
  var sliderValue = document.getElementById("slider-number");
  valPercent =
    ((customSlider.value - customSlider.min) /
      (customSlider.max - customSlider.min)) *
    100;
  customSlider.style.background = `linear-gradient(to right, #3264fe ${valPercent}%, #d5d5d5 ${valPercent}%)`;
  sliderValue.textContent = customSlider.value;
  mode = document.querySelector(".active").textContent.substring(0, 3);
  if (mode === "0.5") mode = "slow";
  else if (mode === "1.0") mode = "fast";
  else if (mode === "2.0") mode = "medium";
  else {
    mode = "fast";
    button(1.0);
  }
  isSliding = false;
  customSlider.addEventListener("input", function () {
    isSliding = true;
  });
  customSlider.addEventListener("mouseup", function () {
    if (isSliding) {
      document.getElementById("responsive-gif").src =
        `../../static/fft_painter/fft${Math.round(
          parseFloat(sliderValue.textContent) * 10
        )}` +
        mode +
        ".gif";
    }
    isSliding = false;
  });
}
document.addEventListener("DOMContentLoaded", function () {
  slider();
});
