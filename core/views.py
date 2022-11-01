from django.shortcuts import render, HttpResponse
from django.db.models import Q
from rest_framework.views import APIView


class GlobalSearchView(APIView):
    def get(self, request, *args, **kwargs):
        word = kwargs[""]
        return HttpResponse('test')
