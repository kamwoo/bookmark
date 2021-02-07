from django.urls import path
from .views import *

urlpatterns = [
    # 2차 url
    path("", BookmarkListView.as_view(), name='list'),
    # as_view()는 클래스 뷰를 함수형 뷰로 바꿔준다.
    # name은 화면을 보여줄 템플릿에서 url을 이렇게 불러서 쓸거라는 정하는 이름
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
                # 글번호, PK = 프라이머리 키 ,슬러스, 인트, 스트링등으로 사용한다.
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]