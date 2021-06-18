from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            (UserCreationForm)(form).save()
            messages.success(request, f'Account successfully created!')
            return HttpResponseRedirect(str(self.success_url))

        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'users/profile.html'
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        ctx = {
            'username': request.user.username,
            'user_update_form': UserUpdateForm(instance=request.user),
            'profile_update_form': ProfileUpdateForm(instance=request.user.profile),
        }
        return render(request, self.template_name, context=ctx)

    def post(self, request, *args, **kwargs):
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)\

        ctx = {
            'username': request.user.username,
            'user_update_form': user_update_form,
            'profile_update_form': profile_update_form,
        }

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Your accout has been updated!')
            return HttpResponseRedirect(str(self.success_url))

        return render(request, self.template_name, context=ctx)
