from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.shortcuts import render, redirect
from charts.models import Vulnerabilities


def index(request):
    unremediated = Vulnerabilities.objects.filter(unremediated=True)
    remediated = Vulnerabilities.objects.filter(unremediated=False)
    unremediated_by_status = Vulnerabilities.objects.filter(unremediated=True).values('status') \
        .annotate(total=Count('status')).order_by('status')
    unremediated_by_severity = Vulnerabilities.objects.filter(unremediated=True).values('severity') \
        .annotate(total=Count('severity')).order_by('severity')

    return render(request, "index.html", {
        'unremediated': int(len(unremediated)),
        'remediated': int(len(remediated)),
        'total': int(len(unremediated)) + int(len(remediated)),
        'unremediated_by_severity': unremediated_by_severity,
        'unremediated_by_status': unremediated_by_status
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
