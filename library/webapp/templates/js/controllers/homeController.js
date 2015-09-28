var homeController = angular.module('homeController', []);

//Constant Strings used to switch tabs
var HOME_TAB = 'home';
var BOOKLIST_TAB = 'booklist';
var SEARCH_TAB = 'search';
var ABOUT_TAB = 'about';
var CONTACT_TAB = 'contact';
var googleBookApiLink = 'https://www.googleapis.com/books/v1/volumes';

homeController.controller('homeController', ['$scope',
    function($scope) {
        $scope.message = 'This is home page';
		$scope.changeActiveTab(HOME_TAB);
    }]);
