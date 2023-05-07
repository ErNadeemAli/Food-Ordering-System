from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    create_date=models.DateField(auto_created=True)
    update_date=models.DateField(auto_created=True)

    class Meta:
        abstract=True


class Product(BaseModel):
    product_name=models.CharField(max_length=100)
    product_desc=models.TextField()
    product_price=models.IntegerField(default=0, max_length=100)
    
    
class ProductImages(BaseModel):
    product_image=models.ImageField()