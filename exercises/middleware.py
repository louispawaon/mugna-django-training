from django.contrib.auth import get_user_model
from exercises.models import Author


class AuthorMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.author:
            request.author = request.user.author

        response = self.get_response(request)
        return response
