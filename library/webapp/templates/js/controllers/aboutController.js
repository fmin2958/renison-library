var aboutController = angular.module('aboutController', []);

aboutController.controller('aboutController', ['$scope',
	function($scope) {
		$scope.changeActiveTab(ABOUT_TAB);
	}]);
