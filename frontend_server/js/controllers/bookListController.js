var bookListController = angular.module('bookListController', []);

var renLibBookListApiLink = 'http://45.55.82.111:8000/webapp/api/v1/book/';
var renLibBookCoverBaseApiLink = 'http://45.55.82.111:8000';

bookListController.controller('bookListController', ['$scope', '$http', '$routeParams', '$location',
	function($scope, $http, $routeParams, $location) {

		function updateCurrentPageBooks(index) {
			var books = [],
				data = $scope.listResults,
				beginIndex;

			if (index > $scope.pages - 5 && $scope.pages > 10) {
				beginIndex = $scope.pages - 10;
			} else if (index > 5) {
				beginIndex = index - 5;
			} else {
				beginIndex = 0;
			}

			for (var i = 0; i < $scope.pageNumbers.length; i++) {
				$scope.pageNumbers[i] = beginIndex + i;
			}

			for (var i = index * 10; i < index * 10 + 10; i++) {
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
			$scope.selectedPageIndex = index;
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
					var dataLength = data.books.length;
					$scope.pages = Math.ceil(data.books.length / 10);

					if ($scope.pages < 10) {
						$scope.pageNumbers = new Array($scope.pages);
					} else {
						$scope.pageNumbers = new Array(10);
					}

					if ($routeParams.page) {
						updateCurrentPageBooks($routeParams.page);
					} else {
						updateCurrentPageBooks(0);
						$location.search('page', 0);
					}
				}
			});

		$scope.pageNumberClicked = function (index) {
			$scope.selectedPageIndex = index;
			$location.search('page', index);
			updateCurrentPageBooks(index);
		};

		$scope.selectFirstPage = function () {
			if ($scope.selectedPageIndex === 0) return;
			$location.search('page', 0);
			updateCurrentPageBooks(0);
		}

		$scope.selectLastPage = function () {
			var lastIndex = $scope.pages - 1;
			if ($scope.selectedPageIndex === lastIndex) return;
			$location.search('page', lastIndex);
			updateCurrentPageBooks(lastIndex);
		}

		$scope.getDetailUrl = function (bookId) {
			return '/#/detail/' + bookId;
		}

		$scope.$on('$viewContentLoaded', function() {
			$scope.selectedPageIndex = $routeParams.page;
		});
	}]);
