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
  if ($(it).html() === "Confirm") {
    const request = new Request("/manage/category/config/", {
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
  $("button.btn-del").html("Delete");
  it.innerHTML = "Confirm";
}
window.addEventListener("DOMContentLoaded", (event) => {
  $("input#category_create").on("input", function (e) {
    $("button.btn-create").html("Create");
  });
  $("button.btn-create").on("click", function (e) {
    var it = e.target;
    if (it.innerHTML === "Confirm") {
      if (document.querySelector("input#category_create").value.trim() === "")
        return;
      const request = new Request("/manage/category/config/", {
        headers: { "X-CSRFToken": csrftoken },
      });
      fetch(request, {
        method: "POST",
        body: JSON.stringify({
          content: document.querySelector("input#category_create").value,
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
    it.innerHTML = "Confirm";
  });
  document.body.addEventListener("click", function (e) {
    if (!e.target.classList.contains("btn-del")) {
      $("button.btn-del").html("Delete");
    } else if (!e.target.classList.contains("btn-create")) {
      $("button.btn-create").html("Create");
    } else {
      $("button.btn-del").html("Delete");
      $("button.btn-create").html("Create");
    }
  });
  const myTable = new window.simpleDatatables.DataTable("#datatableCategory", {
    columns: [
      {
        select: 1,
        sortable: false,
        orderable: false,
      },
    ],
  });
});
