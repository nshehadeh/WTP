# myapp/serializers.py

from rest_framework import serializers

class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField()
    response = serializers.CharField(read_only=True)
