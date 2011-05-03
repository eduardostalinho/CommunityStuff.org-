from django.shortcuts import render_to_response
from django.template import RequestContext

def welcome(request):
    return render_to_response('index.html', RequestContext(request))

def header(request):
    return render_to_response('header.html', RequestContext(request))

def body(request):
    return render_to_response('body.html', RequestContext(request))
