from web3 import Web3 

# Infura url key from infura Website. 

infura_url = "https://mainnet.infura.io/v3/e0ffef02fc8b4a7c8a9993d28dcdd878"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if we are connected to the Eth block chain. 
print(web3.isConnected())

# print blockNumber 
print(web3.eth.blockNumber)

# MetaMask Wallet address 
balance = web3.eth.getBalance("0x0fc5Bb8e76BDEaAa5e27e85122A348a40618EFb1")
print(web3.fromWei(balance, "ether"))
