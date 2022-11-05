from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework.decorators import action
from .models import Category, Product, Basket
from .serializer import ProductSerializer, CategorySerializer, BasketSerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def products_one_category(self, *args, **kwargs):
        products = Product.objects.filter(category=kwargs.get('pk'))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BasketViewSet(viewsets.ModelViewSet):

    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    @action(detail=True, methods=['get'])
    def add_product_in_basket(self, request, *args, **kwargs):
        serializer = BasketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

