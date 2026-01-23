from django.urls import path

from shortener.views import GenerateShortUrlAPI

urlpatterns = [
    path(
        'api/generate-short-url/',
        GenerateShortUrlAPI.as_view(),
        name='generate-short-url',
    )
]