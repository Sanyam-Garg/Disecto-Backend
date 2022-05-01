from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework import status

# Create your views here.
class AllItems(APIView):
    """
    View to get or update information about the items stored in the 'Item' model.
    """
    def get(self, request):
        try:
            items = Item.objects.all().order_by('name')
            data = []

            for item in items:
                data.append({
                    'name': item.name,
                    'available_stock': item.available_stock,
                    'price': item.price,
                })
            
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response({'err': 'Please try again later'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        # Return an error if no name given
        if 'name' not in request.data:
            return Response({'err': 'Item must contain a name'})

        # Set default values for stock and price if not given
        stock = None
        price = None
        if 'stock' not in request.data:
            stock = 100
        else:
            stock=request.data['stock']
        if 'price' not in request.data:
            price = 100
        else:
            stock=request.data['price']
        item = Item(name=request.data['name'], initial_stock=stock, price=price)
        item.save()

        return Response({'msg': 'Item added successfully'}, status=status.HTTP_201_CREATED)

class ListView(APIView):
    """
    This view maintains a single list in the database and
    provides the functionality to create a new list or update
    the previous one if already created.
    """
    def get(self ,request):
        list = List.objects.all()

        if not list:
            list = List(title='Primary List')
            list.save()
        else:
            list = list[0]
        
        data = [{'title': list.title}]
        for item in list.list_items.all().order_by('name'):
            data.append({
                'name': item.name,
                'quantity': item.initial_stock - item.available_stock,
                'price': item.price
            })
        
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if 'name' not in request.data:
            return Response({'err': 'Item must contain a name'})
        if 'quantity' not in request.data:
            return Response({'err': 'Item must contain a name'})

        item = Item.objects.get(name=request.data['name'])
        list = List.objects.all()[0]
        item.list = list
        item.available_stock -= request.data['quantity']
        item.save()

        return Response({'msg': 'Item added successfully'}, status=status.HTTP_201_CREATED)