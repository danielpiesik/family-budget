from django.contrib.auth import models
from rest_framework import serializers

from .models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = (
            'id',
            'name',
            'created',
        )
        read_only_fields = (
            'id',
            'created',
        )
