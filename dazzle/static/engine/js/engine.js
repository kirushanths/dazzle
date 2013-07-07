
var SERVER_URL = 'http://10.30.0.2/update/legend'
//$.fn.editable.defaults.mode = 'inline';

window.dazzlejQuery = jQuery.noConflict(true);

window.dazzlejQuery(function(){ 

	var dz$ = window.dazzlejQuery;

	dz$('[dztype="text"]').each(function(index){

		var height = dz$(this).height();

		var id = dz$(this).attr('dzid');
		var type = 'text';
		if (height > 60) type = 'textarea';

		dz$(this).editable({
			disabled: false,
			type: type,
			unsavedclass: null,
			error: function(response, newValue) { 
				console.log(response);  
			},
			value: dz$.trim(dz$(this).text()),
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
		dz$.post(SERVER_URL, data, function(response)
		{
			//alert(response);
		});
	}
});