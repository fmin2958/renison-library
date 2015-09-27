var searchController = angular.module('searchController', []);

var renLibSearchBaseApiLink = 'http://45.55.82.111:8000/webapp/api/v1/book/search/?';
var renLibBookCoverBaseApiLink = 'http://45.55.82.111:8000';

searchController.controller('searchController', ['$scope', '$http', '$routeParams', '$location', 
    function($scope, $http, $routeParams, $location) {

        function updateCurrentPageBooks(data, beginIndex) {
            var books = [];
            for (var i = beginIndex * 10; i < beginIndex * 10 + 10; i++) {
                //Skip to next one if for some reason data[i] is undefined
                //Also solves the bug where data.length < 10, 'undefined'
                //will be pushed into books, causing angularjs to complain
                if (data[i] === undefined) {
                    continue;
                }
                books.push(data[i]);
            }
            $scope.currentPageBooks = books;
            $scope.noResults = false;
        }

        $scope.changeActiveTab(SEARCH_TAB);
		//Set the base get api for image cover src
		$scope.bookCoverBaseApi = renLibBookCoverBaseApiLink;
        $scope.selectedPageIndex = 0;
        $scope.noResults = false;

        //TODO
        // $scope.filter = function () {
        //     console.log($scope.searchInput);
        // };

        $scope.searchAction = function (keyWord, beginPage) {
            if (!keyWord) return;
            $location.search('text', keyWord);


            if (!beginPage) {
                beginPage = 0;
            }


            $http.get(renLibSearchBaseApiLink, {
				params : {
					field: 'title',
					keyword: keyWord
				}})
            .success(function (data, status) {
                if (status === 200) {
                    if (data.books.length == 0) {
                        $scope.searchResults = null;
                        $scope.noResults = true;
                        return;
                    }
                    $scope.searchResults = data.books;
                    updateCurrentPageBooks(data.books, beginPage);

                    if (data.books.length < 10) {
                        $scope.endingPageNumber = 1;
                    } else {
                        $scope.endingPageNumber = new Array(Math.ceil(data.books.length / 10));
                    }

                    $location.search('page', beginPage);
                    $scope.searchInput = keyWord;
                }
            });

        };

        $scope.pageNumberClicked = function ($index) {
            $scope.selectedPageIndex = $index;
            $location.search('page', $index);
            updateCurrentPageBooks($scope.searchResults, $index);
        };

        $scope.selectFirstPage = function () {
            if ($scope.selectedPageIndex === 0) return;
            $scope.selectedPageIndex = 0;
            $location.search('page', 0);
            updateCurrentPageBooks($scope.searchResults, 0);
        }

        $scope.selectLastPage = function () {
            var lastIndex = $scope.endingPageNumber.length - 1;
            if ($scope.selectedPageIndex === lastIndex) return;
            $scope.selectedPageIndex = lastIndex;
            $location.search('page', lastIndex);
            updateCurrentPageBooks($scope.searchResults, lastIndex);
        }

        $scope.getDetailUrl = function (bookId) {
            return '/#/detail/' + bookId;
        }

        $scope.$on('$viewContentLoaded', function() {
            if ($routeParams.text) {
                ($scope.searchAction)($routeParams.text, $routeParams.page);
                $scope.selectedPageIndex = $routeParams.page;
            }
        });
    }]);
