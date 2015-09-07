/**
 * Created by Louis Pan on 31/08/2015.
 */
'use strict';

(function(Models, Views){
    $(document).ready(function(){
        var tabModel = new Models.TabModel();
        var tabView = new Views.TabView();
        tabView.bindModel(tabModel);

		$('.nav.nav-tabs.nav-justified > li').each(function(){
			var thisId = $(this).attr('id');
			$(this).click(function(){
				tabModel.selectTab(thisId);
			});
		});

		$('.pageDiv').each(function(){
			//Remove '_div' at the end of id
			var divName = this.id.substr(0, this.id.length-4);
			var self = this;

			tabModel.addListener(function(eventType, eventData){
				if (eventType === SWITCH_TAB_EVENT){
					if (eventData.indexOf(divName) !== -1){
						//Switch to the div
						$(self).removeClass('hidden');
					} else {
						if (!$(self).hasClass('hidden')){
							$(self).addClass('hidden');
						}
					}
				}
			});
		});
    });
})(ModelModule, ViewModule);