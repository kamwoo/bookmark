from django.db import models
from django.urls import reverse
# model안에서는 reverse를 쓰고 class형 view안에서 필드값으로 쓸때는 reverselazy를 써야한다.
# 라오틴 테이블이 다 불러지지 않은 상태에서 클래스뷰가 먼저 점검이되기때문에 오류가 발생할 수 있다.

# Create your models here.
# 모델 : 데이터베이스를 SQL없이 다루려고 사용
# 우리가 데이터를 객체화해서 다루겠다.
# 모델 = 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드(엑셀에서 행)
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100) # 필드
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사향(몇글자인지)
    # 3. Form의 종류
    # 4. Form에서 제약 사항

    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])


# 모델을 만들었다. => 데이터베이스를 어떤 데이터들을 어떤 형태로 넣을지 결정
# 마이그레이션 => 데이터베이스에 모델의 내용을 반영(테이블 생성)
# makemigrations => 모델의 변경사항을 추적해서 기록 , 모델이 어떻게 변할지 모르기
# 때문에 데이터 베이스에 바로 기록을 하지않고 마이그레이션을 할 정보를 만들고 마이그레이션을 한다.
# 모델을 수정하고 마이그레이션을 해주어야 한다.
