var renisonlibraryApp = angular.module('renisonlibraryApp', [
  'ngRoute',
  'mainControllers'
]);

renisonlibraryApp.config(function($routeProvider) {
    $routeProvider

        // route for the home page
        .when('/', {
            templateUrl : 'pages/home.html',
            controller  : 'homeController'
        })

        // route for the search page
        .when('/search', {
            templateUrl : 'pages/search.html',
            controller  : 'searchController'
        })

});
