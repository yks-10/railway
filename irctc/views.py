from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework import status
from .seralizers import *
from django.db import IntegrityError
from . models import *
# Create your views here.


class TrainList(APIView):
    def get(self,request):
        train=Train.objects.all()
        serializer=TrainSerializer(train, many=True)
        return Response(serializer.data)

class TicketList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'irctc/index.html'

    def get(self, request):
        serializer = TicketSerializer()
        return Response({'serializer': serializer})

    '''def get(self,request,pk):
        ticket=get_object_or_404(Ticket,pk=pk)
        serializer=TicketSerializer(Ticket)
        return Response({'serializer':serializer,'ticket':ticket})'''
    
    def post(self,request):
        #ticket=get_object_or_404(Ticket)
        serializer=TicketSerializer(data=request.data)
        if not serializer.is_valid():
            #return Response({'serializer':serializer,'ticket':ticket})
            serializer.save()
        return redirect('TrainList')


class LoginList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'irctc/login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self,request):
        try:
            user = User.objects.create_user(request.POST['email'], password=request.POST['password'])
            user.save()
            login(request, user)
            return redirect('ticket')
        except IntegrityError:
            return redirect('login')