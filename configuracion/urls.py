
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cuentas.views import UsuarioViewSet
from inventario.views import InventarioDetailView,  InventarioLisView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('usuario', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/inventario/',InventarioLisView.as_view(),name="lista-inventario"),
    path('api/inventario/<int:pk>/',InventarioDetailView.as_view(),name="detalle-inventario"),
    path('api/', include(router.urls))
]
