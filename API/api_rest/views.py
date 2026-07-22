from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Product
from .serializers import UserSerializer, ProductSerializer

import json

# CRUD dos Users
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def users_manager(request):
    """Essa função gerencia os métodos GET, POST, PUT e DELETE para a tabela de Users, ou seja, é o CRUD dos Users."""
    
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')
            user_email = request.GET.get('user_email')

            if user_id:
                try:
                    user = User.objects.get(user_id=user_id)
                except User.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)

            if user_email:
                try:
                    user = User.objects.get(user_email=user_email)
                except User.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'POST':
        new_user = request.data
        
        serializer = UserSerializer(data=new_user)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        user_id = request.data['user_id']
        
        try:
            updated_user = User.objects.get(pk=user_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(updated_user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            user = User.objects.get(user_id=request.data['user_id'])
            user.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Métodos GET
@api_view(['GET'])
def get_users(request):
    """Essa função retorna TODOS os usuários cadastrados no banco de dados."""
    
    if request.method == 'GET':
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_by_username(request, name):
    """Essa função retorna um usuário específico, de acordo com o NOME passado na URL."""
    
    if request.method == 'GET':
        try:
            user = User.objects.get(user_name=name)
            
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'PUT':
        try:
            user = User.objects.get(user_name=name)
            
            serializer = UserSerializer(user, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)





# CRUD dos Products
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def products_manager(request):
    """Essa função gerencia os métodos GET, POST, PUT e DELETE para a tabela de Products, ou seja, é o CRUD dos Products."""
    
    if request.method == 'GET':
        try:
            if request.GET['product_id']:
                product_id = request.GET['product_id']
                
                try:
                    product = Product.objects.get(product_id=product_id)
                except Product.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = ProductSerializer(product)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method == 'POST':
        new_product = request.data
        
        serializer = ProductSerializer(data=new_product)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        product_id = request.data['product_id']
        
        try:
            updated_product = Product.objects.get(pk=product_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(updated_product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    elif request.method == 'DELETE':
        try:
            product = Product.objects.get(product_id=request.data['product_id'])
            product.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

# Métodos GET dos Products
@api_view(['GET'])
def get_products(request):
    
    if request.method == 'GET':
        products = Product.objects.all()
        
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_by_productname(request, name):
    """Essa função retorna um produto específico, de acordo com o NOME passado na URL."""
    
    if request.method == 'GET':
        try:
            product = Product.objects.get(product_name=name)
            
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        try:
            product = Product.objects.get(product_name=name)
            
            serializer = ProductSerializer(product, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)
