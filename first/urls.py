
from django.contrib import admin
from django.urls import path
from api import views
from update import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stuinfo/<int:pk>/',views.student_detail),
    # path('stulist',views.student_list)

    path('stucreate/',views.student_create),
    # path('stuupdate/',v.student_api),
    path('stuupdate/',v.Studentapi.as_view()),
]
