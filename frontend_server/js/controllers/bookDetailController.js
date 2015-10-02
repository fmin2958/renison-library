var bookDetailsController = angular.module('bookDetailsController', []);

var renLibBookDetailBaseApiLink = 'http://45.55.82.111:8000/webapp/api/v1/book/';
var renLibBookCoverBaseApiLink = 'http://45.55.82.111:8000';

bookDetailsController.controller('bookDetailsController', ['$scope', '$http', '$routeParams', 
    function($scope, $http, $routeParams) {
        $scope.changeActiveTab(SEARCH_TAB);

        $http.get(renLibBookDetailBaseApiLink + $routeParams.bookId + '/')
        .success(function (data, status) {
            if (status === 200) {
                $scope.currentBook = data;
				$scope.coverBaseApiLink = renLibBookCoverBaseApiLink;
            }
        });
    }]);
