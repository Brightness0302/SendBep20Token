from web3 import Web3
import time
import json
import requests
from urllib.request import urlopen

# enter your private key.  Be careful with your private key
PRIVATE_KEY = "Your PRIVATE_KEY"

# add your blockchain connection information
url_eth = 'https://api.bscscan.com/api'
bsc = 'https://bsc-dataseed.binance.org/'
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

# enter the account that the crypto is being sent from
checksum_dev_wallet = Web3.toChecksumAddress('0x6128fA913be3721Ef1C437151e92be0255a6afe8')
print("checksum_dev_wallet:",checksum_dev_wallet)

# enter a list of accounts that the crypto is being sent to
to_addresses = ['0x86e3EaEc906f157B281056E44AC50FaE8f9549cb']

# Reward Token
moon_address = '0x047a02a57501a813975b2D347278Fdd3dF671E86'
apikeytoken = '9G16ZJCZ8JDVSFGU2UPHJ1HW1F8ZIP7ZYD'


contract_address = web3.toChecksumAddress(moon_address)
print("contract_address:",contract_address)
API_ENDPOINT = url_eth + '?module=contract&action=getabi&address=' + str(contract_address) + "&apikey=" + str(apikeytoken)
print("API_ENDPOINT:", API_ENDPOINT)

weather = urlopen(API_ENDPOINT).read()
weather = weather.decode('utf-8')

abi=json.loads(json.loads(weather)['result'])

print("-------------",abi,"------------------");

token = web3.eth.contract(address=contract_address, abi=abi) # declaring the token contract
token_balance = token.functions.balanceOf(checksum_dev_wallet).call() / 10**18
print("token_balance:",token_balance)


# loop through each of the to_addresses and send Ether in the amount designated below
nonce = web3.eth.getTransactionCount(checksum_dev_wallet)
print("nonce:",nonce)
for dest_address in to_addresses:
    checksum_dest_wallet = Web3.toChecksumAddress(dest_address)
    send_amount = int(0.00001*(10**18))
    print(send_amount, "********************************Send amount********************************")

    try:
        contract_method_transferToken = token.functions.transfer(checksum_dest_wallet, send_amount)
        contract_method_transferToken_build_tx = contract_method_transferToken.buildTransaction({
            'nonce': nonce,
            'from': checksum_dev_wallet,
            'gas': 210000,
            'value': 0,
            'gasPrice': web3.eth.gas_price
        })

        print(checksum_dest_wallet,"-",contract_method_transferToken_build_tx)

        bsc_sign_tx_transferToken = web3.eth.account.signTransaction(contract_method_transferToken_build_tx, private_key = PRIVATE_KEY)

        print("----------------",bsc_sign_tx_transferToken,"-----------------------")
        bscTxHash = web3.eth.sendRawTransaction(bsc_sign_tx_transferToken.rawTransaction)

        print("----------------",bscTxHash,"-----------------------")
        print('tx_hash:', web3.toHex(bscTxHash), '-', checksum_dest_wallet, ' : ', send_amount,'2022M')
    
    except Exception as e:
        print('error:', e)
