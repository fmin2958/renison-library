var renisonlibraryApp = angular.module('renisonlibraryApp', [
	'ngRoute',
	'homeController',
	'searchController',
	'bookDetailsController',
	'bookListController',
	'aboutController',
	'contactController'
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

		// route for book list page
		.when('/booklist', {
			templateUrl	: 'pages/book_list.html',
			controller	: 'bookListController',
			reloadOnSearch	: false
		})

		// route for about page
		.when('/about', {
			templateUrl : 'pages/about.html',
			controller  : 'aboutController'
		})

		// route for contact page
		.when('/contact', {
			templateUrl : 'pages/contact.html',
			controller  : 'contactController'
		})

        // initially redirect to /home
        // direct to home if url not found
        .otherwise({
            redirectTo  : '/home'
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
