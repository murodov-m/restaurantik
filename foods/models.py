from django.db import models

class Food(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)
    photo = models.ImageField()
    price = models.FloatField()
    favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.title

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
