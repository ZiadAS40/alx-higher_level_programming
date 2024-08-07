$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  const results = data.results;
  for (const result of results) {
    $('UL#list_movies').append('<li>' + result.title + '</li>');
  }
});
