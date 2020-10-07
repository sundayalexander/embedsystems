import json
import os
from datetime import datetime

import pytz
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from core.models import Project, Category, Setting
from timi.main_settings import MEDIA_ROOT, UPLOADS_DIR

tz = pytz.timezone('Africa/Lagos')


# Create your views here.
def index(request):
    return render(request, 'flex/index.html', {'setting': Setting.objects.first(),
                                               'projects': Project.objects.all()[:12]})


def portfolio(request, slug=None):
    if slug:
        try:
            project = Project.objects.get(slug=slug, status=True)
        except:
            project = None

        if project:
            return render(request, 'project.html', {'project': project})
        else:
            messages.error(request, 'Project not available', extra_tags="3000")
            return redirect('portfolio')

    return render(request, 'portfolio.html', {
        'categories': Category.objects.all(),
        'projects': Project.objects.filter(status=True)
    })


def projects(request):
    return render(request, 'flex/projects.html', {'setting': Setting.objects.first(),
                                                  'projects': Project.objects.all()})


def about(request):
    return render(request, 'flex/about.html', {'setting': Setting.objects.first()})


def contact(request):
    if request.method == "GET":
        return render(request, 'flex/contact.html', {'setting': Setting.objects.first()})
    elif request.method == "POST":
        pass


@csrf_exempt
def upload(request):
    if request.method == "GET":
        images = []
        path = UPLOADS_DIR
        valid_images = [".jpg", ".gif", ".png", ".tga"]
        for f in os.listdir(path):
            filename = os.path.splitext(f)[0]
            ext = os.path.splitext(f)[1]
            if ext.lower() not in valid_images:
                continue
            images.append({'title': filename, 'value': f'uploads/{f}'})
        return JsonResponse(data=images, safe=False)
    elif request.method == "POST":
        file = request.FILES['file']
        img_extension = os.path.splitext(file.name)[1]
        img_name = f'upload-{datetime.now(tz).timestamp()}{img_extension}'
        upload_dir = os.path.join(MEDIA_ROOT, 'uploads')
        if not os.path.exists(upload_dir):
            os.mkdir(upload_dir)
        img_save_path = os.path.join(upload_dir, img_name)
        print(img_save_path)
        with open(img_save_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)

        return JsonResponse(data={'location': img_name})
