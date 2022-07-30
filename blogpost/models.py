from django.db import models
from django.contrib.auth.models import User

EVALUATION_CHOICES = [('良い', '良い'), ('悪い', '悪い')]
class ReviewModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='')
    useful_review = models.IntegerField(null=True, blank=True, default=0)
    useful_review_record = models.TextField()
    evaluation = models.CharField(max_length=10, choices=EVALUATION_CHOICES)


'''
EVALUATION_CHOICES = [('good', 'good'),('bad', 'bad')]
class ReviewModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

CATEGORY = (('buisiness', 'ビジネス'),('life', '生活'), ('other', 'その他'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
    #admin/ タイトル表示
    def __str__(self):
        return self.title
'''

