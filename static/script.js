$(document).ready(function() {
    $('#show-notification').click(function() {
      $('#notification').removeClass('hidden');
      setTimeout(function() {
        $('#notification').addClass('hidden');
      }, 3000);
    });
  });