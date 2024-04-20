from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category_name



class Manufacturer(models.Model):
    mfg_name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.mfg_name

class Brand(models.Model):
    brand_name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.brand_name

class Product(models.Model):
    product_id=models.CharField(max_length=10)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, null=True)
    sku = models.CharField(max_length=20, null=True)
    unit = models.IntegerField()
    length = models.DecimalField(max_digits=10, decimal_places=3)
    breadth = models.DecimalField(max_digits=10, decimal_places=3)
    height = models.DecimalField(max_digits=10, decimal_places=3)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    upc = models.CharField(max_length=12, null=True)
    ean = models.CharField(max_length=13, null=True)
    mpn = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=250, null=True)
    image = models.ImageField(null=True)
    cost_price = models.DecimalField(max_digits=10,decimal_places=2)
    selling_price = models.DecimalField(max_digits=10,decimal_places=2)
    is_available = models.BooleanField()
    # date_added = models.DateField(default=datetime.today)

    def __str__(self):
        return self.product_id

class Customer(models.Model):
    customer_id=models.CharField(max_length=10)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    email = models.EmailField()
    gst_num = models.CharField(max_length=15, null=True)
    phone_num = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)
    pincode = models.CharField(max_length=6, null=True)
    username = models.CharField(max_length=15, null=True)
    password = models.CharField(max_length=20, null=True)
    aadhar_num=models.IntegerField()
    pan_num=models.CharField(max_length=12)

    def __str__(self):
        return self.customer_id

class Warehouse(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    STATUS_CHOICES = [
    ('available', 'Available'),
    ('out_of_stock', 'Out of Stock'),
    ('on_hold', 'On Hold'),
    ]

    stock_num = models.IntegerField()
    stock_status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='available')
    min_stock = models.IntegerField()

class PurchaseOrder(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.now)
    shipping_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

class PurchaseItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

class Department(models.Model):
    department_name = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.department_name

class Employees(models.Model):
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=15)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.TextField()
    phone_num = models.IntegerField()
