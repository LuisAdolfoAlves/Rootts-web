from django.shortcuts import render, redirect
from .forms import EncostaForm, EncostaFormUpdate

from .models import Encosta


def IndexView(request):
  return render(request, 'index.html')

def EncostaView(request):
  encostas = Encosta.objects.all()
  return render(request, 'crud.html', {'encostas': encostas})


# create view
def CreateEncostaView(request):
  form = EncostaForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('crud')
  return render(request, 'encosta_add.html', {'form': form})

def UpdateEncostaView(request, pk):
  encosta = Encosta.objects.get(id=pk)
  form = EncostaFormUpdate(request.POST or None, instance=encosta)
  if form.is_valid():
    form.save()
    return redirect('crud')
  return render(request, 'encosta_upd.html', {'form': form, 'encosta': encosta})


# delete view
def DeleteEncostaView(request, pk):
  encosta = Encosta.objects.get(id=pk)
  if request.method == 'POST':
    encosta.delete()
    return redirect('crud')
  return render(request, 'encosta_del.html', {'encosta': encosta})