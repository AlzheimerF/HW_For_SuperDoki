from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('basket', views.BasketViewSet)


urlpatterns = router.urls

