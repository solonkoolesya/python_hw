from django.conf import settings
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import path
import re 
import random, string

if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['']
        }]
    )
stat = {}

def random_key(stringLength=5):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


def index(request):
    context = {}
    if request.method == 'POST':
        url = request.POST.get("url")        
        if re.match(r"^https*|ftp://.*$", url): 
            key = random_key()
            cache.add(key, url)
            stat[key] = 0
            context['url_out'] = "http://localhost:8000/"+key
        else:
            context['err_out'] = "Only http, https, ftp schemas are supported"	
    return render(request, 'index.html',  context)
    
def redirect_view(request, key):  
    if cache.get(key):
        stat[key] += 1
        return redirect(to=cache.get(key))
    else:
        return redirect(to='/')


def stats(request, key):
    return render(request, 'index.html',  {'key': key, 'stat': stat[key]})

urlpatterns = [
    path('', index),
    path(r'stats/<key>', stats),
    path(r'<key>', redirect_view),
]

if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
