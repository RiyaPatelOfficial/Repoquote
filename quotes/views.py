from django.shortcuts import render, redirect
from .models import Quote
import random

def home(request):

    quotes = Quote.objects.all()

    random_quote = (
        random.choice(quotes)
        if quotes.exists()
        else None
    )

    return render(
        request,
        "home.html",
        {
            "random_quote": random_quote,
            "quotes": quotes
        }
    )

def add_quote(request):

    if request.method == "POST":

        Quote.objects.create(
            text=request.POST.get("text"),
            author=request.POST.get("author")
        )

        return redirect('/')

    return render(
        request,
        "add_quote.html"
    )