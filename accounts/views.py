from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserEditView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("home")
    template_name = "registration/edit_profile.html"

    def get_object(self, queryset=None):
        return self.request.user
