from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='categories/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
