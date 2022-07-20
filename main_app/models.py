from django.db import models

# A tuple of 2-tuples
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)
# can now use with cat model and feeding model, since it lives above the models


# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # new code below
    def __str__(self):
        return self.name


# Add new Feeding model below Cat model
class Feeding(models.Model):   
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )

