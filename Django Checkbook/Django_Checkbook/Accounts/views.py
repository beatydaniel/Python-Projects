from django.shortcuts import render, get_object_or_404, redirect

from .forms import AccountForm, InformationForm
from .models import Account


# Create your views here.

def home(request):
    accounts = Account.objects.all()
    return render(request, 'checkbook/index.html', {'accounts': accounts})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Account, pk=pk)
    form = AccountForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        return render(request, 'checkbook/index.html', {'form': form})


def createRecord(request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        print(form.errors)
        form = AccountForm()
    context = {
        'form': form,
    }
    return render(request, 'checkbook/CreateNewAccount.html', context)


def createTransaction(request):
    form = InformationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        print(form.errors)
        form = InformationForm()
    context = {
        'form': form,
    }
    return render(request, 'checkbook/AddTransaction.html', context)


