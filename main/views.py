from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'footer': 'Copyright © Home Ilya Kaplun 2024'
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - Главная',
        'content1': 'О нас',
        'content2': 'Текст о том какой классный этот интернет магазин.',
        'footer': 'Copyright © Home Ilya Kaplun 2024'
    }

    return render(request, 'main/about.html', context)

def delivery(request):
    context = {
        'title': 'Home - Главная',
        'title_on_page': 'Доставка',
        'content1': 'Мы умеем доставлять товары.',
        'content2': 'Вы можете не оплачивать товары.',
        'footer': 'Copyright © Home Ilya Kaplun 2024'
    }

    return render(request, 'main/delivery.html', context)

def contacts(request):
    context = {
        'title': 'Home - Главная',
        'title_on_page': 'Контакты',
        'tel': 'phone: +7 985 654 32 23',
        'email': 'email: home@mail.ru',
        'footer': 'Copyright © Home Ilya Kaplun 2024'
    }

    return render(request, 'main/contacts.html', context)