import json
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.files.uploadhandler import FileUploadHandler
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from outfit.forms import UserForm, ClothesForm
from outfit.models import Clothes, User


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # allows users to be redirected to home page after register
            messages.info(request, "Thanks for registering.")
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])

        # return HttpResponseRedirect(reverse("profile"))
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {
        'form': form,
    })


def login_redirect(request):
    if request.user.gender == 'M':
        return redirect('profile')
    else:
        return redirect('girly')


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
    else: form = ClothesForm()

    clothes_tops = Clothes.objects.filter(type = 'T')
    clothes_bottoms = Clothes.objects.filter(type = 'B')
    clothes_accessories = Clothes.objects.filter(type = 'A')
    clothes_shoes = Clothes.objects.filter(type = 'S')
    clothes_headwear = Clothes.objects.filter(type = 'H')

    return render_to_response('profile.html', RequestContext(request,
        {'form': form, 'big': big, 'clothes_tops': clothes_tops, 'bottoms': clothes_bottoms,
         'accessories': clothes_accessories, 'shoes': clothes_shoes, 'headwear': clothes_headwear }))


def girly(request):
    return render(request, 'girly.html',)