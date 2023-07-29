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

window.addEventListener("DOMContentLoaded", (event) => {
  var init_suf = document.getElementById("inputSuffix").value;
  $(".btn-submit").on("click", function (e) {
    e.preventDefault();
    $("#form").data("serialize", $("#form").serialize());
    const request = new Request("/manage/post/edit/?q=" + init_suf, {
      headers: { "X-CSRFToken": csrftoken },
    });
    const formData = new FormData();
    const title = document.getElementById("inputTitle");
    const author = document.getElementById("inputAuthor");
    const suffix = document.getElementById("inputSuffix");
    const categories = document.getElementById("inputCategories");
    const priority = document.getElementById("inputPriority");
    const introduction = document.getElementById("inputIntroduction");
    const content = $("textarea.editormd-markdown-textarea").text();
    const statusH = document.getElementById("statusHidden");
    formData.append("title", title.value.trim());
    formData.append("author", author.value.trim());
    formData.append("suffix", suffix.value.trim());
    formData.append("categories", categories.value.trim());
    formData.append("priority", priority.value);
    formData.append("introduction", introduction.value);
    formData.append("content", content);
    if (!statusH.checked) {
      formData.append("status", "0");
    } else formData.append("status", "1");
    fetch(request, {
      method: "POST",
      body: formData,
      mode: "same-origin", // Do not send CSRF token to another domain.
    })
      .then((response) => response.json())
      .then((result) => {
        if (result.message == "Success.") {
          $("#form").data("serialize", $("#form").serialize());
          window.location.replace(
            "/manage/post/edit/?q=" + suffix.value.trim()
          );
        }
      });
  });
});
