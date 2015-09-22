var renisonlibraryApp = angular.module('renisonlibraryApp', [
  'ngRoute',
  'mainControllers',
  'searchController',
  'bookDetailsController'
]);

renisonlibraryApp.config(function($routeProvider) {
    $routeProvider

        // route for the home page
        .when('/home', {
            templateUrl : 'pages/home.html',
            controller  : 'homeController'
        })

        // route for the search page
        .when('/search', {
            templateUrl : 'pages/search.html',
            controller  : 'searchController',
            reloadOnSearch : false
        })

        // route for the book details page
        .when('/detail/:bookId', {
            templateUrl : 'pages/book_detail.html',
            controller  : 'bookDetailsController'
        })

});

//Creates global functions
//Controllers can directly call these functions
//To modify globally available variables
renisonlibraryApp.run(function($rootScope){
	$rootScope.changeActiveTab = function(switchToTab){
		$rootScope.home_active_status = '';
		$rootScope.booklist_active_status = '';
		$rootScope.search_active_status = '';
		$rootScope.about_active_status = '';
		$rootScope.contact_active_status = '';
		if (switchToTab === HOME_TAB) {
			$rootScope.home_active_status = 'active';
		} else if (switchToTab === BOOKLIST_TAB) {
			$rootScope.booklist_active_status = 'active';
		} else if (switchToTab === SEARCH_TAB) {
			$rootScope.search_active_status = 'active';
		} else if (switchToTab === ABOUT_TAB) {
			$rootScope.about_active_status = 'active';
		} else if (switchToTab === CONTACT_TAB) {
			$rootScope.contact_active_status = 'active';
		}
	}
});
