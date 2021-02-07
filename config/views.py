# 뷰 : 기능을 담당한다.
# 화면이 나타나는 뷰 = 로그인 페이지
# 화면이 없는 뷰 = Ajax로 콜하는 뷰
# 화면이 있건 없건 URL은 있어야 한다.

# 뷰 내용(함수, 클래스), URL이 있으면 동작한다.

# 뷰의 코드 형식 : 함수형, 클래스형
# 함수형 : request를 매개변수로 받고(추가 매개변수 가능), 모양은 함수,
#           내가 원하는대로 동작들을 설계하고 만들고 싶을 때
# 클래스형 : CRUD 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고
#           상속 받아서 사용한다.
#           장고의 제네릭 뷰를 많이 사용한다.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # request는 사용자가 요청한 내용들이 들어있다. 세션, 쿠키들이 들어있다.
    # 어떤 계산이나 데이터 베이스 조회, 수정, 등록
    # 응답 메세지를 만들어서 반환
    html = "<html><body>hello world</body></html>"
    # 나중에는 html변수를 대신해서 템플릿 사용
    return HttpResponse(html)


def welcome(request):
    html = "<html><body>welcome to django</body></html>"
    return HttpResponse(html)


def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 template 폴더
    # 3. 개인이 설정한 폴더
    # 파일이 추가되면 서버를 껏다가 켜준다.
    return render(request, 'test.html')


def kakao_template(request):
    return render(request, 'kakao.html')
