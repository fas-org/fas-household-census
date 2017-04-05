from ..forms import BuyerForm
from ..models import Buyer


def new(request):
    buyer_id = 0
    if request.method == "POST":
        form = BuyerForm(request.POST)
        buyer_id = save(form)
    else:
        form = BuyerForm()
    return form, buyer_id


def update(request):
        buyer_id = 0
        if request.method == "POST":
            form = BuyerForm(request.POST, instance=None)
            buyer_id = save(form)
        else:
            form = BuyerForm(instance=None)
        return form, buyer_id


def save(form):
    buyer_id = 0
    if form.is_valid():
        buyerform = form.save(commit=False)
        buyer_id = buyerform.pk
        buyerform.save()
    return buyer_id


def get(pk):
    try:
        buyer = Buyer.objects.get(pk=pk)
    except Buyer.DoesNotExist:
        buyer = None
    return buyer
