from django.shortcuts import render ,redirect
from django.utils.crypto import get_random_string
from .models import *
import requests

def shortenView(request):
    if request.method == "POST":
        url=request.POST["url"]
        try :
            requests.get(url)
            my_url = 'http://'+request.get_host()+'/'+get_random_string(8)
            while ShortenUrl.objects.filter(originalurl=my_url).exists():
                my_url = 'http://'+request.get_host()+'/'+get_random_string(8)

            new = ShortenUrl(originalurl=url,shorturl=my_url)
            new.save()
            return render(request,"index.html",{"shorten":my_url})
        except:
            return render(request,"index.html",{"error":"DNS address could not be found for this Url"})
        

    return render(request,"index.html")


def redirectView(request,rand):
    url='http://'+request.get_host()+'/'+rand
    redirected = ShortenUrl.objects.get(shorturl=url)
    print(redirected.originalurl)

    return redirect(redirected.originalurl)