var collectionController = angular.module('collectionController', []);

collectionController.controller('collectionController', ['$scope',
    function($scope) {
        $scope.changeActiveTab(COLLECTION_TAB);
    }]);
