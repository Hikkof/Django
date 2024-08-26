from django.shortcuts import render, redirect
from homebrew.models import Homebrew
from .forms import SignUpForm


def front(request):
    homebrews = Homebrew.objects.all()[::-1]

    return render(request, 'core/front.html', {'homebrews' : homebrews[0:3]})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  # username taken/incorrect email/password too short/incorrect password
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form' : form})


def contact(request):
    return render(request, 'core/contact.html')


def terms_of_use(request):
    return render(request, 'core/terms_of_use.html')
