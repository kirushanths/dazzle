window.dazzlejQuery = jQuery.noConflict(true);

window.dazzlejQuery(function(){ 

	addTextEditable();
	addImageEditable();
});


function addImageEditable()
{
	var dz$ = window.dazzlejQuery;

	findImageElements();

	var toolbar = makeImageUploadToolbar(); 
	toolbar.hide();

	dz$('.dz-image').each(function(index){
		dz$(this).hover(
			function(){    
				toolbar.show();
				toolbar.position({
					my: "center",
    				at: "center",
    				of: this,
    				collision: "fit"
				}); 
			},
			function(){
			}
		);
	});
}

function makeImageUploadToolbar()
{ 
	var dz$ = window.dazzlejQuery;
	var toolbar = dz$("<div>upload new image upload new image image upload new image image upload new image image upload new image </div>");
	toolbar.attr('id','dz-imageToolbar');
	toolbar.appendTo('body');
	toolbar.css({  
		"height": "100px",
		"width": "100px"
	}); 
	return toolbar;
}

function findImageElements()
{

	var tags = document.getElementsByTagName('*');
    var element;

	for (var i = 0, len = tags.length; i < len; i++) {
	    element = tags[i];

	    if (element.nodeName == "BODY")
	    {
	    	continue;
	    }

	    if (element.nodeName == "IMG")
	    {
	    	element.className = 'dz-image';
	    }
	    else if (element.currentStyle)
	    {
	        if( element.currentStyle['backgroundImage'] !== 'none' ) 
	        {
	            element.className += 'dz-image';
	        }
	    }
	    else if (window.getComputedStyle)
	    {
	        if( document.defaultView.getComputedStyle(element, null).getPropertyValue('background-image') !== 'none' ) 
	        {
	            element.className += ' dz-image';
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

		if (this.tagName == 'DIV')
		{
			dz$(this).hallo({
		        plugins: {
			      'halloformat': {}, 
			      'halloblock':{},
			      'hallojustify': {},
			      'hallolists': {},
			      'halloreundo': {},
			      'halloheadings': {},
			      'hallolink': {}
		        }
		    });
		}
		else
		{
			dz$(this).hallo({
				plugins:{
					'halloformat': {}, 
					'halloreundo': {},
					'hallolink': {}
				}
			})
		}

	});	

	dz$(this).bind('hallodeactivated', function(event){ 
			var element = dz$(event.target);

			if (!element.hasClass('dzmodified')) return;

			var ident = element.attr("dzid");
			var newValue = element.html();

			saveData({'type':'saveText', 'id': ident,'value':newValue });

			element.removeClass('dzmodified');
		}
	);

	dz$(this).bind('hallomodified', function(event){
			var element = dz$(event.target);
			if (!element.hasClass('dzmodified'))
			{
				element.addClass('dzmodified')
			}
		}
	);

}

var saveData = function(data)
{ 
	console.log(data);   
	var dz$ = window.dazzlejQuery;
	var url = 'update' + window.location.pathname;
	dz$.post(url, data, function(response)
	{
		console.log(response); 
	});
}