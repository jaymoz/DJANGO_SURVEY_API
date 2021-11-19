from rest_framework import serializers
from .models import Survey, SurveyQuestions, UserResponse, Choice

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'
        read_only_fields = ['id','start_date']
    
class SurveyQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestions
        fields = '__all__'
        read_only_fields = ['id']

class ResponseQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserResponse
        fields = '__all__'
        read_only_fields = ['id']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        read_only_fields = ['id']

