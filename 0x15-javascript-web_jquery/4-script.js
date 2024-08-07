$(function () {
  $('#toggle_header').click(function () {
    const el = $('header');
    if (el.hasClass('red')) {
      el.removeClass('red');
      el.addClass('green');
    } else {
      el.addClass('red');
      el.removeClass('green');
    }
  });
});
