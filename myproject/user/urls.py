from django.urls import path
from .views import LoginView,SignUpAPIview

urlpatterns=[
    path('login/', LoginView.as_view(),name='login'),
    path('sign-up/',SignUpAPIview.as_view(),name='sign_up')
]