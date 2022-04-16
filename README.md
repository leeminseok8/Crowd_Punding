# 프로젝트 개요

- 본 서비스는 크라우드 펀딩 기능을 제공합니다. 게시자는 크라우드 펀딩을 받기위한 상품(=게시물)을 등록합니다.

- 유저는 해당 게시물의 펀딩하기 버튼을 클릭하여 해당 상품 ‘1회펀딩금액’ 만큼 펀딩합니다.

# 사용 Stack 및 Tools

- Python 3.10
- Django 4.0
- MySQL
- dbdiagram

# 설치 방법

1. 해당 프로젝트를 clone 하고, 프로젝트 폴더로 들어간다.<br>

	>``` git clone https://github.com/leeminseok8/wanted_pre_onboarding.git```<br>

    >``` cd wanted_pre_onboarding```<br>

2. 가상 환경 생성 및 실행
	>``` conda create -n 프로젝트명 python=3.10```<br>

	>``` conda activate 프로젝트명```

3. Python 패키지 설치
	>``` pip install -r requirements.txt```

4. DB 생성 후 model의 변경사항을 DB에 반영한다.
	>``` python manage.py makemigrations```<br>

	>``` python manage.py migrate```<br>

5. 서버를 실행한다.
	>``` python manage.py runserver 0.0.0.0:8000```

<br>

# 모델링

> ![wanted_pre_onboarding (1)](https://user-images.githubusercontent.com/93478318/163388301-e77224a3-3ea5-4e8e-8e09-8a61156a0a85.png)

<br>

# 구현 기능
- 상품 등록
- 상품 수정
- 상품 삭제
- 상품 목록(검색, 정렬)
- 상품 상세 페이지

## 구현 과정
- 크라우드 펀딩 모델링을 작성하기 위해 기존에 서비스를 제공하고 있는 홈페이지를 참고했습니다. 모델링 작성 후 View에서 실제 API를 작성 중 모델링을 수정하며 진행했습니다. 마지막으로, test 코드를 작성하면서 실제 데이터를 받을 때 발생할 수 있는 문제들과 프론트와 소통할 때 필요한 실제 데이터를 생각하며 최종 API를 수정했습니다.

- REST API를 구현하기 위해 클래스명, URL을 명사형으로 작성했습니다.

- CASCADE를 사용하여 의미없이 남게 되는 독립적인 데이터를 삭제했습니다.

# DB 설치
>``` pip install mysqlclient ```<br>

> ``` (M1을 사용하시는 분들은 pip install PyMySQL)```<br>

> ``` (중요) mysql 설치되어 있는지 먼저 확인해주세요 ```<br>


# DB 재구축
> 덤프 파일명 : wanted_pre_onboarding.sql (root directory에 있습니다.)<br>

> MySQL 접속 후 ``` CREATE DATABASE 데이터베이스명 character set utf8mb4 collate utf8mb4_general_ci; ``` 를 입력하여 DB 생성<br>

> CLI(terminal)환경에서 ``` mysql -u root -p 데이터베이스명 < wanted_pre_onboarding.sql ```
