// Materialize functions
$(document).ready(function () {
  $("select").formSelect();
  $("textarea").characterCounter();
  $(".modal").modal();
  $(".collapsible").collapsible();
  // Hide header spans
  // $(".target").hide();
  // Materialize slider function
  let slider = document.querySelector(".slider");
  M.Slider.init(slider, {
    indicators: false,
    height: 500,
    transition: 500,
    interval: 6000,
  });
});
