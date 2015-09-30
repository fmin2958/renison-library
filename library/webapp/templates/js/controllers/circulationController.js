var circulationController = angular.module('circulationController', []);

circulationController.controller('circulationController', ['$scope',
    function($scope) {
        $scope.changeActiveTab(CIRCULATION_TAB);
    }]);
