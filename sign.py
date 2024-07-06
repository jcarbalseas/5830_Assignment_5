import eth_account
from web3 import Web3
from eth_account.messages import encode_defunct


# def sign(m):
#     w3 = Web3()
#     # create an eth account and recover the address (derived from the public key) and private key
#     # your code here

#     eth_address = None  # Eth account
#     private_key = None

#     # generate signature
#     # your code here

#     signed_message = None

#     assert isinstance(signed_message, eth_account.datastructures.SignedMessage)

#     return eth_address, signed_message

def sign(m):
    w3 = Web3()

# Create an Ethereum account
    account = w3.eth.account.create()
    eth_address = account.address
    private_key = account.privateKey

# Encode the message
    message = encode_defunct(text=m)

# Sign the message
    signed_message = w3.eth.account.sign_message(message, private_key)

    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)

    return eth_address, signed_message