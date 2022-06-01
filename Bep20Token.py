from web3 import Web3
import time
import json
import requests

# enter your private key.  Be careful with your private key
PRIVATE_KEY = "YOUR PRIVATE_KEY"

# add your blockchain connection information
url_eth = 'https://api-testnet.bscscan.com/api'
bsc = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

# enter the account that the crypto is being sent from
checksum_dev_wallet = Web3.toChecksumAddress('0x6128fA913be3721Ef1C437151e92be0255a6afe8')
print("checksum_dev_wallet:",checksum_dev_wallet)

# enter a list of accounts that the crypto is being sent to
to_addresses = ['0x86e3EaEc906f157B281056E44AC50FaE8f9549cb']

# Reward Token
moon_address = '0xFEB814fd2c240E1a8F71f6EAc0630E4bd56E96F2'
# apikeytoken = '9G16ZJCZ8JDVSFGU2UPHJ1HW1F8ZIP7ZYD'


contract_address = web3.toChecksumAddress(moon_address)
print("contract_address:",contract_address)
API_ENDPOINT = url_eth + '?module=contract&action=getapi&address=' + str(contract_address)
print("API_ENDPOINT:", API_ENDPOINT)

r = requests.get(url = API_ENDPOINT)
response = r.json()
abi=json.loads(response['result'])
# abi = "[{\"inputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Approval\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"previousOwner\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"OwnershipTransferred\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"address\",\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"internalType\":\"address\",\"name\":\"to\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Transfer\",\"type\":\"event\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"owner\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"}],\"name\":\"allowance\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"approve\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"}],\"name\":\"balanceOf\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"burn\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"account\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"burnFrom\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"decimals\",\"outputs\":[{\"internalType\":\"uint8\",\"name\":\"\",\"type\":\"uint8\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"subtractedValue\",\"type\":\"uint256\"}],\"name\":\"decreaseAllowance\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"getOwner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"spender\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"addedValue\",\"type\":\"uint256\"}],\"name\":\"increaseAllowance\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"_mintamount\",\"type\":\"uint256\"}],\"name\":\"mint\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"name\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"owner\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"renounceOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"symbol\",\"outputs\":[{\"internalType\":\"string\",\"name\":\"\",\"type\":\"string\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"name\":\"totalSupply\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"transfer\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"sender\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"recipient\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"name\":\"transferFrom\",\"outputs\":[{\"internalType\":\"bool\",\"name\":\"\",\"type\":\"bool\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"newOwner\",\"type\":\"address\"}],\"name\":\"transferOwnership\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]"


token = web3.eth.contract(address=contract_address, abi=abi) # declaring the token contract
token_balance = token.functions.balanceOf(checksum_dev_wallet).call() / 10**18
print("token_balance:",token_balance)


# loop through each of the to_addresses and send Ether in the amount designated below
nonce = web3.eth.getTransactionCount(checksum_dev_wallet)
print("nonce:",nonce)
for dest_address in to_addresses:
    checksum_dest_wallet = Web3.toChecksumAddress(dest_address)
    send_amount = int(1*(10**18))
    print(send_amount, "********************************Send amount********************************")

    try:
        contract_method_transferToken = token.functions.transfer(checksum_dest_wallet, send_amount)
        contract_method_transferToken_build_tx = contract_method_transferToken.buildTransaction({
            'nonce': nonce,
            'from': checksum_dev_wallet,
            'gas': 100000,
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
