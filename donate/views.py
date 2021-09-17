from django.shortcuts import redirect
from django.views import generic
from .forms import InquiryForm
from django.urls import reverse_lazy
import logging
from .paypay import test

logger = logging.getLogger(__name__)
# Create your views here.
price = {"donate" : int} # 寄付金額を保持

class IndexView(generic.FormView):
    template_name = "index.html"
    form_class = InquiryForm
    success_url = 'result'

    def form_valid(self, form):
        form.send_email()
        # messages.success(self.request, 'メッセージを送信しました。')
        price["donate"] = format(form.cleaned_data['price'])
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

def result_view(request):
    redirect_url = str(request._current_scheme_host)+"/omikuji/"
    pay_price = price["donate"]
    pay_url = test.pay_url( int(pay_price) ,redirect_url )
    return redirect(pay_url)
class OmikujiView(generic.TemplateView):
    template_name = "omikuji.html"