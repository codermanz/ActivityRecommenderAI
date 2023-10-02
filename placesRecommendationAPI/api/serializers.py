from rest_framework import serializers
from .models import Suggestion


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ['url', 'title', 'description']


class ResponseSerializer(serializers.Serializer):
    response_summary = serializers.CharField()
    suggestions = SuggestionSerializer(many=True)
