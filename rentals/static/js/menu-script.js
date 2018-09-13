$(function(){
  $('.city-logo').on('click',function(){
    $('.city-logo').fadeOut();

    var choosen_city=$(this).attr('id');

    $('h1').text(choosen_city);
    $('#form-cont').css('display','inline-block');
    $('.datepicker').datepicker();
  });
});
