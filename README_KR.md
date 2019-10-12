# gcloud_django_deploy_sample
GAE(Google App Engine) and Cloud Storage를 사용한 Django 애플리케이션

## 개요 및 참조
이 애플리케이션은 매우 간단한 다중 파일 첨부 시스템입니다. 이 애플리케이션은 GAE(Google App Engine)에 배포되고, media/static 파일은 Google Cloud Storage의 버킷(Bucket)에 저장됩니다.
이 기능을 구현하기 위해서 몇 개의 주요 문서를 찾았지만, 만족할 만한 수준은 아니였습니다. 첫 번째 'App Engine 표준 환경에서 Django 실행' 문서에서는 Cloud 환경에서 MySQL을 설치하고 Django 애플리케이션을 어떻게 구축하는 지에 대해서 나타냈습니다. 하지만 Static/Media 파일을 어떻게 다루는 지에 대해서는 나타나 있지 못했습니다. 두 번째 'Google Cloud Storage' 문서에서는 Google Cloud Storage에 어떻게 연동하는 지를 나타냈지만 GAE에 어떻게 배포하는 지는 나타나 있지 않았습니다. 사실 이 문서는 django-storage 공식 사이트에서 제공하는 문서라는 점에서 GAE에 배포하는 방법을 설명할 이유는 없었습니다. 세 번째 'Preparing your Django Application for Google Cloud Run' 문서에서는 Django 애플리케이션을 어떻게 구축하고 배포하는지, 그리고 Cloud Storage에 어떻게 연동하는 지 자세히 나와 있습니다. 하지만 이 문서에서는 docker를 사용해서 연동하였고, 적어도 제가 생각하기에 docker를 사용한 연동방법은 어렵다고 판단하였고 가능하면 GAE에서 제공하는 공식 메뉴얼에 따른 배포를 하기를 원했습니다. 이에 따라 결국 세 문서를 합친 Django 애플리케이션 배포 및 스토리지 연결 방법을 고안하였고 완성된 방법을 가지고 이 곳에 배포하고 알리고자 합니다.

언급된 3개의 문서는 다음과 같습니다.
* App Engine 표준 환경에서 Django 실행 (GAE official) - https://cloud.google.com/python/django/appengine
* Google Cloud Storage (django-storage official) - https://django-storages.readthedocs.io/en/latest/backends/gcloud.html
* Preparing your Django Application for Google Cloud Run (Tariq Al-Sadoon Blog): https://medium.com/swlh/preparing-your-django-application-for-google-cloud-run-7c8cb7b7464b


이러한 문서를 제공해주신 분들께 다시 감사를 표하며, 구축하는 데 많은 도움을 받았습니다.


## 세부 구축 방법 문서
이 문서에서는 매우 간단한 절차만 나타낼 예정입니다. 세부 구축 방법을 보기 원하시면 다음 문서를 참조해주시기 바랍니다.

http://onikaze.tistory.com/647

위 사이트로 가시면 세부 절차가 나타난 문서를 볼 수 있으며, 한국어로 제작된 문서라는 점에서 우리나라 사람이라면 이해하는 데 어려움은 없을 것입니다. 만약 도움이 필요할 경우, 이 곳 github에 글을 남겨주시거나, oniamano@gmail.com 로 문의 바랍니다.
