from django.db import models

class FoodMenu(models.Model):
    CATEGORY_CHOICES = [
        ('drink', 'Drinks'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]

    title = models.CharField(max_length=155)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=6)
    text = models.TextField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='image/foods')
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title} - {self.text[:30]}'