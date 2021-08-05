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


Push to git remote by opening a repo with the same aname and following the instruction on the first welcome page 


(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git remote add origin https://github.com/Odogwo/blogocoders.git

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git branch -M main

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git push -u origin main

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git pull

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git remote -v

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git remote add upstream https://github.com/Odogwo/blogocoders.git

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git remote -v

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git fetch upstream

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git checkout main

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git merge upstream/main


(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git add *

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git commit -m "README: added how to sync upstream with local files"

(env) C:\Users\USER\Desktop\sites\blogocoders\env\mysite>git push origin --all















