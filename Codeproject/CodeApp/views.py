from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Products,Companies
from.serilalizers import ProductSerilaizer,CompanySerilaizer
from rest_framework.response import Response
# Create your views here.

class CompanyAPIView(ListAPIView):
    queryset=Companies.objects.all()
    serializer_class= CompanySerilaizer

class ProductAPIView(ListAPIView):
    queryset=Products.objects.all()
    serializer_class= ProductSerilaizer

class Product_Create(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerilaizer(queryset,many=True)
    print(serializer_class.data)


    # def get_queryset(self):
    #     qs=Products.objects.all()
    #     Name=self.request.GET.get('Name')
    #     if Name is not None:
    #         qs=qs.filter(Name__icontains=Name)




