from django.urls import path
from .views import IndexTemplate, CreateUserView

urlpatterns = [
    path('', IndexTemplate.as_view()),
    path('create/', CreateUserView.as_view()),
]
