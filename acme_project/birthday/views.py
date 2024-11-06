from django.shortcuts import render
from .forms import BirthdayForm


def birthday(request):
    # Создаём экземпляр класса формы.
    form = BirthdayForm()
    # Добавляем его в словарь контекста под ключом form:
    context = {'form': form}
    # Указываем нужный шаблон и передаём в него словарь контекста.
    return render(request, 'birthday/birthday.html', context) 