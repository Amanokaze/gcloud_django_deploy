## 참고사항
* 이 소스 파일을 그대로 사용해서 배포한다면 정상적으로 동작하지 않을 것입니다. settings.py를 비롯한 다수의 파일에 개인 정보 및 보안과 관련된 사항은 모두 제거했기 때문입니다. 여러분들께서는 이 곳에 있는 소스코드를 참조해서 개발하는 것은 가능하되, 개인적으로 입력하는 정보(프로젝트명, 버킷명, 계정 정보 등등)에 대해서는 본인의 내용으로 입력해 주시기 바랍니다.
* 세부 메뉴얼은 readme.md 파일에 나타난대로 http://onikaze.tistory.com/647 에 모두 나와있으니 해당 문서를 참고 바랍니다. 이 문서에서는 일체의 스크린샷 등은 제공하지 않습니다.


## 구축 환경
* OS: Ubuntu 18.04 LTS
* Python: 3.7
* Django: 2.2
* MySQL: 5.7


## GAE, Storage가 연동된 Django 애플리케이션 필요 패키지

* APT 
<pre><code>$ sudo apt-get install python3.7-dev lib-mysqlclient-dev
</code></pre>

* VENV 설정 및 가상환경 전용 패키지
<pre><code>$ python3 -m venv venv
(venv)$ pip install --upgrade pip
(venv)$ pip install django==2.2
(venv)$ pip install mysqlclient
(venv)$ pip install django-storages[google]
(venv)$ pip install Pillow
</code></pre>


## settings.py 파일에 사용되는 환경변수

* GS_CREDENTIALS: Google Storage 서비스 계정 인증 파일 위치
  + 여기서 사용되는 service_acount 클래스는 google.oauth2 패키지에 있으므로 반드시 맨 위에 'from google.oauth2 import service_account'를 사용해야 함

* DEFAULT_FILE_STORAGE: Media 파일 저장소, storage_backends.py 파일의 GoogleCloudMediaStorageClass에 명시됨
* STATICFILES_STORAGE: Static 파일 저장소, storage_backends.py 파일의 GoogleCloudStaticStorageClass에 명시됨
* GS_PROJECT_ID: 프로젝트 ID
* GS_MEDIA_BUCKET_NAME / GS_STATIC_BUCKET_NAME: Media/Static 버킷명
* STATIC_URL/MEDIA_URL: Static/Media URL 호출 시 사용될 주소


## Google Cloud에서 사전에 진행해야 할 일

1. 프로젝트 생성

2. 서비스 계정 키 생성
  + '사용자 인증 정보' 메뉴에서 확인 가능
  + 서비스 계정 키는 신규로 생성하고, JSON으로 저장하도록 함
  + JSON 파일은 추후 Storage 배포 시 secret/bucket-admin.json 파일로 대체해서 사용함
  + JSON 파일 내 e-mail 주소는 Storage의 권한 추가에 사용됨
  
3. Compute Engine 생성
  + 생성 시 HTTP, HTTPS 사용 반드시 체크할 것
  + 생성 후 VPC - 방화벽 규칙에서 Port TCP:8000 허용
  + VM 인스턴스에서 Python3.7 버전 사용하도록 설정할 것
  
4. SQL 생성
  + MySQL 5.7 버전 권장
  + 생성 후에는 사용자, 데이터베이스 생성 진행
  + 실제 접속 후 t_images 테이블 생성 진행
    <pre><code>create table t_images (
    id integer primary key auto_increment,
    image varchar2(300) not null,
    creation_date datetime
    );
    </code></pre>
  + 다른 외부 도구를 사용하려면 공개IP 체크 후 아래 '네트워크 입력'에서 주소 입력, 그렇지 않을 경우 Cloud SQL Proxy 이용 권장
  
5. Storage 생성
  + Media/Static 버킷은 이 프로젝트에서는 별도로 구성하도록 설정함
  + 웹 배포가 완료되면 추가로 3개의 버킷이 더 생성된다. 신경쓰지 않아도 된다.
  + 앞서 생성한 서비스 키의 e-mail 주소를 입력 후 권한을 추가한다.
  
  
6. 개발 환경(in VM) 테스트 웹 브라우저 수행 방법
  + python manage.py runserver <내부 IP 주소>:8000
  + 웹 브라우저에서는 <외부 IP 주소>:8000 입력
  + settings.py에서 ALLOWED_HOSTS=["*"] 으로 임시로라도 설정 권장
  
 위 사항에 유의한 후, 소스코드를 참조하여 개발하도록 한다.
