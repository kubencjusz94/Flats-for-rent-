$(document).ready(function(){
  $('.city-logo').on('click',function(){
    $('.city-logo').fadeOut();
    $('#form-cont').css('display','inline-block');
    var choosen_city_id=$(this).attr('id');
    var choosen_city;
    if(choosen_city_id=='gda-logo') choosen_city='Gdańsk';
    if(choosen_city_id=='gdy-logo') choosen_city='Gdynia';
    if(choosen_city_id=='sop-logo') choosen_city='Sopot';
    $("#city option:contains('"+choosen_city+"')").attr('selected','selected');
    $('.datepicker').datepicker();
  });
});
