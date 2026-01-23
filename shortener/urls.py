from django.urls import path

from shortener.views import GenerateShortUrlAPI, RedirectUrlAPI

urlpatterns = [
    path(
        'api/generate-short-url/',
        GenerateShortUrlAPI.as_view(),
        name='generate-short-url',
    ),
    path(
        '<str:token>/',
        RedirectUrlAPI.as_view(),
        name='redirect-url'
    )
]