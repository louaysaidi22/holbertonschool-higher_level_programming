$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let i = 0; i < data.results.length; i++) {
    const text = '<li>' + data.results[i].title + '</li>';
    $('UL#list_movies').append(text);
  }
});
