from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name="recommendation"

router = DefaultRouter()
router.register('', views.MovieListViewSet)

urlpatterns = [
    path('recommend_by_day_of_week/', views.MovieRecommendByDayViewSet.as_view({'get': 'list'})),
    path('today_user_list/', views.today_user_list),
    path('recommend_by_korea/', views.movie_in_korea),
]