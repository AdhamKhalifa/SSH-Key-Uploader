from __future__ import unicode_literals
# pages/views.py
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

#new
from django.shortcuts import render,redirect
from .models import TodoList, Category

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect

import datetime

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): # new
    template_name = 'about.html'

class LoginPageView(TemplateView): # new
    template_name = 'login.html'

class SignupPageView(TemplateView): # newLoginFormView
    template_name = 'signup.html'

def index(request): #the index view
	todos = TodoList.objects.all() #quering all todos with the object manager
	categories = Category.objects.all() #getting all categories with object manager
	if request.method == "POST": #checking if the request method is a POST
		if "taskAdd" in request.POST: #checking if there is a request to add a todo
			title = request.POST["description"] #title
			key = request.POST["key"] #title
			#date = str(request.POST["date"]) #date
			#category = request.POST["category_select"] #category
			content = title + " -- " + " " + key #+ category #content
			Todo = TodoList(title=title, key=key, content=content,) # category=Category.objects.get(name=category)
			Todo.save() #saving the todo 
			return redirect("/%5E$") #reloading the page
		
		if "taskDelete" in request.GET: #checking if there is a request to delete a todo
	
			checkedlist = request.GET["checkedbox"] #checked todos to be deleted
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
				todo.delete() #deleting todo
	return render(request, "home.html", {"todos": todos, "categories":categories})