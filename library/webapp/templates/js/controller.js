var mainControllers = angular.module('mainControllers', []);

mainControllers.controller('homeController', ['$scope',
    function($scope) {
        $scope.message = 'Hello World';
    }]);
