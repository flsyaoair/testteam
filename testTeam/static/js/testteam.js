var app = angular.module('TestTeam', []);

$(function () {
    $('input, textarea').placeholder();
    $('.default-focus').focus();
    $("[data-toggle='tooltip']").tooltip();
    $(".tooltips").tooltip();
    $('*').tooltip({
        selector: "[data-toggle=tooltip]",
        container: "body"
    });
});

app.filter('to_trusted', ['$sce', function ($sce) {
    return function (text) {
   return $sce.trustAsHtml(text);
    };
}]);

function LoginCtrl($scope, $http) {
    $scope.isMatch = true;
    $scope.isDisabled = false;
    $scope.login = function () {
        $scope.isMatch = true;
        $scope.isDisabled = false;
        var btn = $("#btnLogin");
        btn.button('loading');
        $http.post('/Login', $scope.User).success(function (result) {
            btn.button('reset');
            if (result.isMatch != null) {
                $scope.isMatch = result.isMatch;
            }
            if (result.isDisabled != null) {
                $scope.isDisabled = result.isDisabled;
            }
            if (result.isMatch != null && result.isMatch) {
                window.location.href = '/Project';
            }
        });
    };
}