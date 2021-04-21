from django.shortcuts import render
from .models import Category, SubCategory, Product
from django.core.paginator import Paginator
from django.http import JsonResponse

def index(request):
    category = Category.objects.all()       #все категории
    category_first_three = Category.objects.order_by('-name')[:3]     #три категории сортировка по имени
    subcategory = SubCategory.objects.all()      #все подкатегории
    product = Product.objects.all()      # все продукты
    product_rating = Product.objects.order_by('-rating')[:6]    # 6 самых популярных товаров
    product_rating_order = Product.objects.order_by('rating')[:6]     # самых непопулярных товаров
    context = {
        'category': category, 'category_first_three':category_first_three, 'subcategory': subcategory, 'product': product, 'product_rating': product_rating, 'product_rating_order': product_rating_order
    }
    return render(request, 'shop/index.html', context)

def shop(request):
    return render(request, 'shop/shop.html')

def by_category(request, category_id):
    current_category = Category.objects.get(pk=category_id)     # конкретная категория по ключу
    subcategory = SubCategory.objects.filter(category=category_id)    # все подкатегории данной категории по ключу
    context = {
        'current_category': current_category, 'subcategory': subcategory
    }
    return render(request, 'shop/by_category.html', context)

def by_subcategory(request, category_id, subcategory_id):
    current_category = Category.objects.get(pk=category_id)       # кокретная категория по ключу
    current_subcategory = SubCategory.objects.get(pk=subcategory_id)   # конкретная подкатегория по ключу
    product = Product.objects.filter(subcategory=subcategory_id)     # все товары данной подкатегории по ключу
    my_model = Product.objects.filter(subcategory=subcategory_id).order_by('price')    # все товары данной подкатегории отсортированные по возрастанию
    my_model2 = Product.objects.filter(subcategory=subcategory_id).order_by('-price') #  все товары данной подкатегории отсортированные по убыванию
    number_of_item = 9    # количество отображаемых товаров на одной странице
    paginatorr = Paginator(my_model, number_of_item)     # пагинатор для товаров по возрастанию
    paginatorr2 = Paginator(my_model2, number_of_item)  # пагинатор для товаров по убыванию
    first_page = paginatorr.page(1).object_list      # список товаров первой страницы
    page_range = paginatorr.page_range     # количество страниц
    

    
    context = {
        'current_category': current_category, 
        'current_subcategory': current_subcategory, 
        'product': product,
        'paginatorr': paginatorr,
        'first_page': first_page,
        'page_range': page_range
    }
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None) # получаем из href="номер страницы" 
        in_ascending_order = list(paginatorr.page(page_n).object_list.values('id', 'title', 'price', 'img'))
        in_descending_order = list(paginatorr2.page(page_n).object_list.values('id', 'title', 'price', 'img'))
        return JsonResponse({"in_ascending_order": in_ascending_order, "in_descending_order": in_descending_order})
    return render(request, 'shop/by_subcategory.html', context)

def product_page(request, category_id, subcategory_id, product_id):
    product = Product.objects.get(pk=product_id)
    current_subcategory = SubCategory.objects.get(pk=subcategory_id)
    current_category = Category.objects.get(pk=category_id)
    context = {
        'product': product, 'current_subcategory': current_subcategory, 'current_category': current_category
    }
    return render(request, 'shop/product.html', context)



def pagination_pro(request):
    #model
    my_model = Product.objects.all()
    #number of items on each page
    number_of_item = 3
    #Paginator 
    paginatorr = Paginator(my_model, number_of_item)
    #query_set for first page
    first_page = paginatorr.page(1).object_list
    #range of page ex range(1, 3)
    page_range = paginatorr.page_range

    context = {
    'paginatorr':paginatorr,
    'first_page':first_page,
    'page_range':page_range
    }
    #
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None) #getting page number
        results = list(paginatorr.page(page_n).object_list.values('id', 'title'))
        return JsonResponse({"results":results})


    return render(request, 'shop/pagin.html',context)
