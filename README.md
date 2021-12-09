## Fresh Tomatoes
It is a python package to get a movie's rotten tomatoes scores.
## Syntax
```python
import freshtomatoes as ft
movie=ft.FreshTomatoes()
movie.Scores("MOVIE_NAME")
name=movie.Scores("MOVIE_NAME",MOVIE_RELEASE_YEAR)
```
## Useage
```python
import freshtomatoes as ft
movie=ft.FreshTomatoes()
movie.Scores("aladdin")
name=movie.Scores("coco",2017)
```
## Output
`{'audiencescore': '94', 'tomatometerscore': '57'}
`
## Installation
```python
pip install freshtomatoes
```

## License
The package is available as open source under the terms of the MIT License.