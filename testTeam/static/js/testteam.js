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

function LoginCtrl($scope, $http) 
{
    $scope.isMatch = true;
    $scope.isDisabled = false;
    $scope.login = function () 
    {
        $scope.isMatch = true;
        $scope.isDisabled = false;
        var btn = $("#btnLogin");
        btn.button('loading');
        $http.post('/Login', $scope.User).success(function (result) 
        {
            btn.button('reset');
            if (result.isMatch != null) 
            {
                $scope.isMatch = result.isMatch;
            }
            if (result.isDisabled != null) 
            {
                $scope.isDisabled = result.isDisabled;
            }
            if (result.isMatch != null && result.isMatch) 
            {
                window.location.href = '/Project';
            }
        });
    };
}

function RegisterCtrl($scope, $http) 
{
    $scope.userExist = false;
    $scope.register = function () 
    {
        $scope.userExist = false;
        var btn = $("#btnRegister");
        btn.button('loading');
        $http.post('/Register/Save', $scope.User).success(function (result) 
        {
            btn.button('reset');
            if (!result.created) 
            {
                $scope.userExist = true;
            }
            else 
            {
                window.location.href = '/Project';
            }
        });
    }
}

function UpdateProfileCtrl($scope, $http) 
{
	$scope.UpdateSuccess = false;
    $scope.Error = false;
    $scope.update = function () 
    {
        $scope.UpdateSuccess = false;
        $scope.Error = false;
        var btn = $("#btnUpdateProfile");
        btn.button('loading');
        $http.post('/UpdateProfile', $scope.User).success(function (result) 
        {
            if (result.Updated) 
            {
                $scope.UpdateSuccess = true;
                $scope.Error = false;
                btn.button('reset');
                window.location.href = '/Project';
            }
            else 
            {
                $scope.UpdateSuccess = false;
                $scope.Error = true;
                btn.button('reset');
            }
        });
    }
}

function ChangePasswordCtrl($scope, $http) 
{
    $scope.UpdateSuccess = false;
    $scope.Error = false;
    $scope.update = function () 
    {
        $scope.UpdateSuccess = false;
        $scope.Error = false;
        var btn = $("#btnUpdate");
        btn.button('loading');
        $http.post('/ChangePassword', $scope.User).success(function (result) 
        {
            if (result.Updated) 
            {
                $scope.UpdateSuccess = true;
                $scope.Error = false;
                btn.button('reset');
                window.location.href = '/Project';
            }
            else 
            {
                $scope.UpdateSuccess = false;
                $scope.Error = true;
                btn.button('reset');
            }
        });
    }
}

function ProjectCtrl($scope, $http) 
{
	$scope.ProjectList = [];
	$scope.Query = { PageNo: 1, ProjectName: '', Introduction: '', RowCount: 0, PageCount: 0, ClassName: "all" };
	$scope.create = function () 
	{
		var btn = $("#btnCreateProject");
        btn.button('loading');
        $http.post('/Project/Create', $scope.Project).success(function (result) 
        {
            btn.button('reset');
            $('#project_add').modal('hide');
	        $scope.query();
	    });
	}
	$scope.query = function () 
	{
		$http.post('/Project/Query', $scope.Query).success(function (result) 
		{
			$scope.ProjectList = result.data;
		});
	}
	$scope.query_inclass = function (){
		$http.post('/Project/Query', $scope.Query).success(function (result) 
		{
			$scope.ProjectListInEdit = result.data;							//更新分类里面的项目列表，区别于正常的项目列表
		});
	}
	$scope.before = 0;
	$scope.toggle = function (t) 
	{
		
		$($scope.before).collapse("hide");
		$(t).collapse("toggle");
		$scope.before = t;
	}
}

function ModelCtrl($scope, $http) 
{
	editor = UE.getEditor('editor');
}

function CaseCtrl($scope, $http) 
{
	editor = UE.getEditor('editor');
}

function ClassCtrl($scope, $http) 
{
	editor = UE.getEditor('editor');
	$scope.Class = {Project: []};
	$scope.toggle = function (p) 
    {  
		p.ck = !p.ck;
		if ( p.ck == true )
		{
			$scope.Class.Project.push(p.ProjectId);
		} 
		else
		{
			$scope.Class.Project.splice($.inArray((p.ProjectId),$scope.Class.Project),1);
		}
    }
    $scope.newclass = function()
	{
		$scope.Query.ClassName='all';
		$scope.query_inclass();
		$('#class_add').modal('show');
	}
	$scope.create = function () 
	{
		var btn = $("#btnCreateClass");
        btn.button('loading');
        $http.post('/Classes/Create', $scope.Class).success(function (result) 
        {
        	if (!result.isexist)
        	{	
        		$scope.isExist = false;
	        	btn.button('reset');
	            $('#class_add').modal('hide');
		        $scope.query_class();
		        $('#myTab a:first').tab('show');
			}
			else
			{
				$scope.isExist = true;
				btn.button('reset');
			}
        });
	}
	$scope.ClassesList = [];
	$scope.query_class = function ()
	{
		$http.post('/Classes/Query', $scope.QueryClasses).success(function (result) 
		{
			$scope.ClassesList = result.class_list;
		});
	}
	$scope.UpdateClass = { OldName : "", test:123123 };
	$scope.openUpdateClass = function () 
	{
		//先查出所有project列表
		$scope.Query.ClassName='all';
		$scope.query_inclass();  					//在projectctrl里
		//$scope.OldName = $scope.UpdateClass.OldName;
		$scope.UpdateClass.test = "hehahehaaa";
		$('#class_edit').modal('show');
	}
	$scope.update = function () 
	{
		var btn = $("#btnUpdateClass");
        btn.button('loading');
        alert($scope.UpdateClass.OldName);
    }
	$scope.deleteClass = function () 
	{
		var btn = $("#btnDeleteClass");
        btn.button('loading');
        alert("deleteclass");
        btn.button('reset');
	}
}
