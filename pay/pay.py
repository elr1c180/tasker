from yoomoney import Quickpay

def get_payment_link(sum):
    quickpay = Quickpay(
                receiver="410019014512803",
                quickpay_form="shop",
                targets="Sponsor this project",
                paymentType="SB",
                sum=sum,
                )

    return quickpay.base_url