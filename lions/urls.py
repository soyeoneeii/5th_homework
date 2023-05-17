# from rest_framework_simplejwt.views import(
#     TokenObtainPairView,
#     TokenRefreshView,
# )
# from django.urls import path
# # from user.views import SpartaTokenObtainPairView
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .views import RegisterAPIView


# urlpatterns =[
#     path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
#     path('register/', RegisterAPIView.as_view(), name='register'),
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
# ]

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from lions.views import LoginAPIView, RegisterAPIView

app_name = 'lions'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]