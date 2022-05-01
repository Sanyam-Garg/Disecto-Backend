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
                    'stock': item.stock,
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
        item = Item(name=request.data['name'], stock=stock, price=price)
        item.save()

        return Response({'msg': 'Item added successfully'}, status=status.HTTP_201_CREATED)

class ListView(APIView):
    """
    This view maintains a single list in the database and
    provides the functionality to create a new list or update
    the previous one if already created.

    A get request to this url generates the invoice for the present list.
    """
    def post(self, request):
        # if 'name' not in request.data:
        #     return Response({'err': 'Item must contain a name'})
        
        # item = Item.objects.get(name=request.data['name'])
        list = List.objects.all()

        if not list:
            list = List(title='Primary List')
            list.save()
        else:
            list = list[0]
        
        return Response({'list': list.title}, status=status.HTTP_201_CREATED)