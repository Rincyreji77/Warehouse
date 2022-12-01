from unicodedata import name
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import AddProduct
from .models import Purchase
from .forms import PurchaseForm



# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"contact.html")

def admin_login(request):
    if request.method == "POST":
                username = request.POST.get("username")
                password = request.POST.get("password")
                myuser= authenticate(username=username,password=password)
                if myuser is not None:
                    login(request,myuser)
                    return redirect("/admin_home")
                else:
                    
                    return redirect("/admin_login")
    return render(request,"admin_login.html")
    
def admin_home(request):
    return render(request,"admin_home.html")

def user_login(request):
    if request.method == "POST":
            username = request.POST.get("uname")
            password = request.POST.get("passwrd")
            myuser1= authenticate(username=username,password=password)
            if myuser1 is not None:
                login(request,myuser1)
                return redirect("/user_home")
            else:
                return redirect("/user_login")
    return render(request,"user_login.html")

def user_home(request):
    return render(request,"user_home.html")

def signup(request):
    if request.method == "POST":
      
        name = request.POST.get("name")
        email = request.POST.get("mail")
        password = request.POST.get("pswrd")
        cpassword = request.POST.get("cpswrd")
        if(password != cpassword):
            return redirect("/signup")
        try:
            if User.objects.get(name=name):
                return redirect("/signup")
        except:
            pass

        user1 = User.objects.create_user(name,email,password)
        # user.name = name
        user1.username=name
        user1.save()
        return redirect("/user_login")
    return render(request,"signup.html")

def add_product(request):
    if request.method == "POST":
        slno = request.POST.get('slno')
        name = request.POST.get('name')
        image = request.POST.get('image')
        stock = request.POST.get('stock')
        price = request.POST.get('price')
        add_product = AddProduct(slno=slno,name=name,image=image,stock=stock,price=price)
        add_product.save()
    return render(request, 'add_product.html')

def product_view(request):
    pro=AddProduct.objects.all()
    return render(request,"product_view.html", {'myapp':pro})


def user_view(request):
    pro=AddProduct.objects.all()
    return render(request,"user_view.html", {'myapp':pro})




def purchase(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        purchase = Purchase(name=name,address=address,phone=phone,email=email,item=item,quantity=quantity,price=price)
        purchase.save()
    return render(request,"purchase.html")


def order_list(request):
    ord=Purchase.objects.all()
    return render(request,"order_list.html", {'myapp':ord})

def order_view(request):
    view=Purchase.objects.all()
    return render(request,"usord_view.html", {'myapp':view})

def edit(request,id):
    edt = Purchase.objects.get(id=id)
    return render(request,"edit.html",{'myapp':edt}) 

def update(request,id):
    upd = Purchase.objects.get(id=id)
    form = PurchaseForm(request.POST,instance=upd) 
    if form.is_valid(): 
        form.save()  
        return redirect('/usord_view')  
    return render(request,"edit.html",{'myapp':upd}) 

def destroy(request,id):
    dlt=Purchase.objects.get(id=id)
    dlt.delete()
    return redirect('/usord_view')  