from django.shortcuts import render
import json
import os
from datetime import datetime


# # Create your views here.

def index(request):
    current_date = datetime.now().date()
    context = {'date': current_date}
    return render(request, 'mainapp/index.html', context)


def products(request):
    # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # with open(os.path.join(base_dir, 'mainapp/fixtures/products.json'), 'r', encoding='utf-8') as f:
    #     products_data = json.load(f)
    context = {
        # 'title': 'каталог',
        # 'products': products_data
    }
    return render(request, 'mainapp/products.html', context)
