var bookDetailsController = angular.module('bookDetailsController', []);

var googleBookApiLink = 'https://www.googleapis.com/books/v1/volumes';

bookDetailsController.controller('bookDetailsController', ['$scope', '$http', '$routeParams', 
    function($scope, $http, $routeParams) {
        $scope.changeActiveTab(SEARCH_TAB);

        $http.get(googleBookApiLink + '/' + $routeParams.bookId)
        .success(function (data, status) {
            if (status === 200) {
                $scope.currentBook = data.volumeInfo;
            }
        });
    }]);
