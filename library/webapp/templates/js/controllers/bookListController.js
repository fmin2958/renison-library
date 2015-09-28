var bookListController = angular.module('bookListController', []);

var renLibBookListApiLink = 'http://45.55.82.111:8000/webapp/api/v1/book/';
var renLibBookCoverBaseApiLink = 'http://45.55.82.111:8000';

bookListController.controller('bookListController', ['$scope', '$http', '$routeParams', '$location',
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

		$scope.changeActiveTab(BOOKLIST_TAB);
		//Set the base get api for image cover src
		$scope.bookCoverBaseApi = renLibBookCoverBaseApiLink;
		$scope.selectedPageIndex = 0;
		$scope.noResults = false;

		$http.get(renLibBookListApiLink)
			.success(function (data, status) {
				if (status === 200) {
					if (data.books.length == 0) {
						$scope.listResults = null;
						$scope.noResults = true;
						return;
					}
					$scope.listResults = data.books;
					updateCurrentPageBooks(data.books, 0);

					if (data.books.length < 10) {
						$scope.endingPageNumber = 1;
					} else if (data.books.length > 100){
						//TODO: right now hard code the max allowed pages to be 10
						$scope.endingPageNumber = new Array(10);
					}
					else {
						$scope.endingPageNumber = new Array(Math.ceil(data.books.length / 10));
					}

					$location.search('page', 0);
				}
			});

		$scope.pageNumberClicked = function ($index) {
			$scope.selectedPageIndex = $index;
			$location.search('page', $index);
			updateCurrentPageBooks($scope.listResults, $index);
		};

		$scope.selectFirstPage = function () {
			if ($scope.selectedPageIndex === 0) return;
			$scope.selectedPageIndex = 0;
			$location.search('page', 0);
			updateCurrentPageBooks($scope.listResults, 0);
		}

		$scope.selectLastPage = function () {
			var lastIndex = $scope.endingPageNumber.length - 1;
			if ($scope.selectedPageIndex === lastIndex) return;
			$scope.selectedPageIndex = lastIndex;
			$location.search('page', lastIndex);
			updateCurrentPageBooks($scope.listResults, lastIndex);
		}

		$scope.getDetailUrl = function (bookId) {
			return '/#/detail/' + bookId;
		}

		$scope.$on('$viewContentLoaded', function() {
			$scope.selectedPageIndex = $routeParams.page;
		});
	}]);
