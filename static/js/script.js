// Materialize functions
$(document).ready(function () {
  $("select").formSelect();
  $("textarea").characterCounter();
  $(".modal").modal();
  $(".collapsible").collapsible();
  // Hide header spans
  $("h4.card-text .target").hide();
  // Materialize slider function
  let slider = document.querySelector(".slider");
  M.Slider.init(slider, {
    indicators: false,
    height: 400,
    transition: 500,
    interval: 6000,
  });
});
