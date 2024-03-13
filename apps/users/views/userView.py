from rest_framework import viewsets
from usuers.models.user import User
from usuers.serializers.usuarioserializer import UserSerializer

class index(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()