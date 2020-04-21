"""elearning URL Configuration"""

from django.urls import path, include
from django.contrib import admin

from rest_framework import routers

from courses.views import (course_add, course_detail, course_list, do_section,
                           do_test, show_results)
from students.views import student_detail  # , UserViewSet


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'sections', SectionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('course_detail/<pk>/', course_detail, name='course_detail'),
    path('course_add/', course_add, name='course_add'),
    path('section/<int:section_id>/', do_section, name='do_section'),
    path('section/<int:section_id>/test/', do_test, name='do_test'),
    path('section/<int:section_id>/results/',
         show_results, name='show_results'),
    path('student_detail/', student_detail, name='student_detail'),
    # path('api/', include(router.urls)),
    path('', course_list),
]
