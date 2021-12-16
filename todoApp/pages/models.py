
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
#new
from django.utils import timezone

class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100) #Like a varchar
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name #name to be printed when called
    def get_absoulte_url(self):
        return f"categories/"
                
class TodoList(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar for title
    key = models.CharField(max_length=500) # a varchar for key
    content = models.TextField(blank=True) # a text field for content 
    completed = models.BooleanField(default=False) #Is it completed or not?
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    #category = models.ForeignKey(Category, on_delete=models.CASCADE) # a foreignkey
    class Meta:
        ordering = ["-created"] #ordering by the created field
    def __str__(self):
        return self.title #name to be printed when called
