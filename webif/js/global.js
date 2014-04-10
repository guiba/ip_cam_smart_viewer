$('#title-submit').on('click', function() {
  var title=$('#title').val();
  if($.trim(title) != ''){
//     $("#title").effect("bounce","slow");
  $.post('ajax/name.php', $.("#form").serialize(), function(data) {
    $('#result').text(data);
    });
  }
});
