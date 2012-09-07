from func_tools import wrap
from django.http import HttpResponse
import simplejson

def login_required(view):
    @wrap
    def _inner(request, *a, **kw):
        if request.user.is_authenticated():
            return view(request, *a, **kw)
        else:
            json = simplejson.dumps({'not_authenticated': True})
            return HttpResonse(json, mimetype='application/json')
    return _inner
