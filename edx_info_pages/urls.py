from django.urls import include, path

urlpatterns = [
    path('tinymce/', include('tinymce.urls'))
]
