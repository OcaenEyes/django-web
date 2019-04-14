from django.shortcuts import render
from .serializer import MzSerializer
from rest_framework.views import APIView
from .models import Meizitu,StandardResultPagination
# Create your views here.

class PageView(APIView):
    def get(self,request,*args,**kwargs):
        meizis = Meizitu.objects.get_queryset().order_by('id')
        page = StandardResultPagination()
        page_meizi = page.paginate_queryset(queryset=meizis,request=request,view=self)
        meizis_ser = MzSerializer(instance=page_meizi,many=True)

        return page.get_paginated_response(meizis_ser.data)