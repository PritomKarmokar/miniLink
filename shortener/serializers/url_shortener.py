from rest_framework import serializers

class GenerateShortUrlSerializer(serializers.Serializer):
    url = serializers.URLField(max_length=2048)