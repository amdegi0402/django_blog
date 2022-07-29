from django.contrib import admin
from .models import SampleModel, BlogModel, ReviewModel

admin.site.register(SampleModel)
admin.site.register(BlogModel)
admin.site.register(ReviewModel)
