function Restaurants($scope, $http){
  $http.get('{% url api-restaurant_list %}').success(function(data){
    $scope.restaurants = data;
  });
}
