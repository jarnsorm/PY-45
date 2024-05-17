from django.http import HttpResponseRedirect
from django.urls import reverse


class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path == reverse('accounts:account'):
            return HttpResponseRedirect(reverse('registration/select.html'))
        response = self.get_response(request)

        return response
