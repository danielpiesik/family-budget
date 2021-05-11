from django.db import models


class Budget(models.Model):
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='own_budgets',
    )
    name = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
