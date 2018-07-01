from django.db import models
from django.urls import reverse

# Create your models here.

class SittingDate(models.Model):
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.date)

class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a/the category/categories this Parliament Record falls under")
    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

class ParliamentRecord(models.Model):
    title = models.CharField(max_length=200)
    sitting_date = models.ForeignKey('SittingDate', on_delete=models.SET_NULL, null=True)
    # ForeignKey used bc 1 record can only have 1 sitting date in frontend but 1 sitting date can have mulitple records
    category = models.ManyToManyField(Category, help_text="Select a/the category/categories for this Parliament Record")
    content = models.TextField()
    class Meta:
        ordering = ['sitting_date', 'title']

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('record-detail', args=[str(self.id)])
    def display_category(self):
        return ','.join([category.name for category in self.category.all()[:3]]) #idk what the [:3] is for but I'll find out later 
    display_category.short_description = 'Category'
    