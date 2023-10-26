from django.contrib import admin
from django.urls import path
from app.views import isNear, explode, countAnimals, isDoubles

urlpatterns = [
    path("admin/", admin.site.urls),
    path("warmup-1/<int:num>", isNear),
    path("warmup-2/<str:stringThing>", explode),
    path("string-2/<str:animalString>", countAnimals),
    path("logic-2/<int:num1>/<int:num2>/<int:num3>", isDoubles),
]
