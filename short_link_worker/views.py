import base64

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from short_link_user.models import ShortedLink


def resolve_link(request, identifier):
    link_data = get_object_or_404(ShortedLink, Q(short_url=identifier))
    return redirect(link_data.orig_url)


@login_required
def generate_link(request):
    result = ''
    if request.method == 'POST':
        data = request.POST.get('link', 'no-link(')
        user = get_object_or_404(User, id=int(request.POST.get('user', -1)))
        shorted_link = ShortedLink(creator_id=user.id, orig_url=data)
        shorted_link.save()
        shorted_url = base64.b64encode(str(shorted_link.id)
                                       .encode('ascii')).decode()
        shorted_link.short_url = shorted_url.replace('=', '')
        shorted_link.save()
        result = shorted_link.get_absolute_url()
    return HttpResponse(result)
