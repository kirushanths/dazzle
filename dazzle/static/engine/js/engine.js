window.dazzlejQuery = jQuery.noConflict(true);

window.dazzlejQuery(function(){ 

	addTextEditable();
	addImageEditable();
});


function addImageEditable()
{
	var tags = document.getElementsByTagName('*');
    var element;

	for (var i = 0, len = tags.length; i < len; i++) {
	    element = tags[i];

	    if (element.nodeName == "IMG")
	    {
	    	element.className = 'bg_found';
	    }
	    else if (element.currentStyle)
	    {
	        if( element.currentStyle['backgroundImage'] !== 'none' ) 
	        {
	            element.className += ' bg_found';
	        }
	    }
	    else if (window.getComputedStyle)
	    {
	        if( document.defaultView.getComputedStyle(element, null).getPropertyValue('background-image') !== 'none' ) 
	        {
	            element.className += ' bg_found';
	        }
	    }
	}
}

function addTextEditable()
{
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
}

var saveData = function(data)
{ 
	var dz$ = window.dazzlejQuery;
	var url = 'update' + window.location.pathname;
	dz$.post(url, data, function(response)
	{
		console.log(response); 
	});
}