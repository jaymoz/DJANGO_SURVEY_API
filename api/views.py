from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK,HTTP_204_NO_CONTENT
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .serializers import SurveyQuestionsSerializer,ResponseQuestionSerializer,SurveySerializer,ChoiceSerializer
from .models import Survey, SurveyQuestions, UserResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, BasePermission, SAFE_METHODS
from rest_framework import generics
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['GET'])
def urlview(request):
    return Response("API for a user survey system")

@api_view(['POST'])
@permission_classes((IsAdminUser,))
def CreateSurvey(request):
    serializer = SurveySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def SurveyList(request):
    surveys = Survey.objects.all()
    serializer = SurveySerializer(surveys, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def SurveyDetail(request, pk):
    survey = get_object_or_404(Survey, id=pk)
    serializer = SurveySerializer(survey)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((IsAdminUser,))
def UpdateSurvey(request, pk):
    survey = get_object_or_404(Survey, id=pk)
    serializer = SurveySerializer(instance=survey, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
def DeleteSurvey(request, pk):
    survey = get_object_or_404(Survey, id=pk)
    survey.delete()
    return Response("Survey has been deleted", status=HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes((IsAdminUser,))
def CreateQuestion(request):
    serializer = SurveyQuestionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def QuestionList(request):
    questions = SurveyQuestions.objects.all()
    serializer = SurveyQuestionsSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def QuestionDetail(request, pk):
    question = get_object_or_404(SurveyQuestions,id=pk)
    serializer = SurveyQuestionsSerializer(question)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((IsAdminUser,))
def UpdateQuestion(request, pk):
    question = get_object_or_404(SurveyQuestions,id=pk)
    serializer = SurveyQuestionsSerializer(instance=question, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
def DeleteQuestion(request, pk):
    question = get_object_or_404(SurveyQuestions, id=pk)
    question.delete()
    return Response("This question has been deleted", status=HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def CreateResponse(request):
    serializer = ResponseQuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def UpdateResponse(request, pk):
    response = get_object_or_404(UserResponse,id=pk)
    serializer = SurveyQuestionsSerializer(instance=response, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def ResponseDetail(request, pk):
    response = get_object_or_404(UserResponse,id=pk)
    serializer = SurveyQuestionsSerializer(response)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def GetUserResponse(request, id_user):
    try:
        user_response = UserResponse.objects.filter(user_id=id_user)
        serializer = ResponseQuestionSerializer(user_response, many=True)
        return Response(serializer.data)
    except Exception:
        return Response("Response not found")

@api_view(['DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def DeleteResponse(request, pk):
    response = get_object_or_404(UserResponse, id=pk)
    response.delete()
    return Response("Response has been deleted", status=HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def ActiveSurveys(request):
    survey = Survey.objects.filter(end_date__gte=timezone.now()).filter(start_date__lte=timezone.now())
    serializer = SurveySerializer(survey, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
def DeleteChoice(request, pk):
    choice = get_object_or_404(Choice, id=pk)
    choice.delete()
    return Response("Choice has been deleted", status=HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes((IsAdminUser,))
def CreateChoice(request):
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((IsAdminUser,))
def UpdateChoice(request, pk):
    choice = get_object_or_404(Choice,id=pk)
    serializer = ChoiceSerializer(instance=choice, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def ChoiceDetail(request, pk):
    choice = get_object_or_404(Choice,id=pk)
    serializer = ChoiceSerializer(choice)
    return Response(serializer.data)