from rest_framework import viewsets
from CRUD.models.user import User
from CRUD.serializers.usuarioserializer import UserSerializer

class index(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()