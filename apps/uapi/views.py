import json
from django.db.models import Count, F, Value
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import SessionSerializer
from apps.uapi.models import Questions
from apps.uapi.models import Flashcards
from apps.uapi.models import Sessions




def start_new_test_session(request):
    last_session = Sessions.objects.all()
    for i in last_session:
        last_id = i.id
    
    data = JSONParser().parse(request)
    data['id'] = last_id + 1
    serializer = SessionSerializer(data=data)
    if serializer.is_valid():
        session = serializer.save()

    questions = Questions.objects.filter(systemId__in=serializer.data['divisionIds'])
    questionList = []
    questionIdList = []
    for i in questions:
        question = {}
        question['questionId'] = i.questionId
        question['questionText'] = i.questionText
        question['answerChoiceList'] = i.answerChoiceList
        question['correctAnswer'] = i.correctAnswer
        question['explanationText'] = i.explanationText
        questionList.append(question)
        questionIdList.append(i.questionId)

    data = serializer.data
    data['questionIdList'] = questionIdList
    data['questionList'] = questionList
    session = Sessions(
        timeLimit = data['timeLimit'],
        divisionIds = data['divisionIds'],
        maxQuestionCount = data['maxQuestionCount'],
        questionIdList = data['questionIdList'],
        questionList = data['questionList']
    )
    session.save()
   

    return JsonResponse(data)
   
   