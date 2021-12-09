from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_all),
    path('movie_list/', views.movie_list),
    path('recent/', views.movie_list_recent),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/like/', views.movie_like),
    path('<int:movie_id>/hate/', views.movie_hate),
    path('<int:movie_id>/favorite/', views.movie_favorite),
    path('<int:movie_id>/review_create/', views.review_list_create),
    # path('<int:movie_id>/review/', views.movie_review),
    # path('<int:movie_id>/review/create/', views.movie_review_create),
    path('<int:movie_id>/review/<int:review_pk>/update/', views.movie_review_update),
    path('<int:movie_id>/review/<int:review_pk>/delete/', views.movie_review_delete),
    path('<int:movie_id>/review/<int:review_pk>/like/', views.movie_review_like),
    path('<int:movie_id>/review/<int:review_pk>/hate/', views.movie_review_hate),
    path('genre_list/', views.genre_list),
    path('movie_by_genre/', views.movie_by_genre),
    path('movie_by_grade/', views.movie_by_grade),
]
