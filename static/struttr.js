function Struttr($scope, $http) {
    getboasts = function () {
        $http.get("/boasts").
        success(function (data, status, headers, config) {
            // this callback will be called asynchronously
            // when the response is available
            $scope.boasts = data.json
        }).
        error(function (data, status, headers, config) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
            // do nothing for now
        });
    }
    getboasts();


    $scope.boast = function () {
        $http.post("/boast", {boast: $scope.imad}).
        success(function () {
            getboasts()
            $scope.imad = ""
        });
    }


    $scope.boat = function (id) {
        $http.post("/boat", {boat: id}).
        success(function () {
            getboasts()
        });
    }
}

