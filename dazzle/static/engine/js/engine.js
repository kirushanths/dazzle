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
		var url = 'update' + window.location.pathname;
		dz$.post(url, data, function(response)
		{
			//alert(response);
		});
	}
});