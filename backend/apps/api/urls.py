from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, ProgramViewSet, ProgressViewSet, ProgressSummaryView, LanguageListView
)

router = DefaultRouter()
router.register(r'programs', ProgramViewSet, basename='program')
router.register(r'progress', ProgressViewSet, basename='progress')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('i18n/languages/', LanguageListView.as_view(), name='language_list'),
    path('progress/<int:program_id>/summary/', ProgressSummaryView.as_view(), name='progress-summary'),
    path('', include(router.urls)),
]