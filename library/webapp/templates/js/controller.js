var mainControllers = angular.module('mainControllers', []);

mainControllers.controller('homeController', ['$scope',
    function($scope) {
        $scope.message = 'This is home page';
    }]);

mainControllers.controller('searchController', ['$scope',
    function($scope) {
        $scope.message = 'This is search page';
    }]);
