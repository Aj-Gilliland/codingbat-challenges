from django.contrib import admin
from django.urls import path
from app.views import isNear, explode, countAnimals, isDoubles

urlpatterns = [
    path("admin/", admin.site.urls),
    path("warmup-1/near-hundred/<int:num>", isNear),
    path("warmup-2/String-Splosion/<str:stringThing>", explode),
    path("string-2/cat-dog/<str:animalString>", countAnimals),
    path("logic-2/lone-sum/<int:num1>/<int:num2>/<int:num3>", isDoubles),
]
  