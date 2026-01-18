from rest_framework import serializers
from .models import TherapyPlan, TherapyGoal


class TherapyGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TherapyGoal
        fields = '__all__'


class TherapyPlanSerializer(serializers.ModelSerializer):
    goals = TherapyGoalSerializer(many=True)

    class Meta:
        model = TherapyPlan
        fields = '__all__'

    def create(self, validated_data):
        goals_data = validated_data.pop('goals')
        plan = TherapyPlan.objects.create(**validated_data)
        for goal in goals_data:
            TherapyGoal.objects.create(plan=plan, **goal)
        return plan