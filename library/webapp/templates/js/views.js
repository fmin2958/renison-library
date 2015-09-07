/**
 * Created by Louis Pan on 31/08/2015.
 */
'use strict';

var ViewModule = (function(){
    var AbstractView = function(){
		this.listeners = [];
    };

    _.extend(AbstractView.prototype, {

		addListener: function(listener) {
			this.listeners.push(listener);
		},

		removeListener: function(listener) {
			var index = this.listeners.indexOf(listener);
			if (index !== -1) {
				this.listeners.splice(index, 1);
			}
		},

        notify: function(event) {
            _.each(this.listeners, function(listener){
                listener(event);
            });
        },

        init: function(){

        }
    });

    var TabView = function(){
        AbstractView.apply(this, arguments);

        this.model = undefined;

        this.init();
    };

    _.extend(TabView.prototype, AbstractView.prototype, {
        bindModel: function(model){
            this.model = model;
			this.model.addListener(function(eventType, eventData){
				if (eventType === SWITCH_TAB_EVENT){
					$('.nav.nav-tabs.nav-justified > li').each(function(){
						var self = this;
						if (self.id !== eventData) {
							self.className = "";
						} else {
							self.className = "active";
						}
					});
				}
			});
        }
    });

    return {
        TabView: TabView
    };
})();