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
    const request = new Request("/manage/post/config/", {
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
  document.body.addEventListener("click", function (e) {
    if (!e.target.classList.contains("btn-del")) {
      $("button.btn-del").html("Delete");
    }
  });
  const myTable = new window.simpleDatatables.DataTable("#datatablePost", {
    columns: [
      {
        select: 6,
        sortable: false,
        orderable: false,
      },
    ],
  });
});
