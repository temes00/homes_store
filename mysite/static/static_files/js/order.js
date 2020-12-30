$('#submit_btn').on('click', function(e) {
    let form = $('#user_info')[0]
    let data = new FormData(form);
    if (document.forms['user_info'].checkValidity()) {
        $("#submit_btn").prop("disabled", true);
        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "../order/create/",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function(data) {
                if (!data.error) {
                    alert(data.message)
                } else {
                    alert(data.message)
                }
            },
            error: function(e) {
                alert('Произошла ошибка, повторите попытку позже.')
                console.log("ERROR : ", e);
            }
        });
    }
});