from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required



def customer_list(request):
    customers = Customer.objects.all()
    return render(request, "customer_list.html", {"customers": customers})



def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return redirect("customers:customer-list")
    return render(request, "customer_detail.html", {"customer": customer})



def customer_add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customers:customer-list")
    else:
        form = CustomerForm()
    return render(request, "customer_form.html", {"form": form})




@login_required
def customer_edit(request, pk):
   
    if not request.user.is_superuser:
        return redirect("customers:customer-list")

    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return redirect("customers:customer-list")

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customers:customer-list")
    else:
        form = CustomerForm(instance=customer)
    return render(request, "customer_form.html", {"form": form})





@login_required
def customer_delete(request, pk):
   
    if not request.user.is_superuser:
        return redirect("customers:customer-list")

    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return redirect("customers:customer-list")

    if request.method == "POST":
        customer.delete()
        return redirect("customers:customer-list")

    return render(request, "customer_confirm_delete.html", {"customer": customer})

