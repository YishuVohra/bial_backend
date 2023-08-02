from rest_framework.authentication import BaseAuthentication


class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if request.path.startswith('/api/customer_app/'):
            from customer_module.backends import JWTAuthentication
            return JWTAuthentication().authenticate(request)
        else:
            from user.backends import JWTAuthentication
            return JWTAuthentication().authenticate(request)