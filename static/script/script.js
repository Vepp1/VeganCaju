document.addEventListener('DOMContentLoaded', function() {

  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: 'mmm dd, yyyy',
    i18n: {done: "Select"}
  });
});