from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    
    
    
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name
    
    
    
class Shipment(models.Model):
    shipment_id = models.IntegerField(primary_key=True)
    shipment_date = models.DateField(default=datetime.datetime.today) 
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='customer')
    
    def __str__(self):
        return self.country
    
    

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    sku = models.CharField(max_length=100)
    description = models.CharField(max_length=250) 
    price = models.IntegerField()
    stock = models.IntegerField()
   
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    
    def __str__(self):
        return f"SKU {self.sku} - Category id: {self.category_id}"
    
    

class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)
    amount = models.FloatField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='payment')
    
    
    def __str__(self):
        return f"Payment Method #{self.payment_method} | User ID: {self.user_id_id} | Payment Date: ₹{self.payment_date}"
        
    

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_date = models.DateField(auto_now_add=True)
    total_price = models.FloatField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    payment_id = models.ForeignKey(Payment,on_delete=models.CASCADE,related_name='payment')
    Shipment_id = models.ForeignKey(Shipment,on_delete=models.CASCADE,related_name='shipment')
    
    
    def __str__(self):
        return f"Order #{self.order_id} | User ID: {self.user_id_id} | Total: ₹{self.total_price}"

        
class Order_item(models.Model):
    order_item_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order')
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order')
    
    def __str__(self):
        return f"OrderItem {self.order_item_id} - Product: {self.product_id} (Qty: {self.order_id})"
        

class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart')
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_item')
    
    def __str__(self):
        return f"Cart_id {self.cart_id} - Product: {self.product_id} (User: {self.user_id})"
    
    
class Wishlist(models.Model):
    wishlist_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='wishlist')
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='wishlist_item')
    
    def __str__(self):
        return f"Wishlist {self.wishlist_id} - Product: {self.product_id} (User_id: {self.user_id})"
    


    
        
 