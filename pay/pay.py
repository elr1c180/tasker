from yoomoney import Quickpay

def get_payment_link(sum):
    quickpay = Quickpay(
                receiver="4100118826773575",
                quickpay_form="shop",
                targets="Sponsor this project",
                paymentType="SB",
                sum=sum,
                )

    return quickpay.base_url