$('#submit_btn').on('click',function (e){
	let form = $('#user_info')[0]
	data = new FormData(form);
    if(document.forms['user_info'].checkValidity()){
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
            success: function (data) {
            	if (!data.error){
            		alert('Заказ оформлен, на указанную вами почту прийдет оповещение. Вам перезвонят в ближайщее время!')	
            	}else{
            		alert('Заказ оформлен. Вам перезвонят в ближайщее время!')
            	}
            },
            error: function (e) {
            	alert('Произошла ошибка, повторите попытку позже.')
                console.log("ERROR : ", e);
            }
        });
    }
});