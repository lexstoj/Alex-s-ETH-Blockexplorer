#Imports
from tinyec.ec import SubGroup, Curve

from Crypto.Random.random import randint

from web3 import Web3 

#api
url="https://mainnet.infura.io/v3/e17d484236b74ee5b85d95ccbd854b97"
#connection
w3 = Web3(Web3.HTTPProvider(url))


#1st print statement
print("""
🇦​​​​​🇱​​​​​🇪​​​​​🇽​​​​​'🇸​​​​​ 🇧​​​​​🇱​​​​​🇴​​​​​🇨​​​​​🇰​​​​​🇨​​​​​🇭​​​​​🇦​​​​​🇮​​​​​🇳​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇱​​​​​🇴​​​​​🇷​​​​​🇪​​​​​🇷​​​​​""")
#takes option from user
inpn = int(input("Choose an option, 1. Generate a wallet, 2. Check a transaction hash, 3. get info about a block: "))

#Setting keccak algorithim values
p = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F", 16)
n = int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141", 16)

x = int("79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
y = int("483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)
g = (x,y)
h=1

#plots address graph 
field = SubGroup(p,g,n,h)

curve = Curve(a=0,b=7,field=field,name='secp256k1')
#generates private key
private_key=randint(1,n)
public_key = private_key * curve.g
#generates public key
public_key_hex = Web3.toHex(public_key.x)[2:] + Web3.toHex(public_key.y)[2:]
#generates address
address = Web3.keccak(hexstr=public_key_hex).hex()
address = "0x" + address[-40:]
#checks address
address = Web3.toChecksumAddress(address)
#prints all results to console


if inpn == 1:
  print("""
🇦​​​​​🇱​​​​​🇪​​​​​🇽​​​​​'🇸​​​​​ 🇧​​​​​🇱​​​​​🇴​​​​​🇨​​​​​🇰​​​​​🇨​​​​​🇭​​​​​🇦​​​​​🇮​​​​​🇳​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇱​​​​​🇴​​​​​🇷​​​​​🇪​​​​​🇷​​​​​""")
  print("Address:", address,"\n")

  print("Private key:", private_key,"\n")

  print("Public Key:", public_key_hex,"\n")

  print("Use the public and private key to import the wallet address to your wallet app.")

if inpn == 2: 
  hh = str(input("Enter a hash: \n"))
  checkk = w3.eth.get_transaction_receipt(hh)

  if checkk == "TransactionNotFound":
    print("""
🇦​​​​​🇱​​​​​🇪​​​​​🇽​​​​​'🇸​​​​​ 🇧​​​​​🇱​​​​​🇴​​​​​🇨​​​​​🇰​​​​​🇨​​​​​🇭​​​​​🇦​​​​​🇮​​​​​🇳​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇱​​​​​🇴​​​​​🇷​​​​​🇪​​​​​🇷​​​​​""")
    print("Unconfirmed, check back later.")
  else:
    print("""
🇦​​​​​🇱​​​​​🇪​​​​​🇽​​​​​'🇸​​​​​ 🇧​​​​​🇱​​​​​🇴​​​​​🇨​​​​​🇰​​​​​🇨​​​​​🇭​​​​​🇦​​​​​🇮​​​​​🇳​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇱​​​​​🇴​​​​​🇷​​​​​🇪​​​​​🇷​​​​​​""")
    print("Confirmed")

if inpn == 3:
  block = (int(input("enter the block number: ")))
  checker = w3.eth.get_(block,0)
  print("""
🇦​​​​​🇱​​​​​🇪​​​​​🇽​​​​​'🇸​​​​​ 🇧​​​​​🇱​​​​​🇴​​​​​🇨​​​​​🇰​​​​​🇨​​​​​🇭​​​​​🇦​​​​​🇮​​​​​🇳​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇱​​​​​🇴​​​​​🇷​​​​​🇪​​​​​🇷​​​​​​""")
  print(checker)
