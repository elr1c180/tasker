from yoomoney import Quickpay
from yoomoney import Client
import uuid
import os

def get_payment_link(sum):
    quickpay = Quickpay(
        receiver="4100118826773575",
        quickpay_form="shop",
        targets="Sponsor this project",
        paymentType="SB",
        sum=sum,
        label = str(uuid.uuid4())
    )

    """
    Верни кортеж (quickpay.base_url, str(uuid.uuid4()))
    Далее сохраняй в очередь label и user_id из телеграм и можно каждую минту проверять статус операции
    В качетсве очереди можно использовать таблицу в psql payment_transactions
    
    payment_transactions
    ----
    id int 
    created_on timestamp
    user_id bigint
    amount float
    label varchar(60)
    status varchar(50) default 'in progress'
    
    далее каждые 3 минуты выбирать из базы все транзакции в статусе in progress
    
    with Session() as session: 
        in_progress_transactions = session.query(payment_transactions).filter(payment_transactions.status == 'in progress').all()
        for in_progress_transaction in in_progress_transactions: 
            transaction = get_status_operation_by_lable(in_progress_transaction.label)
            if len(transaction.operations) > 0 and transaction.operations[0].status == 'success':
                #Обновлять сумму средств в личном кабинете 
                user = session.query(user).filter(user.id = in_progress_transaction.user_id).one_or_none()
                user.balanse = user.balanse + in_progress_transaction.amount
                #Отправлять в телеге сообщение: 
                send_message(in_progress_transaction.user_id, f"Вам зачисленно {in_progress_transaction.amount}. Ваш Баланс {user.balanse}")
                
                #Обновлять статус транзакции в базе чтобы не обращаться к ней вновь
                in_progress_transaction.status = 'success'
                
        session.commit()
    
    """
    return quickpay.base_url

def get_status_operation_by_lable(label):
    """

    :param label: label операции который получили в методе get_payment_link
    :return: истории операций

    Пример использования:


    :Пример:

        history = get_status_operation_by_lable('mylabel')
        if len(history.operations) > 0 and history.operations[0].status == 'success':
            print('Операция Выполнена')
            #Можно отправлять уведомление


    """
    return Client(os.getenv("YOOMONEY_TOKEN")).operation_history(label=label)