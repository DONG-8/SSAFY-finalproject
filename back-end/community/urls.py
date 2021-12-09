from django.urls import path
from . import views

app_name="community"

urlpatterns = [
    path('', views.community_list),
    path('community_create/', views.community_create),
    path('<int:community_id>/', views.community_detail),
    path('<int:user_pk>/delete/<int:community_id>/', views.community_delete),
    path('<int:community_id>/update/', views.community_update),
    path('<int:community_id>/like/', views.community_like),
    path('<int:community_id>/hate/', views.community_hate),
    path('<int:community_id>/review_create/', views.review_list_create),
    path('<int:community_id>/review/<int:review_pk>/update/', views.community_review_update),
    path('<int:community_id>/review/<int:review_pk>/delete/', views.community_review_delete),
    path('<int:community_id>/review/<int:review_pk>/like', views.community_review_like),
    path('<int:community_id>/review/<int:review_pk>/hate', views.community_review_hate),
]
