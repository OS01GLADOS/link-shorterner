from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from short_link_user.forms import UserRegisterForm, GenerateShortLinkForm
from short_link_user.models import ShortedLink


@login_required
def index(request):
    form = GenerateShortLinkForm()
    return render(request, 'short_link_user/index.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'short_link_user/register.html', {'form': form})


class UserShortLinkListView(ListView):
    model = ShortedLink
    context_object_name = 'Links'
    template_name = 'short_link_user/user_shorted_links.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return ShortedLink.objects.filter(creator=user)
