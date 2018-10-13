$(document).ready(function(){
  $('.city-logo').on('click',function(){
    $('.city-logo').fadeOut();
  });

  $('.datepicker').datepicker({
    orientation: 'top',
    format: 'yyyy-mm-dd',
    autoclose: true
  });
  $('.detail-datepicker').datepicker({
    orientation: 'top',
    format: 'yyyy-mm-dd',
    autoclose: true,
    datesDisabled: ['2018-10-28']
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
