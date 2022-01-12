from django.http import request
from django.shortcuts import render
from django.contrib.auth.views import LogoutView

class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'top.html'

# def test(request):
#     return render(request, 'test/test.html')
