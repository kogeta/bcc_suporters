import paypayopa
import time
API_KEY = 'a_mq2RAD8XrL_4iqN'
API_SECRET = '6r/asvLhV4vdA4g+m53lWlIn9i9g1itTpz7MvFnBJ1I='

def pay_url(price):
    client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
    client.set_assume_merchant("420846171797037056")

# requestの送信情報について
# => https://www.paypay.ne.jp/opa/doc/jp/v1.0/preauth_capture#operation/createAuth
    request = {
        "merchantPaymentId": round(time.time()), # => 加盟店発番のユニークな決済取引ID
        "codeType": "ORDER_QR",
        "redirectUrl": "http://127.0.0.1:8000/omikuji/", # => ここを任意のフロントのアプリにしてあげれば良さそう
        "redirectType": "WEB_LINK",
        "orderDescription":"BBC suporters",
        "orderItems": [{
            "name": "BBC suporters",
            "category": "pasteries",
            "quantity": 1,
            "productId": "67678",
            "unitPrice": {
                "amount": price,
                "currency": "JPY"
            }
        }],
        "amount": {
            "amount": price,
            "currency": "JPY"
        },
    }

    response = client.Code.create_qr_code(request)
    return response['data']['url']
    # print(response['resultInfo']['code'])
