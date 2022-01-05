from django.contrib.auth.models import User
from django.views.generic import CreateView


class AccountRegistrationView(CreateView):
    model = User
    template_name = 'accounts/registration.html'


