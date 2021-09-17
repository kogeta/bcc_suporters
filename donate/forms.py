from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30,  required=False)
    email = forms.EmailField(label='メールアドレス')
    price = forms.IntegerField(label='寄付額', min_value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前を入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください。'

        self.fields['price'].widget.attrs['class'] = 'form-control col-11'
        self.fields['price'].widget.attrs['placeholder'] = 'ご寄付いただける金額を入力ください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        price = self.cleaned_data['price']

        subject = '{}様　ご寄付ありがとうございます'.format(name)
        message = '送信者名: {0}\nメールアドレス: {1}\n寄付金額:\n{2}'.format(name, email, price)
        from_email = 't_koga9278@yahoo.co.jp'
        to_list = [
            email
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()