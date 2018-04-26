from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import json
from rest_framework.decorators import api_view
def bubblesort(request):
    lst=request.GET['listofno']
    a=lst.split(",")
    print (a)
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    template=[]
    for x in a:
        template.append(x)
    return HttpResponse(json.dumps(template), content_type='application/json')