from rest_framework_simplejwt.views import TokenObtainPairView

from service_api.auth.responses import NomadPyTeamTokenObtainPairSerializer


class NomadPyTeamTokenObtainPairView(TokenObtainPairView):
    serializer_class = NomadPyTeamTokenObtainPairSerializer
