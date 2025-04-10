"""
URL configuration for throttling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api import views
from scoped import views as v2
from filter import views as v3
from serachfilter import views as v4
router=DefaultRouter()
router.register('studentroutermodel',views.StudentModelViewSet,basename='stu')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentviewsetmodel',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('studentlist/',v2.StudentList.as_view()),
    path('studentcreate/',v2.StudentCreate.as_view()),
    path('studentretrieve/<int:pk>/',v2.StudentRetrieve.as_view()),
    path('studentupdate/<int:pk>/',v2.StudentUpdate.as_view()),
    path('studentdestory/<int:pk>/',v2.Studentdelete.as_view()),
    path('studentapi/',v3.StudentList.as_view()),
    path('studentsearchapi/',v4.StudentList.as_view()),
]