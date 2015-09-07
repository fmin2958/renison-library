/**
 * Created by Louis Pan on 31/08/2015.
 */
'use strict';

/*Selected Tabs id*/
var HOME_TAB = 'nav-home-tab';
var BOOKLIST_TAB = 'nav-booklist-tab';
var SEARCH_TAB = 'nav-search-tab';
var ABOUT_TAB = 'nav-about-tab';
var CONTACT_TAB = 'nav-contact-tab';

/*Event Types*/
var SWITCH_TAB_EVENT = 'SWITCH_TAB_EVENT';

var ModelModule = (function(){
    var AbstractModel = function(){
        this.listeners = [];
    };

    _.extend(AbstractModel.prototype, {
        addListener: function(listener) {
            this.listeners.push(listener);
        },

        removeListener: function(listener) {
            var index = this.listeners.indexOf(listener);
            if (index !== -1) {
                this.listeners.splice(index, 1);
            }
        },

        notify: function(eventType, eventData) {
            _.each(this.listeners, function(listener){
                listener(eventType, eventData);
            });
        }
    });

    var TabModel = function(){
        AbstractModel.apply(this, arguments);

        this.currentSelectedTab = HOME_TAB;
    };

    _.extend(TabModel.prototype, AbstractModel.prototype, {
        selectTab: function(selectedTab){
            this.notify(SWITCH_TAB_EVENT, selectedTab);
            this.currentSelectedTab = selectedTab;
        },

        getCurrentTab: function(){
			return this.currentSelectedTab;
		}
    });

    return {
        TabModel: TabModel
    }
})();