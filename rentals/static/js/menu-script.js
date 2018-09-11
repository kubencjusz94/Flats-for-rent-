$(function(){
  var choosen_city;
  $('.city-logo').on('click',function(){
    $('.city-logo').fadeOut();
    $('.city-logo').remove();
    $('#first-day').css('display','grid');
    $('#first-day').datepicker();
    $('#last-day').css('display','grid');
    $('#last-day').datepicker();
  })
});
