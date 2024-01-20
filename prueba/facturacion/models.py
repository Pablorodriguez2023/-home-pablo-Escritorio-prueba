from django.db import models



# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.document} - {self.first_name} - {self.last_name} - {self.email}"
       
    
class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    nit = models.CharField(max_length=20)
    code = models.CharField(max_length=50) 
           
    def __str__(self):
        return f"{self.client_id} - {self.company_name} - {self.code} - {self.nit}"      

    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    attribute = models.CharField(max_length=100) 
    
    def __str__(self):
        return f"{self.name} - {self.description} - {self.attribute} "
    
    
class BillProduct(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey('Bill', on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)  
    
    def __str__(self):
        return f"{self.bill_id} - {self.product_id}"
    
