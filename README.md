This program was a tutorial from 
https://www.ordinarycoders.com/blog/article/django-beginners-guide

C:\Users\USER>cd Desktop

C:\Users\USER\Desktop>mkdir sites

C:\Users\USER\Desktop>cd sites

C:\Users\USER\Desktop\sites>mkdir blogocoders

C:\Users\USER\Desktop\sites>cd blogocoders

C:\Users\USER\Desktop\sites\blogocoders>py -m venv env

C:\Users\USER\Desktop\sites\blogocoders>cd env

C:\Users\USER\Desktop\sites\blogocoders\env>Scripts\activate

(env) C:\Users\USER\Desktop\sites\blogocoders\env>pip install --upgrade pip

(env) C:\Users\USER\Desktop\sites\blogocoders\env>pip install django==2.1.15

(env) C:\Users\USER\Desktop\sites\blogocoders\env>django-admin startproject mysite

(env) C:\Users\USER\Desktop\sites\blogocoders\env>cd mysite

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>py manage.py startapp main

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>py manage.py runserver

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>py manage.py migrate

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>py manage.py makemigrations

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>py manage.py migrate

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>py manage.py createsuperuser

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>pip install django-crispy-forms

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>pip install python-decouple

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>py manage.py runserver

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>pip freeze > requirements.txt

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git init


(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git add *



(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git commit -m "blogcoders book: first commit , complete from the site"



You can create a local directory, let's call it local-git-repo.git

mkdir local-git-repo.git
Then in it we can execute

git init --bare
Then in your actual projcet you can do the following

git add remote origin <path to your git repo>

