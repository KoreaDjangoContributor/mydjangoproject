from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.PostListCreateAPIView.as_view(), name="list-create"),
    path("<int:pk>/", views.PostRetrieveUpdateDestroyAPIView.as_view(), name="retrieve-update-destroy"),
]
