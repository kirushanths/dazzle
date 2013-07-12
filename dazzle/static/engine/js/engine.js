window.dazzlejQuery = jQuery.noConflict(true);

window.dazzlejQuery(function(){ 

	addTextEditable();
	addImageEditable();
});


function addImageEditable()
{
	var dz$ = window.dazzlejQuery;

	var toolbar = makeImageUploadToolbar(); 
	toolbar.hide();

	var tags = document.getElementsByTagName('*');
    var element;

	for (var i = 0, len = tags.length; i < len; i++) {
	    element = tags[i];

	    if (element.nodeName == "BODY")
	    {
	    	continue;
	    }

	    var image = getImageFromElement(element);
	    if (image == null) 
	    {
	    	continue;
	    } 
	    
	    element.className = ".dz-image";
 
	    dz$(element).hover(
			function(){    
				toolbar.show();
				toolbar.position({
					my: "center",
    				at: "right top+35",
    				of: this,
    				collision: "fit"
				}); 
				var previewFile = { name: "previewFile", size: 0 };
				toolbar.dropzone.options.addedfile.call(toolbar.dropzone, previewFile);
				toolbar.dropzone.options.thumbnail.call(toolbar.dropzone, previewFile, getImageFromElement(this));
			},
			function(){
			}
		); 
	}
}


function makeImageUploadToolbar()
{ 
	var dz$ = window.dazzlejQuery;
	var toolbar = dz$("<div id='dz-imageToolbar'> \
					  		<div class='dz-title'>Replace Image</div> \
					   		<div class='dz-preview'></div> \
					   		<div class='dz-text'>Click or drag file here </div> \
					   </div>");

	toolbar.appendTo('body');
	var dropzone = new Dropzone(toolbar.get(0), 
		{  
			parallelUploads: 1,
			clickable: true,
			maxFilesize: 2 ,
			url: "/file/post", 
			previewsContainer:".dz-preview",
			accept: function(file, done) {
				//done();
			}
		}
	);
 
	dropzone.on("error", function(file, message) { alert(message); }); 
	dropzone.on("complete", function() {
    	if (this.filesQueue.length == 0 && this.filesProcessing.length == 0) {
    		console.log("upload complete");
      	}
  	});
 
	toolbar.dropzone = dropzone; 

	return toolbar;
} 

function getImageFromElement(element)
{
	if (element.nodeName == "IMG")
	{
		var image = element.src;
		if (image)
		{
			return image;
		}
	}
	if (element.currentStyle)
    {
    	var image = element.currentStyle['backgroundImage'];
        if( image !== 'none' && image.match(/\.(jpg|jpeg|png|gif)/))
        { 
            return image.replace('url(','').replace(')','');
        }
    }
    else if (window.getComputedStyle)
    {
    	var image = document.defaultView.getComputedStyle(element, null).getPropertyValue('background-image');
        if( image !== 'none' && image.match(/\.(jpg|jpeg|png|gif)/))
        { 
            return image.replace('url(','').replace(')','');
        }
    }
    return null;
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