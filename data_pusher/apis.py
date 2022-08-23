from rest_framework.views import APIView
from .serializers import UserCreateSerializer


class UserCreateView(APIView):
    serializer_class = UserCreateSerializer
    def post(self, data):
        serializer = self.serializer_class(data)
        serializer.validate(raise_exception=True)

        print(serializer)