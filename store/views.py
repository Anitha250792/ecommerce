# store/views.py
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product
from .forms import CustomLoginForm, CustomRegisterForm, ContactForm


def home(request):
    categories = [
        {
            "name": "Diapers & Pampers",
            "description": "For A Comfortable Night's Sleep",
            "image_url": "/static/images/diaper.png",
            "link": "/pampers"
        },
        {
            "name": "Baby Dress",
            "description": "Floral and comfy outfits",
            "image_url": "/static/images/dresses.png",
            "link": "/boys"
        },
        {
            "name": "Baby Soap",
            "description": "Gentle cleansing with natural ingredients",
            "image_url": "/static/images/soaps.png",
            "link": "/soaps"
        },
        {
            "name": "Baby Stroller & Prams",
            "description": "Adjustable comfort for every mood",
            "image_url": "/static/images/strollers.png",
            "link": "/stroller"
        }
    ]

    trust_items = [
        {
            "icon": "/static/images/dermatologist.png",
            "title": "Dermatologist Approved",
            "description": "Every product is tested and safe for even the most sensitive baby skin."
        },
        {
            "icon": "/static/images/natural.png",
            "title": "Natural & Non-Toxic Ingredients",
            "description": "We use only gentle, plant based formulas free from harsh chemicals."
        },
        {
            "icon": "/static/images/loved.png",
            "title": "Loved by Thousands of Parents",
            "description": "Real reviews, real results trusted by families across the country."
        },
        {
            "icon": "/static/images/eco.png",
            "title": "Eco-Friendly Promise",
            "description": "From biodegradable packaging to cruelty-free manufacturing, we care for the planet as much as your baby."
        },
        {
            "icon": "/static/images/shipping.png",
            "title": "Fast & Reliable Shipping",
            "description": "We deliver your baby’s essentials swiftly and safely because every moment counts."
        }
    ]

    best_sellers = [
        {
            "name": "wipes",
            "image_url": "/static/images/diapers.png",
            "mrp": 1444.00,
            "price": 1299.00,
            "rating": 5,
            "link": "/pampers"
        },
        {
            "name": "Mama Miel Baby",
            "image_url": "/static/images/babi.png",
            "mrp": 1444.00,
            "price": 1299.00,
            "rating": 5,
            "link": "/boys"
        },
        {
            "name": "Zibuyu",
            "image_url": "/static/images/zibu.png",
            "mrp": 1444.00,
            "price": 1299.00,
            "rating": 5,
            "link": "/girls"
        }
    ]

    products = [
        {
            "title": "Baby Stroller",
            "description": "Explore the world in comfort with our smooth and stylish baby stroller. Designed for safety, ease, and flexibility perfect for every little adventure. Lightweight, foldable, and parent-friendly for life on the go.",
            "image_url": "/static/images/babystroller.png",
            "link": "/stroller",
            "reverse": True
        },
        {
            "title": "Feeding Bottle",
            "description": "The baby feeding bottle is made from 100% BPA-free, safe materials. Its soft silicone nipple feels natural and gentle on the baby’s mouth. The anti-colic design helps reduce gas and fussiness during feeding. It’s lightweight, easy to hold, and perfect for everyday use.",
            "image_url": "/static/images/feeding.png",
            "link": "/bottle",
            "reverse": True
        },
        {
            "title": "Pampers",
            "description": "Keep your baby dry, comfy, and smiling all day with our ultra-soft diapers. Designed with leak-lock technology and breathable layers for extra protection. Gentle on delicate skin, perfect for day and night comfort.",
            "image_url": "/static/images/diapers.png",
            "link": "/pampers",
            "reverse":True
        }
    ]

    testimonials = [
        {"name": "Aarav Mehta", "location": "Mumbai", "review": "The baby lotion is so soft!", "image_url": "/static/images/baby.png"},
        {"name": "Priya Sharma", "location": "Delhi", "review": "Loved the eco-friendly wipes.", "image_url": "/static/images/babies.png"},
        {"name": "John Doe", "location": "Bangalore", "review": "Amazing stroller quality.", "image_url": "/static/images/zibu.png"},
        {"name": "Sofia Iyer", "location": "Chennai", "review": "Super gentle on my baby’s skin.", "image_url": "/static/images/babi.png"},
        {"name": "Ravi Patel", "location": "Pune", "review": "Fast delivery and great packaging.", "image_url": "/static/images/baby1.png"},
        {"name": "Neha Kapoor", "location": "Hyderabad", "review": "My baby sleeps better with their blanket.", "image_url": "/static/images/dress.png"},
    ]

    paginator = Paginator(testimonials, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    faqs = [
        {
            "question": "Are your products safe for newborns?",
            "answer": "Yes, all our products are dermatological tested and made with gentle, non-toxic ingredients that are safe for newborns and sensitive skin."
        },
        {
            "question": "How long does delivery take?",
            "answer": "Delivery usually takes 3-5 business days depending on your location."
        },
        {
            "question": "Can I return or exchange a product?",
            "answer": "Yes, you can return or exchange products within 14 days of purchase, provided they are unused and in original packaging."
        },
        {
            "question": "What payment methods do you accept?",
            "answer": "We accept all major credit/debit cards, UPI, and net banking."
        },
        {
            "question": "Are your skincare products organic or natural?",
            "answer": "Yes, our skincare range is made with certified organic and natural ingredients."
        }
    ]

    return render(request, 'home.html', {
        'categories': categories,
        'trust_items': trust_items,
        'best_sellers': best_sellers,
        'products': products,
        'testimonials_page': page_obj,
        'faqs': faqs
    })


def about(request):
    return render(request, 'about.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomRegisterForm()

    return render(request, 'register.html', {'form': form})


# Product list views
def pampers_list(request):
    products = Product.objects.filter(category__iexact="pampers").order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj, "title": "Pampers"})


def boys_list(request):
    products = Product.objects.filter(category__iexact="boys").order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj, "title": "Boys"})


def girls_list(request):
    products = Product.objects.filter(category__iexact="girls").order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj, "title": "Girls"})


def soaps_list(request):
    products = Product.objects.filter(category__iexact="soaps").order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj, "title": "Soaps"})


def stroller_list(request):
    products = Product.objects.filter(category__iexact="stroller").order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj, "title": "Stroller"})


def bottle_list(request):
    products = Product.objects.filter(category__iexact="bottle").order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj, "title": "Bottle"})


def all_products(request):
    products = Product.objects.all().order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj, "title": "All Products"})


def offers_list(request):
    products = Product.objects.filter(category__iexact="offer").order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "offers.html", {"page_obj": page_obj, "title": "Offers"})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contacts.html', {'form': form})
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
# store/views.py
from django.shortcuts import render

def cart_view(request):
    # For now, just render an empty cart page
    return render(request, 'cart.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import JsonResponse

# ------------------
# CART PAGE
# ------------------
def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, item in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * item['quantity']
        total += subtotal
        products.append({
            'product': product,
            'quantity': item['quantity'],
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {
        'products': products,
        'total': total
    })


# ------------------
# ADD TO CART
# ------------------
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.GET.get('quantity', 1))

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
    else:
        cart[str(product_id)] = {'quantity': quantity}

    request.session['cart'] = cart
    return redirect('cart_view')


# ------------------
# UPDATE QUANTITY
# ------------------
def update_cart_item(request):
    if request.method == 'POST':
        product_id = str(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity', 1))

        cart = request.session.get('cart', {})
        if product_id in cart:
            cart[product_id]['quantity'] = quantity
            request.session['cart'] = cart

    return redirect('cart_view')


# ------------------
# REMOVE ITEM
# ------------------
def remove_from_cart(request):
    if request.method == 'POST':
        product_id = str(request.POST.get('product_id'))

        cart = request.session.get('cart', {})
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart

    return redirect('cart_view')

# store/views.py
def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('coupon_code', '').strip()
        # Later you can validate the code against a Coupon model
        request.session['coupon'] = code
    return redirect('cart_view')
# store/views.py
from django.shortcuts import render, redirect
from django.contrib import messages

def checkout_view(request):
    if request.method == "POST":
        # Here you would process payment and save order details
        # Example:
        # order = Order.objects.create(...)
        messages.success(request, "Your order has been placed successfully!")
        return redirect('order_complete')
    return render(request, 'checkout.html')

def order_complete(request):
    return render(request, 'order_complete.html')



def search(request):
    query = request.GET.get('q', '').strip()
    if query:
        products = Product.objects.filter(name__icontains=query).order_by('-created_at')
    else:
        products = Product.objects.none()

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_results.html', {'page_obj': page_obj, 'query': query})
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
def category_products(request, category_name):
    products = Product.objects.filter(category__iexact=category_name).order_by('-created_at')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj, "title": category_name.capitalize()})
