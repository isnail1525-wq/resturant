from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm



def item_list(request):
    items = Item.objects.all()
    return render(request, "item_list.html", {"items": items})


def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return redirect("menu:item-list")
    return render(request, "item_detail.html", {"item": item})


@login_required
def item_add(request):
    if not request.user.is_superuser:  
        return redirect("menu:item-list")

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("menu:item-list")
    else:
        form = ItemForm()
    return render(request, "item_form.html", {"form": form})



@login_required
def item_edit(request, pk):
    if not request.user.is_superuser:
        return redirect("menu:item-list")

    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return redirect("menu:item-list")

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("menu:item-detail", pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {"form": form, "item": item})



@login_required
def item_delete(request, pk):
    if not request.user.is_superuser:
        return redirect("menu:item-list")

    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return redirect("menu:item-list")

    if request.method == "POST":
        item.delete()
        return redirect("menu:item-list")
    return render(request, "item_confirm_delete.html", {"item": item})
