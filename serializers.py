from rest_framework import serializers
from .models import question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = question
        url = serializers.SerializerMethodField(read_only=True)

    # converts to JSON
    # validations for data passed

    def get_url(self, obj):
        # request
        request = self.context.get("request")
        return obj.get_api_url(request=request)
