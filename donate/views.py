from django.shortcuts import render
from django.views import generic
from .forms import InquiryForm
from django.urls import reverse_lazy
import logging
from .paypay import test

logger = logging.getLogger(__name__)
# Create your views here.
class IndexView(generic.FormView):
    price = 1000
    template_name = "index.html"
    form_class = InquiryForm
    pay_url = test.pay_url(price)
    success_url = pay_url

    def form_valid(self, form):
        form.send_email()
        # messages.success(self.request, 'メッセージを送信しました。')
        price = format(form.cleaned_data['price'])
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class OmikujiView(generic.TemplateView):
    template_name = "omikuji.html"