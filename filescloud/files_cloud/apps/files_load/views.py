from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Upload

# Create your views here.
def files_upload(request):
    if request.method == 'GET':
        return render(request,'files_upload.html')

    if request.method == 'POST':
        file = request.FILES.get('myfile')

        if not file:
            return HttpResponse("no files for upload")
        else:
            file_url = settings.MEDIA_ROOT + '/files/' + file.name
            with open(file_url,'wb+') as f:
                # 分块写入文件
                for chunk in file.chunks():
                    f.write(chunk)
            model = Upload()
            model.name = file.name

            model.save()
            return HttpResponse("upload over!")




def files_download(request):
    return render(request,'files_download.html')