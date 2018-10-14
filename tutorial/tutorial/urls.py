from django.contrib import admin
from django.conf.urls import include, url
from courses import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'branch', views.BranchViewSet)
router.register(r'contact', views.ContactViewSet)


urlpatterns = [
    url('^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^course/', views.CourseViewSet),
    url(r'^course/(?P<pk>[0-9]+)/$', views.CourseDetailView.as_view()),
]