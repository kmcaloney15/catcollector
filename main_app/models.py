from django.db import models
from django.urls import reverse

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

    # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})



# Add new Feeding model below Cat model
class Feeding(models.Model):   
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )

    # Create a cat_id FK
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    # As you can see, the ForeignKey field-type is used to create a one-to-many relationship. The first argument provides the parent Model.

    # In a one-to-many relationship, the on_delete=models.CASCADE is required. It ensures that if a Cat record is deleted, all of the child Feedings will be deleted automatically as well - thus avoiding orphan records (seriously, that's what they're called).



    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        # so we know what meal we are having on what date
        return f"{self.get_meal_display()} on {self.date}"
        # Check out the convenient get_meal_display() method Django automagically creates to access the human-friendly value of a Field.choice like we have on meal.




