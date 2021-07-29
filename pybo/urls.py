from django.urls import path
from pybo.views import base_views, question_views, answer_views, comment_views, vote_views

app_name = 'pybo'
# url 별칭 - 네임스페이스다.

urlpatterns = [
    #base_views.py
    #인덱스 메인

    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    #답변등록
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    #질문등록
    path('question/create/', question_views.question_create, name='question_create'),


    #질문수정
    path('question/modify/<int:question_id>/', question_views.question_modify,
         name='question_modify'),
    #질문삭제
    path('question/delete/<int:question_id>/', question_views.question_delete,
         name='question_delete'),
    path('board/', base_views.board, name='board'),
    path('profile/', base_views.profile, name='profile'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify,
            name='answer_modify'),
    path('answer/delete/<int:answer_id>/',answer_views.answer_delete,
         name='answer_delete'),
    #질문추천
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),

    # 답변추천 - 숙제
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),

    #질문댓글등록
    path('comment/create/question/<int:question_id>', comment_views.comment_create_question,
         name='comment_create_question'),
    #질문 댓글 수정
    path('comment/modify/question/<int:comment_id>', comment_views.comment_modify_question,
         name='comment_modify_question'),
    #질문 댓글 삭제
    path('comment/delete/question/<int:comment_id>', comment_views.comment_delete_question,
         name='comment_delete_question'),

    #질문댓글등록
    path('comment/create/answer/<int:answer_id>', comment_views.comment_create_answer,
         name='comment_create_answer'),
    #질문 댓글 수정
    path('comment/modify/answer/<int:comment_id>', comment_views.comment_modify_answer,
         name='comment_modify_answer'),
    #질문 댓글 삭제
    path('comment/delete/answer/<int:comment_id>', comment_views.comment_delete_answer,
         name='comment_delete_answer'),

]