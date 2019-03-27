from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def files_upload(request):
    if request.method == 'GET':
        return render(request,'files_upload.html')

    if request.method == 'POST':
        file = request.Files.get('upload')
        if not file:
            return HttpResponse("no files for upload")


def files_download(request):
    return render(request,'files_download.html')