from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


# def heyDude(request: HttpRequest, name):
#     return HttpResponse(f"Hey, {name}!")


def isDoubles(request: HttpRequest, num1: int, num2: int, num3: int) -> HttpResponse:
    masterNumber = 0
    if num1 == num2 and num2 == num3:
        return HttpResponse(masterNumber)
    if num1 != num2 and num1 != num3:
        masterNumber += num1 
    if num2 != num1 and num2 != num3:
        masterNumber += num2
    if num3 != num2 and num3 != num1:
        masterNumber += num3
    return HttpResponse(masterNumber)


def countAnimals(request: HttpRequest, animalString: str) -> HttpResponse:
    catAmout = animalString.count("cat")
    dogAmout = animalString.count("dog")
    if catAmout == dogAmout:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def explode(request: HttpRequest, stringThing: str) -> HttpResponse:
    if len(stringThing) >= 2:
        word = ""
        for i in range(len(stringThing)):
            word += stringThing[0 : i + 1]
        return HttpResponse(f"{word}")


def isNear(request: HttpRequest, num: int) -> HttpResponse:
    diff = [
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        107,
        108,
        109,
        110,
        190,
        191,
        192,
        193,
        194,
        195,
        196,
        197,
        198,
        199,
        200,
        201,
        202,
        203,
        204,
        205,
        206,
        207,
        208,
        209,
        210,
    ]
    for i in diff:
        if i == num:
            return HttpResponse(True)

    return HttpResponse(False)
