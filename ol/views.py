from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe

# Create your views here.
from . import medal

def medallist(request):
    u=medal.u
    context = {'u': u}
    # 载入模板，并返回context对象
    return render(request, 'ol/ol.html', u)

