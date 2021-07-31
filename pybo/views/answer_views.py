from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from pybo.forms import AnswerForm
from pybo.models import Question, Answer


@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user #추가한 속성 author 적용
            answer.question = question
            from django.utils import timezone
            answer.create_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question':question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
    #답변 등록은 리턴 render가 아니고 리다렉트로 해줘야 한다.

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    #답변 수정
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        from django.contrib import messages
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', question_id=answer.id)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            from django.utils import timezone
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'form': form}
    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
#질문 삭제 버튼 클릭 처리
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        from django.contrib import messages
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    #return redirect('pybo:board')
    return redirect('pybo:detail', question_id = answer.question.id)