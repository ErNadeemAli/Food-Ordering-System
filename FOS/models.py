from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model): # we create base model because we need to use this property other classes.
    uid=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    create_date=models.DateField(auto_created=True)
    update_date=models.DateField(auto_created=True)

    class Meta:
        abstract=True # this means this class trite as class not models


class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    product_desc=models.TextField()
    product_price=models.IntegerField(default=0)
    product_demo_price=models.IntegerField(default=0)
    

class ProductMetaInformation(BaseModel):
    product=models.OneToOneField(Product, on_delete=models.CASCADE)
    product_measuring = models.CharField(null=True, blank=True, max_length=100, choices=(('kg','kg'),('ml','ml'),('mg','mg'),('g','g'),(None,None)))
    quantity=models.CharField(null=True, blank=True, max_length=100)
  
class ProductImages(BaseModel):
    product_image=models.ImageField(upload_to='product')