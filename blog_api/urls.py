"""blog_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importações Django
from django.contrib import admin
from django.urls import include, path

# Importações DRF
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

# Importações da app
from blog_api.user import views as user_views
from blog_api.post import views as post_views

# nome da app
app_name = 'blog_api'

# Configurações de rotas padrões
router = routers.DefaultRouter()
router.register('post', post_views.PostViewSet)

# Padrões de URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('signup/', user_views.CreateUserView.as_view(), name='signup'),
    path('token_refresh', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
