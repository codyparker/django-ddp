from django_cas_ng import views as baseviews
from django.views.decorators.csrf import csrf_exempt

"""
Handles login from CAS client from meteor.
Extends the login method to add the meteor token generated on the client-side.
This allows for ddp login to confirm that the requestor is the same as the CAS auth'd user
"""
@csrf_exempt
def login(request, **kwargs):
    return _add_meteor_token(request, baseviews.login(request, **kwargs))


def _add_meteor_token(request, response):
    token = request.GET.get('meteor_token')
    request.session['meteor_token'] = token
    return response

