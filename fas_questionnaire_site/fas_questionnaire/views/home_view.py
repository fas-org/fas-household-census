from . import household, introduction, buyer, seller, landsold, landbought
from django.shortcuts import render, redirect


def new(request):
    household_form = household.new(request)
    introduction_form = introduction.new(request)

    buyer_form, buyer_id = buyer.new(request)
    landsold_form = landsold.new(request, buyer_id)

    seller_form, seller_id = seller.new(request)
    landbought_form = landbought.new(request, seller_id)

    if request.session['household'] == 0:
        return render(request, 'home.html',
                      {'household_form': household_form, 'introduction_form': introduction_form,
                       'buyer_form': buyer_form, 'landsold_form': landsold_form, 'seller_form': seller_form, 'landbought_form': landbought_form})
    else:
        return redirect('home_update', pk=request.session['household'])


def update(request, pk):
    request.session['household'] = pk  # when coming from search
    household_form = household.update(request, pk)
    introduction_form = introduction.update(request, pk)
    buyer_form,buyer_id = buyer.update(request)
    landsold_form = landsold.update(request, pk, buyer_id)

    seller_form, seller_id = seller.new(request)
    landbought_form = landbought.new(request, seller_id)

    # keep on adding update views
    return render(request, 'home.html',
                  {'household_form': household_form, 'introduction_form': introduction_form,
                   'buyer_form': buyer_form, 'landsold_form': landsold_form, 'seller_form': seller_form, 'landbought_form': landbought_form})
