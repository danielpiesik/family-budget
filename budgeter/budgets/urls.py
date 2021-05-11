from rest_framework import routers

from .views import BudgetViewSet


router = routers.DefaultRouter()
router.register('', BudgetViewSet, basename='budgets')
urlpatterns = router.urls
