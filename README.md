# gcloud_django_deploy
Django simple application using GAE(Google App Engine) and Cloud Storage


## Introduction and reference
This django application is a very simple multiple file attachment system. The application can be deployed GAE(Google App Engine) and the app's media and static files are saved in the bucket of the Google Cloud Storage. 

For this project, I found some documents but they aren't satisfied by myself. The first document, 'Django on App Engine standard environment', shows how to install MySQL and django application but it doesn't show how to manage media and static files. The second document, 'Google Cloud Storage', shows how to connect Google Cloud Storage but it doesn't show how to deploy GAE because the document is provided by the django-storage official site. The third document, 'Preparing your Django Application for Google Cloud Run', shows how to construct and deploy django application and also connect with Cloud Storage, but it uses docker. I think that using docker is so difficult and I want to deploy using GAE's deployment manual. Finally, I tried to connect the three documents and I completed my project and share the source code.

The documents are below:
* Django on App Engine standard environment (GAE official) - https://cloud.google.com/python/django/appengine
* Google Cloud Storage (django-storage official) - https://django-storages.readthedocs.io/en/latest/backends/gcloud.html
* Preparing your Django Application for Google Cloud Run (Tariq Al-Sadoon Blog): https://medium.com/swlh/preparing-your-django-application-for-google-cloud-run-7c8cb7b7464b

Thanks to the references.


## Detail Specific Document
In this document, I introduce very simple procedure. If you want to see a detail document, please visit below.

http://onikaze.tistory.com/647

In this site, you can see the document. It is written in Korean so if you are not Korean you have in difficulty apprciating. However, the document is provided with many images and contained source codes. If you need a help, please contact me through this github or to send a email, oniamano@gmail.com .
