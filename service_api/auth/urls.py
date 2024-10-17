from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from service_api.auth.views import NomadPyTeamTokenObtainPairView

service_api_auth_urlpatterns = [
    path('api/v1/users/token', NomadPyTeamTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/users/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
