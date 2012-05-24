from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    context = {"title":"Site Base"}
    return render_to_response('index.html',context,
                context_instance=RequestContext(request))

