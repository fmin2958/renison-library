var searchController = angular.module('searchController', []);

var googleBookApiLink = 'https://www.googleapis.com/books/v1/volumes';

searchController.controller('searchController', ['$scope', '$http', '$routeParams', '$location', 
    function($scope, $http, $routeParams, $location) {

        function updateCurrentPageBooks(data, beginIndex) {
            var books = [];
            for (var i = beginIndex * 10; i < beginIndex * 10 + 10; i++) {
                books.push(data[i]);
            }
            $scope.currentPageBooks = books;
            $scope.noResults = false;
        }

        $scope.changeActiveTab(SEARCH_TAB);
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

            $http.get(googleBookApiLink, {
                params : {
                    q: keyWord,
                    maxResults: 40
                }
            })
            .success(function (data, status) {
                if (status === 200) {
                    if (data.totalItems == 0) {
                        $scope.searchResults = null;
                        $scope.noResults = true;
                        return;
                    }
                    $scope.searchResults = data.items;
                    updateCurrentPageBooks(data.items, beginPage);

                    if (data.totalItems < 10) {
                        $scope.endingPageNumber = 1;
                    } else {
                        $scope.endingPageNumber = new Array(data.items.length / 10);
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
