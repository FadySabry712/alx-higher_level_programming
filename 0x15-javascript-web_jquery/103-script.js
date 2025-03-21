$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (enter) {
      if (enter.keycode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const defUrl = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(defUrl + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}
