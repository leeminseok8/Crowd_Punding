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

> ![wanted_pre_onboarding (2)](https://user-images.githubusercontent.com/93478318/163719742-c3be3e7b-08dd-437c-ae7f-3271bef23d8a.png)

<br>

# 구현 기능
- 상품 등록
- 상품 수정
- 상품 삭제
- 상품 목록(검색, 정렬)
- 상품 상세 페이지

## 구현 과정
- 크라우드 펀딩 모델링을 작성하기 위해 기존에 서비스를 제공하고 있는 홈페이지를 참고했습니다. 모델링 작성 후 View에서 실제 API를 작성 중 모델링을 수정하며 진행했습니다. 마지막으로, test 코드를 작성하면서 실제 데이터를 받을 때 발생할 수 있는 문제들과 프론트와 소통할 때 필요한 실제 데이터를 생각하며 user와 product의 fk를 추가하며 API를 수정했습니다.

## 고민했던 부분
- REST API를 구현하기 위해 클래스명, URL을 명사형으로 작성했습니다. update와 delete는 RESTFUL하기 위해서 동사형을 최대한 베재하고 작성해야 하는데 url상에서 겹칠 수 밖에 없었습니다. 그래서 두 가지 method를 하나의 클래스로 병합하여 request의 method에 따라 다른 API를 호출하도록 작성했습니다. 또한 클래스명이 method를 포괄하거나 직관적인 단어를 사용하도록 고민했습니다.

- 모델링에서 CASCADE와 SET NULL중에 무엇이 데이터 측면에서 의미있을까에 대한 고민을 했습니다. 현재는 펀딩 기능이 온전하게 구현되지 않아서 CASCADE를 사용했지만, 유저의 관심 분야나 상품의 카테고리 통계에 이용할 수 있도록 상품과 유저간에는 SET NULL을 사용하는 것이 의미있다고 생각합니다. 

## 아쉬운 점
- 혼자 repository를 관리하던 좋지 않은 습관으로 인해 Modeling하는 과정에서 git관리가 너무 지저분하게 되었습니다. 마지막 merge하기 전에 rebase를 통해 git commit 이력 관리를 했어야 하는데 뒤늦게 commit 이력을 보며 깨달았습니다. 이미 merge가 된 상태라 view를 작성하면서는 최대한 관리를 했습니다. 당연한 말이지만, 앞으로 commit과 push는 하나하나 신중하게 해야겠다고 생각했습니다.

- DRF로 decorator를 구현하지 못한 아쉬움이 있습니다. 그래서 User App이 단순 펀딩 기능만 구현되고 인증 인가를 구현하지 못한 부분이 아쉽습니다. 온보딩의 결과와 관계없이 빠른 시일 내에 공부하고 추가할 예정입니다.

# DB 설치
>``` pip install mysqlclient ```<br>

> ``` (M1을 사용하시는 분들은 pip install PyMySQL)```<br>

> ``` (중요) mysql 설치되어 있는지 먼저 확인해주세요 ```<br>


# DB 재구축
> 덤프 파일명 : wanted_pre_onboarding.sql (root directory에 있습니다.)<br>

> MySQL 접속 후 ``` CREATE DATABASE 데이터베이스명 character set utf8mb4 collate utf8mb4_general_ci; ``` 를 입력하여 DB 생성<br>

> CLI(terminal)환경에서 ``` mysql -u root -p 데이터베이스명 < wanted_pre_onboarding.sql ```
