document.addEventListener("DOMContentLoaded", function () {
  var initial_form_state = $("textarea.editormd-markdown-textarea").text();
  $(window).bind("beforeunload", function (e) {
    var form_state = $("textarea.editormd-markdown-textarea").text();
    if (initial_form_state != form_state) {
      var message =
        "You have unsaved changes on this page. Do you want to leave this page and discard your changes or stay on this page?";
      e.returnValue = message; // Cross-browser compatibility (src: MDN)
      return message;
    }
  });
});
