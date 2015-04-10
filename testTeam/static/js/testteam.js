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

function RegisterCtrl($scope, $http) {
    $scope.userExist = false;
    $scope.register = function () {
        $scope.userExist = false;
        var btn = $("#btnRegister");
        btn.button('loading');
        $http.post('/Register/Save', $scope.User).success(function (result) {
            btn.button('reset');
            if (!result.created) {
                $scope.userExist = true;
            }
            else {
                window.location.href = '/Project';
            }
        });
    }
}

function ProjectCtrl($scope, $http) {
	$scope.ProjectList = [];
	$scope.Query = { PageNo: 1, ProjectName: '', Introduction: '', RowCount: 0, PageCount: 0 };
	$scope.create = function () {
		var btn = $("#btnCreateProject");
        btn.button('loading');
        $http.post('/Project/Create', $scope.Project).success(function (result) {
            btn.button('reset');
            $('#project_add').modal('hide');
	        //$scope.query();
	    });
	}
}

function UpdateProfileCtrl($scope, $http) {
	$scope.UpdateSuccess = false;
    $scope.Error = false;
    $scope.update = function () {
        $scope.UpdateSuccess = false;
        $scope.Error = false;
        var btn = $("#btnUpdateProfile");
        btn.button('loading');
        $http.post('/UpdateProfile', $scope.User).success(function (result) {
            if (result.Updated) {
                $scope.UpdateSuccess = true;
                $scope.Error = false;
            }
            else {
                $scope.UpdateSuccess = false;
                $scope.Error = true;
            }
            btn.button('reset');
            window.location.href = '/Project';
        });
    }
}