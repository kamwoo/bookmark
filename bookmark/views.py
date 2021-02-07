from django.shortcuts import render

# Create your views here.
# CRUD : create read update delete
# List

# 제네릭 뷰 : 준비되있는, 만들어져있는, 웹사이트를 만들때 제일 많이 사용하는 뷰

# 웹 페이에 접속한다. => 페이지를 본다.
# URL을 입력 => 웹 서버가 뷰를 찾아서 동작시킨다. => 응답

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark
from django.shortcuts import render

class BookmarkListView(ListView):
    model = Bookmark
    # list 뷰를 만들었다. 클래스뷰가 쓰기 간편하다.

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list') # 작업이 수행되고 난 다음 화면
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
