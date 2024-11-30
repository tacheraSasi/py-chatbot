from django.shortcuts import render
from .chatbot import get_answer

def home(request):
    return render(request,"index.html")


def chat(request):
    if request.method == "POST":
        input = request.POST["input"]
        return print(get_answer(input))
    return "Invalid method"
