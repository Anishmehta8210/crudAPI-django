from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import VcardSerializer
from .models import Vcard
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class VcardList(APIView):
    vcard = Vcard.objects.all()
    serializer = VcardSerializer(vcard,many=True)
    
    def get(self ,req ):
       
        return Response(self.serializer.data,status=200)
    
    def post(self,r):
        data = {
            "name": r.POST.get("name"),
            "contact": r.POST.get("contact"),
        }
        serializer = VcardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)

    


