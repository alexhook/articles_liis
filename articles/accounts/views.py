from .serializers import SignUpSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer