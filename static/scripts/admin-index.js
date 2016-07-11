$(function() {
    $('#role-select').click(function(e) {
        var target = $(this);
        var user_id = target.data('uid');
        
        var jqxhr = $.ajax('/paper/role?uid=' +  , {
        dataType: 'json'
}).done(function (data) {
    $('#paper-title').val(data.title);
    $('#paper-author').val(data.author);
    $('#paper-pubdate').val(data.pubDate);
    $('#paper-content').val(data.content);
    console.log('成功, 收到的数据: ' + JSON.stringify(data));
}).fail(function (xhr, status) {
    console.log('失败: ' + xhr.status + ', 原因: ' + status);
}).always(function () {
    console.Log('请求完成: 无论成功或失败都会调用');
});
    })
})