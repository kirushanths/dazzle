window.dazzlejQuery = jQuery.noConflict(true);

window.dazzlejQuery(function(){ 
 
	dzEngine.runEngine();

});


var dzEngine = (function(){

	var dz$ = window.dazzlejQuery;
	var updateUrl = "http://10.30.0.2/update" + window.location.pathname;

	/**
	 *	IMAGE FUNCTIONS
	 */
	function runImageEngine() 
	{ 
		var toolbar = createImageToolbar(); 
		toolbar.hide();

		var tags = document.getElementsByTagName('*');
	    var element;

		for (var i = 0, len = tags.length; i < len; i++) 
		{
		    element = tags[i];
		    if (element.nodeName == "BODY")	continue;
		   
		    var imageUrl = getImageFromElement(element);

		    if (imageUrl == null) continue;

		    element.className = ".dz-image";

		    addImageToolbar(element, imageUrl, toolbar);
		}
	}

	function createImageToolbar()
	{  
		var toolbar = dz$("<div id='dz-imageToolbar'> \
						  		<div class='dz-title'>Replace Image</div> \
						   		<div class='dz-preview'></div> \
						   		<div class='dz-text'>Click or drag file here </div> \
						   </div>");
		toolbar.appendTo('body');
		var dropzone = new Dropzone(toolbar.get(0), 
		{  
			parallelUploads: 5,
			clickable: true,
			maxFilesize: 5 ,
			url: updateUrl,
			previewsContainer: ".dz-preview",
			accept: function(file, done) {  
				done();
			}
		});

		toolbar.dropzone = dropzone; 

		addImageHandlers(dropzone);

		return toolbar;
	} 

	function addImageHandlers(dropzone)
	{
		dropzone.on("addedfile", function(file)
		{ 
			console.log(file);
			console.log(file.targetElement);  
			//getImageFromElement(dropzone.customData.targetElement, dropzone.c)
		});


		dropzone.on("error", function(file, message) { //alert(message); 
		}); 

		dropzone.on("success", function(file, response) {
			console.log('success'); 
			console.log(response);

			// TEMPORARY CAT PIC
			updateElementImage(file.targetElement, 'http://hdnaturepictures.com/wp-content/uploads/2013/05/Cute-Little-Cat.jpg');
			/*
			if (this.filesQueue.length == 0 && this.filesProcessing.length == 0) {
				console.log("upload complete");
		  	}
		  	*/
		});
	}

	function addImageToolbar(element, imageUrl, toolbar)
	{  
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
				toolbar.dropzone.options.targetElement = this;
			},
			function(){
			}
		); 
	}

	function updateElementImage(element, imageUrl)
	{
		if (!element || !imageUrl) return;
	 
		if (element.nodeName == "IMG")
		{  
			$(element).attr("src", imageUrl);
		}
		else
		{
			$(element).css("background-image", "url(" + imageUrl + ")"); 
	    }
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

	/**
	 *	TEXT FUNCTIONS
	 */
	function runTextEngine()
	{  
		dz$('[dztype="text"]').each(function(index){ 
			addHalloEditor(this);
			addHalloHandlers(this);
		});	
	}

	function addHalloEditor(element)
	{
		if (element.tagName == 'DIV')
		{
			dz$(element).hallo({
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
			dz$(element).hallo({
				plugins:{
					'halloformat': {}, 
					'halloreundo': {},
					'hallolink': {}
				}
			})
		}
	}

	function addHalloHandlers(element)
	{
		dz$(element).bind('hallodeactivated', function(event){ 
				var el = dz$(event.target);

				if (!el.hasClass('dzmodified')) return;

				var ident = el.attr("dzid");
				var newValue = el.html();

				saveData({'requestType':'updateText', 'id': ident,'value':newValue });

				el.removeClass('dzmodified');
			}
		);

		dz$(element).bind('hallomodified', function(event){
				var el = dz$(event.target);
				if (!el.hasClass('dzmodified'))
				{
					el.addClass('dzmodified')
				}
			}
		);
	}

	/**
	 * HELPERS
	 */
	var saveData = function(data)
	{ 
		console.log(data);    
		dz$.post(updateUrl, data, function(response)
		{
			console.log(response); 
		});
	}

	/**
	 * PUBLIC
	 */
	return {
		runEngine: function()
		{
			runImageEngine();
			runTextEngine();
		}
	}

})();