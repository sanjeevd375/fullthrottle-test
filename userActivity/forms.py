from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import FTUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = FTUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = FTUser
        fields = ('email',)
