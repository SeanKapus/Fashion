import json
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.files.uploadhandler import FileUploadHandler
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from forms import *

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # allows users to be redirected to home page after register
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect(reverse("profile"))

            # return redirect(reverse("profile"))
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {
        'form': form,
    })


@login_required()
def profile(request):
    big = Clothes.objects.all()
    if request.method == 'POST':
        form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            clothes = form.save(commit=False)
            clothes.client = request.user
            clothes.save()

            # FileUploadHandler(request.FILES['image'])
            return HttpResponseRedirect('/profile')
    else:
        form = ClothesForm()
    return render_to_response('profile.html', RequestContext(request, {'form': form, 'big': big}))


# def ClothesAll(request):
#     clothes = Clothes.objects.all().order_by('name')
#     context = {'clothes': clothes}
#     return render_to_response('clothesall', context, context_instance=RequestContext(request))

# def tops(request):
#     data = {
#         'clothes': Clothes.objects.all()
#     }
#     return render(request, 'profile.html', data)

@csrf_exempt
def getall(request):
    print request.user.id
    print Clothes.objects.filter(client=request.user.id)
    data = Clothes.objects.filter(client=request.user.id, type='T')
    # clothes_objects = Clothes.objects.all()
    # collection = []
    # for object in clothes_objects:
    #     collection.append({
    #         'image': object.i.fields.image,
    #
    #     })

    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
