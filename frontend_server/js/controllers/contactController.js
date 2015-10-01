var contactController = angular.module('contactController', []);

contactController.controller('contactController', ['$scope',
	function($scope) {
		$scope.changeActiveTab(CONTACT_TAB);
	}]);
