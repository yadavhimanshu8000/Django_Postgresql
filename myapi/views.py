from django.shortcuts import render
from myapi.serializer import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class Userview(APIView):
    def get(self,request,format=None):
        store = User.objects.all()
        serializer = Userserializer(store,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Usercurd(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        curd = self.get_object(pk)
        serializer = Userserializer(curd)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED) 
    
    
    
    
class Productview(APIView):
    def get(self,request,format=None):
        store = Product.objects.all()
        serializer = Productserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Productcurd(APIView):
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        curd = self.get_object(pk)
        serializer = Productserializer(curd)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        curd = self.get_object(pk)
        serializer = Productserializer(curd,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        curd = self.get_object(pk)
        curd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
   
    
class Wishlistview(APIView):
    def get(self,request,format=None):
        store = Wishlist.objects.all()
        serializer = Wishlistserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=True):
        serializer = Wishlistserializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Wishlistcurd(APIView):
    
    def get_object(self,pk):
        try:
            return Wishlist.objects.get(pk=pk)
        except Wishlist.DoesNotExist:
            raise Http404
        
    def delete(self,request,pk,format=None):
        curd = self.get_object(pk)
        curd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class Cartview(APIView):
    def get(self,request,format=None):
        store = Cart.objects.all()
        serializer = Cartserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = Cartserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Cartcurd(APIView):
    def get_object(self,pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        curd = self.get_object(pk)
        serializer = Cartserializer(curd)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk,format=None):
        curd = self.get_object(pk)
        serializer = Cartserializer(curd,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        curd = self.get_object(pk)
        curd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
class Orderview(APIView):
    def get(self,request,format=None):
        store = Order.objects.all()
        serializer = Orderserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
       
    def post(self,request,format=True):
        serializer = Orderserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    




class Categoryview(APIView):
    def get(self,request,format=None):
        store = Category.objects.all()
        serializer = Categoryserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = Categoryserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class Paymentview(APIView):
    def get(self,request,format=None):
        store = Payment.objects.all()
        serializer = Paymentserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = Paymentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
class Shipmentview(APIView):
    def get(self,request,format=None):
        store = Shipment.objects.all()
        serializer = shipmentseriallizer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = shipmentseriallizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    
    
class Order_item_view(APIView):
    def get(self,request,format=None):
        store = Order_item.objects.all()
        serializer = Order_itemserializer(store,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = Order_itemserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class Order_item_curd(APIView):
    
    def get_object(self,pk):
        try:
            return Order_item.objects.get(pk=pk)
        except Order_item.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,format=None):
        curd = self.get_object(pk)
        serializer = Order_itemserializer(curd)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    

    
    
    
       
    

        
    
    
    
    
        
        
        
        
    
    
    
    
        
        
    
    
            
        
    
