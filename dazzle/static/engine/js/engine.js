
//$.fn.editable.defaults.mode = 'inline';

$(function(){ 
	
	$('* [dztype="text"]').filter(function(){
 
		var height = $(this).height();
		var type = 'text';
		if (height > 60) type = 'textarea';

		$(this).editable({
			disabled: false,
			type: type,
			unsavedclass:null,
			error: printError,
			value: $(this).text(),
			success: function(response, newValue) {
				
			}, 
		});
 
	});
 
 
}); 

var printError = function(response, newValue) 
{ 
  console.log(response);  
}  
