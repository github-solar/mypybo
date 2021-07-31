from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404
from pybo.models import Question

def index(request):
    return render(request, 'pybo/index.html')

def profile(request):
    return render(request, 'pybo/profile.html')

def board(request): #교재에서는 index 함수로 했다. 주의!
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    # 127.0.0.1:8000/pybo/?page=1 과 같은 의미 이것은 교재내용과 다르게 구현된다.
    if so == 'recommend':
        question_list = Question.objects.annotate( #num_voter 는 임시필드다.
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = Question.objects.order_by('-create_date')

    # 아래는 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |   #제목검색
            Q(content__icontains=kw) |  #내용검색
            Q(author__username__icontains=kw) |  #질문자 검색
            Q(answer__author__username__icontains=kw) |  #답변자 검색
            Q(answer__content__icontains=kw)  #내용검색
        ).distinct() # 중복제외하고 검색하라.

    #-내림차순으로 정렬
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)
    #return HttpResponse("pybo 환영합니다.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)