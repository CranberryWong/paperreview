$(function() {
    $('#role-select').change(function() {
        var target = $(this);
        console.log("load");
        var user_id = target.data('uid');
        var roleselect = target.val();

        var jqxhr = $.post('/admin/role', {
        user_id: user_id,
        roleselect: roleselect
    },
        function(){
            console.log("Done");
            
        }
);
    })
})

$(function() {
    $('#auth-select').change(function() {
        var target = $(this);
        console.log("load");
        var user_id = target.data('uid');
        var authselect = target.val();
        console.log(authselect)

        var jqxhr = $.post('/admin/auth', {
        user_id: user_id,
        authselect: authselect
    },
        function(){
            console.log("Done");
            
        }
);
    })
})