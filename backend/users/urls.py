
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet
from rest_framework.authtoken.views import obtain_auth_token  # Import token login view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import google_login


# Initialize the router and register the RegisterViewSet under 'register'
router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')

urlpatterns = [
    path('api/', include(router.urls)),  # Includes all the routes for the RegisterViewSet
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh
    path('auth/', include('social_django.urls')),
    path('api/google-login/', google_login, name='google-login')
    
   
]
