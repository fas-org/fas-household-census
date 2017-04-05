from ..forms.land_sales_forms_section4 import SellerForm
from ..models.land_sales_models_section4 import Seller


def new(request):
    seller_id = 0
    if request.method == "POST":
        form = SellerForm(request.POST)
        seller_id = save(form)
    else:
        form = SellerForm()
    return form, seller_id


def update(request):
    seller_id = 0
    if request.method == "POST":
        form = SellerForm(request.POST, instance=None)
        seller_id = save(form)
    else:
        form = SellerForm(instance=None)
    return form, seller_id


def save(form):
    seller_id = 0
    if form.is_valid():
        sellerform = form.save(commit=False)
        seller_id = sellerform.pk
        sellerform.save()
    return seller_id


def get(pk):
    try:
        buyer = Seller.objects.get(pk=pk)
    except Seller.DoesNotExist:
        buyer = None
    return buyer
