from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the news items index.")


def source_list(request, source_id):
    return HttpResponse(f"You're looking at a list of items for {source_id}.")


def detail(request, source_id, question_id):
    return HttpResponse(
        f"You're looking at item {question_id} from source {source_id}."
    )
