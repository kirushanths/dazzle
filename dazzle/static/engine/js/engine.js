
var SERVER_URL = 'http://10.30.0.2/update/legend'
//$.fn.editable.defaults.mode = 'inline';

$(function(){ 

	$('[dztype="text"]').each(function(index){
 
		var height = $(this).height();

		var id = $(this).attr('dzid');
		var type = 'text';
		if (height > 60) type = 'textarea';

		$(this).editable({
			disabled: false,
			type: type,
			unsavedclass: null,
			error: function(response, newValue) { 
				console.log(response);  
			},
			value: $(this).text(),
			success: function(response, newValue) {
				var data = { 
						'type' : 'saveText',
						'id' : id,
						'value' : newValue 
					   };
				saveData(data);
			}, 
		});
 
	});

	var saveData = function(data)
	{ 
		$.post(SERVER_URL, data, function(response)
		{
			//alert(response);
		});
	}
 
});