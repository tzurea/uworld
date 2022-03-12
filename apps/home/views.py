# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import random
import json
from django import template
import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import *


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def topics(request):
    topic_link = 'http://192.168.1.100:8000/api/topic-ids/'
    question_link = 'http://192.168.1.100:8000/api/create-session/'
    if request.method == 'POST':
        form = SessionForm(request.POST)
        #print(form)
        qn_request = request.POST.dict()
        qn_request['topicIds'] = request.POST.getlist('topicIds')
        print(qn_request)
        question_response = requests.post(question_link, data=json.dumps(qn_request))
        question_response = json.loads(question_response.text)
        
        questionList = question_response['questionList']
        random.shuffle(questionList)
        question_display_list = []
        maxQuestionCount = question_response['maxQuestionCount']
        count = 0
        for i in questionList:
            if count >= int(maxQuestionCount):
                break
            i['questionIndex'] =  count
            count = count + 1
            question_display_list.append(i)
            
        return render(request, 'home/question-drill.html',{'questions': question_display_list})
    
    response = requests.get(topic_link).text
    response = json.loads(response)
    return render(request, 'home/test-drill.html',{'topics': response})




    