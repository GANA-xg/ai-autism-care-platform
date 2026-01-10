from rest_framework import serializers
from .models import ScreeningSession, ScreeningResponse


class ScreeningResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreeningResponse
        fields = ('question', 'answer')


class ScreeningSessionSerializer(serializers.ModelSerializer):
    responses = ScreeningResponseSerializer(many=True)

    class Meta:
        model = ScreeningSession
        fields = '__all__'
        read_only_fields = ('total_score', 'risk_level')

    def create(self, validated_data):
        responses_data = validated_data.pop('responses')
        session = ScreeningSession.objects.create(**validated_data)

        answers = []
        for r in responses_data:
            ScreeningResponse.objects.create(session=session, **r)
            answers.append(r['answer'])

        from .scoring import calculate_risk
        score, risk = calculate_risk(answers)

        session.total_score = score
        session.risk_level = risk
        session.save()

        return session