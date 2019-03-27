from django.shortcuts import render

# Create your views here.
def files_upload(request):
    return render(request,'files_upload.html')

def files_download(request):
    return render(request,'files_download.html')