from django.shortcuts import render




def intx(request):
    return render(request, 'intx/index.html')

def payment_link_view(request):
    payment_link_html = """
        <span>አሁኑኑ በ </span>
        <a id="yenepayLogo" href="https://yenepay.com/checkout/Home/Process/?ItemName=Ticket&ItemId=&UnitPrice=900&Quantity=1&Process=Express&ExpiresAfter=&DeliveryFee=&HandlingFee=&Tax1=&Tax2=&Discount=&SuccessUrl=&IPNUrl=&MerchantId=33431">
            <img style="width:100px" src="https://yenepayprod.blob.core.windows.net/images/logo.png">
        </a>
        <span> ይግዙ</span>
    """

    return render(request, 'intx/pay.html', {'payment_link_html': payment_link_html})
