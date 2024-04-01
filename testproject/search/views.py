from django.views.generic import ListView
from .models import News, Comment
import requests
import datetime
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404,redirect
from django.contrib.auth import logout
from .forms import InquiryForm


def logout_view(request):
    logout(request)
    return redirect('index')

def contact_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'search/index.html', {'form': form})

def create_comment(request):
    if request.method == 'POST':
        content = request.POST.get('message-input', '')
        Comment.objects.create(
            content=content
        )
        comments = Comment.objects.all()
        return render(request, 'search/index.html', {'comments': comments})
    
@require_POST  #利用中
def deletecomment(request,pk):
    comment = get_object_or_404(Comment,id=pk)
    comment.delete()
    print(request.user.id)

    return redirect(request.META.get('search/index.html', '/'))

class ListNewsView(ListView):
    template_name = 'search/index.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #api_url = 'http://localhost:3000/dummy/dummy.json'
        api_url = 'https://newsapi.org/v2/top-headlines?country=jp&category=business&apiKey=42e7f97b2a2c4889a763ffedb7f8bde2'

        # APIエンドポイントにGETリクエストを送信
        response = requests.get(f'{api_url}')

        # HTTPステータスが200 OKであることを確認
        if response.status_code == 200:
            # JSONデータを取得して解析
            data = response.json()
            titles = [article["title"] for article in data["articles"]]
            titles = titles[0:20]
            context['comments'] = Comment.objects.all()
            # レスポンスデータをextra_contextに追加
            context['extra_context'] = {'news_titles': titles}
            context['date'] = datetime.datetime.now().strftime('%Y/%m/%d')
        else:
            # エラーメッセージをコンソールに表示
            print(f'HTTP error! Status: {response.status_code}')

        return context

class ListcompanyView(ListView):
    template_name = 'search/company.html'
    model = News

class ListindexView(ListView):
    model = News
    template_name = 'search/index.html'
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #api_url = 'http://localhost:3000/dummy/dummy.json'
        api_url = 'https://newsapi.org/v2/top-headlines?country=jp&category=business&apiKey=42e7f97b2a2c4889a763ffedb7f8bde2'

        # APIエンドポイントにGETリクエストを送信
        response = requests.get(f'{api_url}')

        # HTTPステータスが200 OKであることを確認
        if response.status_code == 200:
            # JSONデータを取得して解析
            data = response.json()
            titles = [article["title"] for article in data["articles"]]
            titles = titles[0:20]
            # レスポンスデータをextra_contextに追加
            context['extra_context'] = {'news_titles': titles}
            context['date'] = datetime.datetime.now().strftime('%Y/%m/%d')
        else:
            # エラーメッセージをコンソールに表示
            print(f'HTTP error! Status: {response.status_code}')

        return context

class ListfaqView(ListView):
    template_name = 'search/faq.html'
    model = News

class ListcontactView(ListView):
    template_name = 'search/contact.html'
    model = News

class ListserviceView(ListView):
    template_name = 'search/service.html'
    model = News

class Listservice2View(ListView):
    template_name = 'search/service2.html'
    model = News

