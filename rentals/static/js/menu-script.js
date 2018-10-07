$(document).ready(function(){
  $('.city-logo').on('click',function(){
    $('.city-logo').fadeOut();
  });

  $('.datepicker').datepicker({
    orientation: 'top',
    format: 'yyyy-mm-dd',
  });

/*  $('#myform').submit(function(e){
    $.ajax({
      data: $(this).serialize(),
      type: $(this).attr('method'),
      url: $(this).attr('action'),
      success: function(){
        $('#flat-list').css('visibility','visible');
      }
    });
    return false;
  });*/
});
