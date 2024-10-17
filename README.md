# nomad-pyteam-backend

## Roles of modules

### pyteam_backend
- 프로젝트 셋팅 모듈

### service_api
- 기본 api 및 비즈니스 로직 모듈

### data_auth
- 인증 모델 및 어드민 모듈

## Guide of set-up

### commands

```shell
python manage.py makemigrations  # 마이그레이션 파일 생성
python manage.py migrate  # 전체 마이그레이션 파일 반영
python manage.py createsuperuser  # 슈퍼유저 생성

# only local info
username: admin
email : admin@test.com
password: 1q2w3e4r
```
