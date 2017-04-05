from ..forms import LandSoldForm, LandBoughtForm, BuyerForm, SellerForm
from ..models import LandSold, LandBought, Buyer, Seller
from django.shortcuts import get_object_or_404, render, redirect
from . import household as household
from . import buyer, seller


def new(request):
    if request.method == "POST":
        landsoldform = LandSoldForm(request.POST)
        landboughtform = LandBoughtForm(request.POST)
        buyerform = BuyerForm(request.POST)
        sellerform = SellerForm(request.POST)
        if landsoldform.is_valid() and landboughtform.is_valid():
            buyer_id = buyer.new(request)
            landsold = landsoldform.save(commit=False)
            landsold.household = household.get(request.session['household'])
            landsold.buyer = buyer.get(buyer_id)
            landsold.save()

            seller_id = seller.new(request)
            landbought = landboughtform.save(commit=False)
            landbought.household = household.get(request.session['household'])
            landbought.seller = seller.get(seller_id)
            landbought.save()
            return redirect('landsales_edit', pk=landbought.pk)
    else:
        landsoldform = LandSoldForm()
        landboughtform = LandBoughtForm()
        buyerform = BuyerForm()
        sellerform = SellerForm()
    return render(request, 'land_sales_section4.html', {'landsold_form': landsoldform, 'landbought_form':landboughtform, 'buyer_form': buyerform, 'seller_form': sellerform})


def edit(request, pk):
    landsold = get_object_or_404(LandSold, pk=pk)
    if request.method == "POST":
        form = LandSoldForm(request.POST, instance=landsold)
        if form.is_valid():
            landsold = form.save(commit=False)
            landsold.save()
            return redirect('landsales_edit', pk=pk)
    else:
        form = LandSoldForm(instance=landsold)
    return render(request, 'land_sales_section4.html', {'landsold_form': form})


def get(household):
    try:
        landsold = LandSold.objects.get(household=household)
    except LandSold.DoesNotExist:
        landsold = None
    return landsold
