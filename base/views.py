from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils.translation import get_language
from .models import Product, Category
from .forms import productForm
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def home(request):
    current_lang = get_language() 
    q = request.GET.get('q') if request.GET.get('q') else ''
    
    products = Product.objects.filter(
        Q(name__icontains=q) | Q(description__icontains=q),
        language=current_lang
    )

    context = {
        'products': products,
        'current_lang': current_lang,
    }
    return render(request, "home.html", context)



def categories(request):
    current_lang = get_language()
    categories = Category.objects.filter(language=current_lang)
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    products = Product.objects.filter(category__name__iexact=q, language=current_lang)
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, "categories.html", context)



def about(request):
    context = {}
    return render(request, "about.html", context)



def product(request, pk):
    data = {
    1: {"wilaya": "Adrar", "home": 1400, "office": 970},
    2: {"wilaya": "Chlef", "home": 750, "office": 520},
    3: {"wilaya": "Laghouat", "home": 950, "office": 670},
    4: {"wilaya": "Oum El Bouaghi", "home": 700, "office": 520},
    5: {"wilaya": "Batna", "home": 700, "office": 520},
    6: {"wilaya": "Bejaia", "home": 750, "office": 520},
    7: {"wilaya": "Biskra", "home": 900, "office": 620},
    8: {"wilaya": "Bechar", "home": 1100, "office": 720},
    9: {"wilaya": "Blida", "home": 750, "office": 520},
    10: {"wilaya": "Bouira", "home": 700, "office": 520},
    11: {"wilaya": "Tamanrasset", "home": 1600, "office": 1120},
    12: {"wilaya": "Tebessa", "home": 800, "office": 520},
    13: {"wilaya": "Tlemcen", "home": 900, "office": 570},
    14: {"wilaya": "Tiaret", "home": 800, "office": 520},
    15: {"wilaya": "Tizi Ouzou", "home": 700, "office": 520},
    16: {"wilaya": "Alger", "home": 600, "office": 470},
    17: {"wilaya": "Djelfa", "home": 950, "office": 670},
    18: {"wilaya": "Jijel", "home": 750, "office": 520},
    19: {"wilaya": "Setif", "home": 750, "office": 520},
    20: {"wilaya": "Saida", "home": 800, "office": 570},
    21: {"wilaya": "Skikda", "home": 700, "office": 520},
    22: {"wilaya": "Sidi Bel Abbess", "home": 800, "office": 520},
    23: {"wilaya": "Annaba", "home": 750, "office": 520},
    24: {"wilaya": "Guelma", "home": 700, "office": 520},
    25: {"wilaya": "Constantine", "home": 500, "office": 370},
    26: {"wilaya": "Medea", "home": 800, "office": 520},
    27: {"wilaya": "Mostghanem", "home": 800, "office": 520},
    28: {"wilaya": "Msila", "home": 800, "office": 570},
    29: {"wilaya": "Mascara", "home": 800, "office": 520},
    30: {"wilaya": "Ouargla", "home": 900, "office": 670},
    31: {"wilaya": "Oran", "home": 750, "office": 720},
    32: {"wilaya": "El Bayadh", "home": 1050, "office": 670},
    # 33: {"wilaya": "Illizi", "home": None, "office": None},
    34: {"wilaya": "Bordj Bou Arreridj", "home": 700, "office": 520},
    35: {"wilaya": "Boumerdes", "home": 750, "office": 520},
    36: {"wilaya": "El Tarf", "home": 800, "office": 520},
    # 37: {"wilaya": "Tindouf", "home": None, "office": None},
    38: {"wilaya": "Tissemsilt", "home": 800, "office": None},  # office not available
    39: {"wilaya": "Eloued", "home": 950, "office": 670},
    40: {"wilaya": "Khenchela", "home": 700, "office": None},  # office not available
    41: {"wilaya": "Souk Ahras", "home": 750, "office": 520},
    42: {"wilaya": "Tipaza", "home": 800, "office": 520},
    43: {"wilaya": "Mila", "home": 750, "office": 520},
    44: {"wilaya": "Ain Defla", "home": 750, "office": 520},
    45: {"wilaya": "Naama", "home": 1100, "office": 670},
    46: {"wilaya": "AinTemouchent", "home": 800, "office": 520},
    47: {"wilaya": "Ghardaia", "home": 950, "office": 670},
    48: {"wilaya": "Relizane", "home": 800, "office": 520},
    49: {"wilaya": "Timimoun", "home": 1400, "office": None},  # office not available
    # 50: {"wilaya": "BordjBadji Mokhtar", "home": None, "office": None},
    51: {"wilaya": "Ouleddjellal", "home": 900, "office": 620},
    52: {"wilaya": "Beniabbes", "home": 1000, "office": 970},
    53: {"wilaya": "In Saleh", "home": 1600, "office": None},  # office not available
    54: {"wilaya": "Inguezzam", "home": 1600, "office": None},  # office not available
    55: {"wilaya": "Touggourt", "home": 950, "office": 670},
    # 56: {"wilaya": "Djelfa", "home": None, "office": None},
    57: {"wilaya": "Mghair", "home": 950, "office": None},  # office not available
    58: {"wilaya": "El menia", "home": 1000, "office": None},  # office not available
    
}

    product = Product.objects.get(pk=pk)
    context = {
        'pk': pk,
        'product': product,
        'data': data,
    }
    if request.method == 'POST':
        print("POST request received")
        #extract the data from the form
        """
        the post request example:
        <QueryDict: {'csrfmiddlewaretoken': ['0ITsZAyqeO9o9daIC3XokfacxVNPWUxdh4SMlz7erxksDI6meZsHdJs1ShFQqUos'],
        'full_name': ['aa'],
        'phone_number': ['aa'],
        'wilaya': ['Oum El Bouaghi'],
        'delivery_type': ['home'],
        'municipality': ['aaa'],
        'quantity': ['2'],
        'unit_price': ['5000'],
        'delivery_tax': ['700'],
        'total_price': ['10700']}>
        """
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        wilaya = request.POST.get('wilaya')
        delivery_type = request.POST.get('delivery_type')
        municipality = request.POST.get('municipality')
        quantity = request.POST.get('quantity')
        unit_price = request.POST.get('unit_price')
        delivery_tax = request.POST.get('delivery_tax')
        total_price = request.POST.get('total_price')

        #now we send the email data to the admin (client)
        subject = f"New Order from {full_name}"
        message = f"""
        You have a new order from {full_name}.\n
        product: {product.name}\n
        Phone Number: {phone_number}\n
        Wilaya: {wilaya}\n
        Delivery Type: {delivery_type}\n
        Municipality: {municipality}\n
        Quantity: {quantity}\n
        Unit Price: {unit_price}DA\n
        Delivery Tax: {delivery_tax}DA\n
        Total Price: {total_price}DA
        """
        email_from = "khalil.ghanem.dev@gmail.com"
        recipient_list = ["khalil.ghanem.dev@gmail.com"]
        try:
            send_mail(subject, message, email_from, recipient_list)
            print("Email sent successfully")
        except Exception as e:
            print(f"Error sending email: {e}")
            # You might want to handle the error more gracefully in a real application


    return render(request, "product.html", context)



def add_product(request):
    form = productForm()
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = { 'form': form }
    return render(request, "add_product.html", context)



def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    form = productForm(instance=product)
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = { 'form': form }
    return render(request, "add_product.html", context)



def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    context = { 'product': product }
    return render(request, "delete_product.html", context)