from myapi.models import *
from rest_framework import serializers


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
          
class shipmentseriallizer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'
        
class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class Paymentserializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        
class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
         
class Order_itemserializer(serializers.ModelSerializer):
    class Meta:
        model = Order_item
        fields = '__all__'
                  
class Cartserializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
         
class Wishlistserializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

        


        


        
        
        

         

        
        