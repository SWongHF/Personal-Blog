$("path").each(function (i) {
  var path = this;
  var len = path.getTotalLength();
  var p = path.getPointAtLength(0);
  var height=$("svg").height();
  stp = p.x.toFixed(3) + "," + (height-p.y).toFixed(3) + '\n';
  for (var i = 1; i < len; i++) {
    p = path.getPointAtLength(i);
    stp = stp + p.x.toFixed(3) + "," + (height-p.y).toFixed(3) + '\n';
  }
});
