from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login


def signup(request): #회원가입 화면 처리 함수
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user) # 로그인 인증되어 세션권한을 획득
            return redirect('index')
    else: #GET 방식일때
        form = UserForm()
    context = {'form': form}
    return render(request, 'common/signup.html', context)
# Create your views here.
