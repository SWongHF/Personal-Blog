function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");
function DEL(it, name) {
  const request = new Request("/manage/image/config/", {
    headers: { "X-CSRFToken": csrftoken },
  });
  fetch(request, {
    method: "DELETE",
    body: JSON.stringify({
      content: name,
    }),
    mode: "same-origin", // Do not send CSRF token to another domain.
  })
    .then((response) => response.json())
    .then((result) => {
      if (result.message == "Success.") {
        location.reload(true);
      } else {
        location.reload(true);
      }
    });
}
function clipboardURL(url) {
  var copyText = url;
  var base_url = window.location.origin;

  navigator.clipboard.writeText(base_url + copyText);

  // Alert the copied text
  document.querySelector("div.alert").style.display = "block";
}

window.addEventListener("DOMContentLoaded", (event) => {
  const Im = document.getElementById("photo");
  const Finm = document.getElementById("image_upload");
  $("input#image_upload").on("input", function (e) {
    $("button.btn-upload").html("Upload");
  });
  $(".btn-upload").on("click", function (e) {
    e.preventDefault();
    var it = e.target;
    if (it.innerHTML === "Confirm") {
      const request = new Request("/manage/image/config/", {
        headers: { "X-CSRFToken": csrftoken },
      });
      const formData = new FormData();

      formData.append("filename", Finm.value);
      formData.append("image", Im.files[0]);
      fetch(request, {
        method: "POST",
        body: formData,
        mode: "same-origin", // Do not send CSRF token to another domain.
      })
        .then((response) => response.json())
        .then((result) => {
          if (result.message == "Success.") {
            location.reload(true);
          } else {
            location.reload(true);
          }
        });
    }
    it.innerHTML = "Confirm";
  });
  document.body.addEventListener("click", function (e) {
    if (!e.target.classList.contains("btn")) {
    } else {
      if (e.target.classList.contains("btn-clipboard"))
        $("button.btn-upload").html("Upload");
      else document.querySelector("div.alert").style.display = "none";
    }
  });
});
