import requests
import time
address = 'http://localhost:8071'
wallet_to = 'fill_address_to_wallet'
time_out = 1
tx_quantity = 2
tx_sum = 1.00


if __name__ =="__main__":
    try:
        for i in range(tx_quantity):
            check_balance = requests.get(f'{address}/gettotalbalance').json()
            wallet = str("".join(list(requests.get(f'{address}/mywallet').json()['result'].keys())))
            balance = int(''.join(x for x in check_balance['result'][0:6] if x.isdigit()))
            send = requests.get(
                f'{address}/addtransaction?from={wallet}_{tx_sum}&to={wallet_to}_{tx_sum}&autofee=true').json()
            if balance > 2001:
                print(send)
                time.sleep(time_out)
    except:
        pass

