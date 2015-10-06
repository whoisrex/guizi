'use strict';

/* Controllers */

app.factory("commonService", function($http, $q) {
    var service ={};
    service.get = function(url) {
        var deferred = $q.defer();
        $http.get(url).success(
            function(data){
                deferred.resolve(data.objects);
        }).error(function() {
             deferred.reject("error!");
        });
        return deferred.promise;
    };

    service.post = function(url, data) {
        var deferred = $q.defer();
        $http.post(url, data).success(
            function(data) {
        }).error(function() {
            deferred.reject("error!");
        });
        return deferred.promise;
    };

    return service;
});

app.factory("brandService", function($http, $q, commonService) {
    var service ={};
    var url = "/management/api/v1/brand/";

    service.get = function() {
        return commonService.get(url);
    }
    service.post = function(data) {
        return commonService.post(url, data);
    }

    return service;
});

app.factory("spaceService", function($http, $q, commonService) {
    var service ={};
    var url = "/management/api/v1/productspace/";

    service.get = function() {
        return commonService.get(url);
    }
    service.post = function(data) {
        return commonService.post(url, data);
    }

    return service;
});

app.factory('articleService', function($http, $q, commonService) {
    var service ={};
    var url = "/management/api/v1/article/";

    service.get = function() {
        return commonService.get(url);
    }
    service.post = function(data) {
        return commonService.post(url, data);
    }

    return service;
})



app.controller('ProductCtl', ['$scope', '$http', function($scope, $http) {
    $http.get("/management/api/v1/product/")
        .success(function(response) {
        $scope.products = response.objects;
    });

}]);

app.controller('BrandCtl', function($scope, brandService) {
    $scope.data = {};
    $scope.listbrands = brandService.get()
            .then(function(data){
                console.log(data);
                $scope.data.brands = data;
            }, function(data) {
                alert(data);
            });
});

app.controller("NewBrandFormCtl", function($scope, brandService){
    $scope.brand = {
        name: "",
        short_content: "",
        story:"",
        cover:"",
    };
    $scope.uploads = "";
    $scope.msg = "";
    $scope.display_cover=false;

    $scope.submit_brand = function() {
        brandService.post($scope.brand).
            then(function(data){
                $scope.msg = "提交成功";
                alert($scope.msg);
            }, function(data) {
                $scope.msg = "提交失败";
                alert($scope.msg);
            })
    };

    $scope.$on("$emitOnSuccess", function(e, data) {
        $scope.brand.cover = "/management/api/v1/image/"+data.pic_id + "/";
        $scope.uploads=data.file_path;
        $scope.display_cover = true;
    });

})

app.controller('SpaceCtl', function($scope, spaceService) {
    $scope.data = {};
    $scope.listspace = spaceService.get()
            .then(function(data){
                console.log(data);
                $scope.data.spaces = data;
            }, function(data) {
                alert(data);
            });
});

app.controller('NewSpaceCtrl', function($scope, spaceService) {
    $scope.space = {
        name: "",
    };
    $scope.submit_space = function() {
        spaceService.post($scope.space).
            then(function(data){
                $scope.msg = "提交成功";
                alert($scope.msg);
            }, function(data) {
                $scope.msg = "提交失败";
                alert($scope.msg);
            })
    };

});


app.controller('articleCtrl', function($scope, articleService) {
    $scope.data = {};
    $scope.listarticles = articleService.get()
            .then(function(data){
                $scope.data.articles = data;
            }, function(data) {
                alert(data);
            });
});
