"""ExamOnLine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from users import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.views import static as static1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/', include('exam.urls', namespace='exam')),
    path('user/', include('users.urls', namespace='user')),

    # 主页、登录、注销、注册/+/
    path('index/', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/forgort_pwd/<int:idcard>/', views.forgort_pwd, name='forgort_pwd'),

    url(r'^static/(?P<path>.*)$', static1.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# todo 这里必须制定后面的static才能正常显示