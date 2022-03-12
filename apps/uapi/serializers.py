from rest_framework import serializers
from apps.uapi.models import Sessions

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = ['id','timeLimit','topicIds','maxQuestionCount' ]


    def create(self, validated_data):
        return Sessions.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.superDivisionIds = validated_data.get('superDivisionIds', instance.superDivisionIds)
        instance.divisionIds = validated_data.get('topicIds', instance.divisionIds)
        instance.maxQuestionCount = validated_data.get('maxQuestionCount', instance.maxQuestionCount)
        instance.questionIdList = validated_data.get('questionIdList', instance.questionList)
        instance.save()
        return instance