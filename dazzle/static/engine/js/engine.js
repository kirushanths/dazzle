
//$.fn.editable.defaults.mode = 'inline';

$(function(){ 

	$('[dztype="text"]').each(function(index){

		var height = $(this).height();

		var type = 'text';
		if (height > 60) type = 'textarea';

		$(this).editable({
			disabled: false,
			type: type,
			unsavedclass: null,
			error: function(response, newValue) { 
				console.log(response);  
			},
			value: $.trim($(this).text()),
			success: function(response, newValue) {
				
			}, 
		});

	});

});