from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework import exceptions


User = get_user_model()


class AppSecretTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user_token = request.META.get('CL-X-TOKEN')
        if not user_token:
            return None

        try:
            user = User.objects.get(app_secret_token=user_token)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Un Authenticate')
        return (user, None)