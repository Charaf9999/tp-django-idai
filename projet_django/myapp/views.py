from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render

from .models import Feature


def index(request):
    features = Feature.objects.all()
    context = {
        'name': 'Charaf',
        'age': 20,
        'moroccan': True,
        'features': features,
    }
    return render(request, 'index.html', context)


def counter(request):
    text = ''
    if request.method == 'POST':
        text = request.POST.get('text', '')
    else:
        text = request.GET.get('text', '')

    amount = len(text.split()) if text.strip() else 0
    return render(request, 'counter.html', {'amount': amount, 'text': text})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Cet email existe déjà.")
                return redirect('register')
            if User.objects.filter(username=username).exists():
                messages.info(request, "Ce nom d'utilisateur existe déjà.")
                return redirect('register')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Inscription réussie. Vous pouvez maintenant vous connecter.")
            return redirect('login')

        messages.info(request, "Les mots de passe ne sont pas identiques.")
        return redirect('register')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')

        messages.info(request, "Identifiants invalides.")
        return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')
