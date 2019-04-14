
from .serializer import YouoneSerializer
from .models import Youone,StandardResultSetPagination
from rest_framework.views import APIView

# Create your views here.

class PageView(APIView):
    def get(self,request,*args, **kwargs):
        ones = Youone.objects.get_queryset().order_by('id')
        page = StandardResultSetPagination()
        page_ones = page.paginate_queryset(queryset=ones,request=request,view=self)
        ones_ser = YouoneSerializer(instance=page_ones,many=True)

        return page.get_paginated_response(ones_ser.data)