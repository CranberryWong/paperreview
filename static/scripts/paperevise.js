$(function() {
  $('.paper-feed-revise').click(function(e) {
    var target = $(this);
    var paper_id = target.data('pid');

    console.log('here');
    var jqxhr = $.ajax('/paper/' + paper_id + '/revise', {
    dataType: 'json'
}).done(function (data) {
    $('#paper-bibtex').val(data.bibtex);
    $('.paper-content').val(data.content);
    $('#paper-id').val(data.paper_id);
    console.log('成功, 收到的数据: ' + JSON.stringify(data));
}).fail(function (xhr, status) {
    console.log('失败: ' + xhr.status + ', 原因: ' + status);
}).always(function () {
    console.log('请求完成: 无论成功或失败都会调用');
});
  })
})

$(function() {
  $('#add-abstract-button').click(function(e) {
    var target = $(this);
    $('#paper-bibtex').val('');
    $('.paper-content').val('');
    $('#paper-id').val('');
    $('.simditor-toolbar').css("top",'0px').css("width","966px").css("left","237.5px")
  })
})