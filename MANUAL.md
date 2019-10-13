## Announcement
* If you use this source code without any change, your program is not executed, because some files contains personal information, so I removed related information. 
* this manual doesn't provide any screenshot, so If you want some screenshots and detailed information then go http://onikaze.tistory.com/647 .


## Environment
* OS: Ubuntu 18.04 LTS
* Python: 3.7
* Django: 2.2
* MySQL: 5.7


## Packages to implement this code

* APT 
<pre><code>$ sudo apt-get install python3.7-dev lib-mysqlclient-dev
</code></pre>

* VENV and PIP
<pre><code>$ python3 -m venv venv
(venv)$ pip install --upgrade pip
(venv)$ pip install django==2.2
(venv)$ pip install mysqlclient
(venv)$ pip install django-storages[google]
(venv)$ pip install Pillow
</code></pre>


## Environment variables in settings.py

* GS_CREDENTIALS: Google Storage Service Account Information
  + To use this variable, you must add 'from google.oauth2 import service_account'.

* DEFAULT_FILE_STORAGE: Media Storage, declared GoogleCloudMediaStorageClass in storage_backends.py
* STATICFILES_STORAGE: Static Storage, decalred GoogleCloudStaticStorageClass in storage_backends.py
* GS_PROJECT_ID: Project ID
* GS_MEDIA_BUCKET_NAME / GS_STATIC_BUCKET_NAME: Media/Static Bucket name
* STATIC_URL/MEDIA_URL: Static/Media URL Addresses


## Preparation in Google Cloud

1. Create a project

2. Create a Service Account Key
  + Menu: API & Services - Credential
  + Select a New service account key and you select a JSON key type.
  + the JSON file will be used to connect a Google Storage and it's file name will be changed to 'secret/bucket-admin.json'.
  + an e-mail address in the JSON file will be used to add a bucket permision in the storage.
  
3. Create a VM Machin in Compute Engine
  + Please check HTTP, HTTPS checkbox.
  + After creation, allow TCP:8000 in the Firewall Rules.
  + Have to set a python version 3.7 in VM instance.
  
4. Create a SQL
  + Recommend MySQL 5.7 version
  + After creation, also create user and database
  + After connecting, create a table, 't_images'
    <pre><code>create table t_images (
    id integer primary key auto_increment,
    image varchar2(300) not null,
    creation_date datetime
    );
    </code></pre>
  + If you want to use other external tools, check public IP address and input an 'Add Network', otherwise recommend using Cloud SQL Proxy
  
5. Create a Storage
  + Media/Static buckets are separeted in thie project
  + After deploying app engine, automatically three buckets but it is not important.
  + Add a bucket permission. the permission's member is an e-mail address of created service account key.
  
  
6. a test of the django development environment(in VM) and to execute in the web browser
  + python manage.py runserver <Internal IP address>:8000
  + input <External IP address>:8000 in the web browser
  + set a ALLOWED_HOSTS=["*"] in settings.py temporarily
  
Thank you for your concerns.
