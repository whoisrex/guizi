'use strict';

/* Controllers */

// Form controller
app.factory('userListService', ['$http',
    function($http) {
        var doRequest = function(username, path) {
            return $http({
                method: "GET",
                url: '/management/api/v1/user/'
            });
        }
        return {
            userList: function(username) {
                return doRequest(username, 'userList');
            }
        };
    }
]);

app.controller('UserCtl', ['$scope', '$http', function($scope, $http) {
    $http.get("http://127.0.0.1:8000/management/api/v1/user/?format=json")
        .success(function(response) {
        $scope.users = response.objects;
            console.log($scope.users)
    });

    $scope.addUser = function() {

    }

}]);