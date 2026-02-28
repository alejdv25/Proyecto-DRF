from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from inventario.models import Producto
from inventario.models import Categoria
from inventario.serializers import ProductoSerializer, CategoriaSerializer, ProductoPosSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

# Create your views here.







class InventarioLisView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        nombre = self.request.query_params.get("nombre")
        categoria = self.request.query_params.get("categoria")
        data = Producto.objects.all()
        if nombre:
            data = data.filter(nombre_icontains=nombre)
        if categoria:
            data = data.filter(categoria_nombre_icontains=categoria)
        
        paginador = PageNumberPagination()
        page = paginador.paginate_queryset(data, request)
        serializer = ProductoSerializer(page, many=True)

       


        
        return paginador.get_paginated_response(serializer.data)
    
    def post(self, request):
        print(request.data)
        serializer = ProductoPosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

class InventarioDetailView(APIView):
    def get(self, request, pk=None):
        try:
            data = Producto.objects.get(pk=pk)
            serializer = ProductoSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Producto.DoesNotExist:
            return Response(data={"error": "Producto no encontrado"}, 
                            status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk=None):
        try:
            data = Producto.objects.get(pk=pk)
            serializer = ProductoSerializer(data, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "Producto editado"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Producto.DoesNotExist:
            return Response({"message": "No se encontro el producto"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):

        try:
            data = Producto.objects.get(pk=pk)
            serializer = ProductoSerializer(data, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "Producto editado"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Producto.DoesNotExist:
            return Response({"message": "No se encontro el producto"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk=None):
        #Consultar el registro que se busca existe
        #Si no existe devuelve un error
        #Si existe borra el producto
        try:
            data = Producto.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response({"message": "No se encontro el producto"}, status=status.HTTP_404_NOT_FOUND)



class Categorialisview(APIView):
    def get(self, request):
        
        nombre = self.request.query_params.get("nombre")
        categoria = self.request.query_params.get("categoria")
        data = Categoria.objects.all()

        if nombre:
            data = data.filter(nombre_icontains=nombre)
        if categoria:
            data = data.filter(categoria_nombre_icontains=categoria)


        serializer = CategoriaSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        serializer = CategoriaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class CategoriaDetailview(APIView):
    def get(self, request, pk=None):
        try:
            data = Categoria.objects.get(pk=pk)
            serializer = CategoriaSerializer(data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Categoria.DoesNotExist:
            return Response({"message": "La categoria no existe"},
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        try:
            data = Categoria.objects.get(pk=pk)
            serializer = CategoriaSerializer(data, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "Categoria editada"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Producto.DoesNotExist:
            return Response({"message": "No se encontro la categoria"}, status=status.HTTP_404_NOT_FOUND)
        
    def patch(self, request, pk=None):

        try:
            data = Categoria.objects.get(pk=pk)
            serializer = CategoriaSerializer(data, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message": "Categoria editada"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Producto.DoesNotExist:
            return Response({"message": "No se encontro la categoria"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        #Consultar el registro que se busca existe
        #Si no existe devuelve un error
        #Si existe borra el producto
        try:
            data = Categoria.objects.get(pk=pk)
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response({"message": "No se encontro la categoria"}, status=status.HTTP_404_NOT_FOUND)