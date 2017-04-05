from ..forms.land_sales_forms_section4 import BuyerForm
from ..models.land_sales_models_section4 import Buyer


def new(request):
    buyer_id = 0
    if request.method == "POST":
        form = BuyerForm(request.POST)
        if form.is_valid():
            buyerform = form.save(commit=False)
            buyerform.save()
            buyer_id = buyerform.pk
    return buyer_id


def update(request):
    buyer_id = 0
    if request.method == "POST":
        form = BuyerForm(request.POST, instance=None)
        buyer_id = save(form)
    else:
        form = BuyerForm(instance=None)
    return form, buyer_id


def get(pk):
    try:
        buyer = Buyer.objects.get(pk=pk)
    except Buyer.DoesNotExist:
        buyer = None
    return buyer
