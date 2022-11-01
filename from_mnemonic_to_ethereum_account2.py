{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# From Mnemonic to Ethereum Account \n",
    "\n",
    "In this activity, you will use the mnemonic, bip44, and Web3.py libraries to generate a wallet instance and a new, secure public-private key phrase from a mnemonic seed phrase.\n",
    "\n",
    "## Instructions\n",
    "\n",
    "Complete each of the following steps:\n",
    "\n",
    "1. Import the following dependencies:\n",
    "\n",
    "   * Import `os`.\n",
    "   \n",
    "   * From `dotenv` import `load_dotenv` and then call `load_dotenv`.\n",
    "\n",
    "   * From `bip44` import `Wallet`.\n",
    "\n",
    "   * From `mnemonic` import `Mnemonic`.\n",
    "\n",
    "   * From `web3` import `Account`.\n",
    "\n",
    "2. Remember that you don't want to generate a new mnemonic every time you run the program, because then you'll lose access to your previous mnemonic and subsequently your private key. If you have not already generated a mnemonic seed phrase and saved it to a `.env` file associated with this activity, you will need to generate one now.  \n",
    "\n",
    "If you already have a mnemonic phrase that you would like to use for this activity, complete the following step:\n",
    "   * Create a `.env` file in the same folder as the Jupyter notebook, and set the mnemonic phrase equal to an environment variable named `MNEMONIC`. \n",
    "\n",
    "If you do not already have a mnemonic seed phrase that you would like to use for this activity, create one by completing the following steps:\n",
    "\n",
    "   * Call `os.getenv(\"MNEMONIC\")`, and save its value as a variable named `mnemonic`.\n",
    "\n",
    "   * Use an `if` statement to check if the mnemonic variable is `None`.\n",
    "\n",
    "   * If the mnemonic variable is `None`, initialize a new `Mnemonic()` instance and pass it a string value of “english” so that it will use the English word list. Save the instance as a variable named `mnemo`. Next, generate your mnemonic seed phrase by creating a variable named `mnemonic` and calling `mnemo.generate(strength=128)`. Finally, print out the mnemonic phrase.\n",
    "\n",
    "   * Create a `.env` file in the same folder as the Jupyter notebook, and create an environment variable named `MNEMONIC`. Copy the new mnemonic seed phrase that you just generated and set it equal to the `MNEMONIC` variable.\n",
    "\n",
    "3. Generate a `Wallet` instance using your `mnemonic` variable and the bip44 package.\n",
    "\n",
    "   * Instantiate a new instance of the `Wallet()` class from the bip44 package, and pass it your `mnemonic` variable to create a universal wallet instance. Save the wallet instance to a variable named `wallet`.\n",
    "\n",
    "4. Derive public and private keys from your `wallet` instance. To do so, complete the following steps:\n",
    "\n",
    "   * Create two variables, `public` and `private`, and set their values by calling the `derive_account` method on your wallet instance. In order to associate the account with Ethereum, pass the string “eth” to the `derive_account` method.\n",
    "\n",
    "   * Create a new variable named `account`, and construct the Ethereum account by calling `Account.privateKeyToAccount` and passing it your private key variable.\n",
    "\n",
    "   * Call `account.address` to access the address associated with your new Ethereum account. By using this address, other participants can send you ether on the Ethereum blockchain.\n",
    "\n",
    "## References\n",
    "\n",
    "[Web3.py](https://web3py.readthedocs.io/en/stable/)\n",
    "\n",
    "[mnemonic](https://pypi.org/project/mnemonic/)\n",
    "\n",
    "[bip44](https://pypi.org/project/bip44/)\n",
    "\n",
    "[Ethereum](https://ethereum.org/en/developers/docs/)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1: Import the following dependencies:\n",
    "\n",
    "   * Import `os`.\n",
    "   \n",
    "   * From `dotenv` import `load_dotenv` and then call `load_dotenv`.\n",
    "\n",
    "   * From `bip44` import `Wallet`.\n",
    "\n",
    "   * From `mnemonic` import `Mnemonic`.\n",
    "\n",
    "   * From `web3` import `Account`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Imports\n",
    "import os\n",
    "from dotenv import load_dotenv\n",
    "load_dotenv()\n",
    "from mnemonic import Mnemonic\n",
    "from bip44 import Wallet\n",
    "from web3 import Account"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2: If you do not already have a mnemonic seed phrase that you would like to use for this activity, create one by completing the following steps:\n",
    "\n",
    "   * Call `os.getenv(\"MNEMONIC\")`, and save its value as a variable named `mnemonic`.\n",
    "\n",
    "   * Use an `if` statement to check if the mnemonic variable is `None`.\n",
    "\n",
    "   * If the mnemonic variable is `None`, initialize a new `Mnemonic()` instance and pass it a string value of “english” so that it will use the English word list. Save the instance as a variable named `mnemo`. Next, generate your mnemonic seed phrase by creating a variable named `mnemonic` and calling `mnemo.generate(strength=128)`. Finally, print out the mnemonic phrase.\n",
    "\n",
    "   * Create a `.env` file in the same folder as the Jupyter notebook, and create an environment variable named `MNEMONIC`. Copy the new mnemonic seed phrase that you just generated and set it equal to the `MNEMONIC` variable.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'soda entire hockey borrow flock sugar regular amount vast evolve protect drink hello industry skate tape way physical nothing leave cycle flock shop scene'"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Call os.getenv(\"MNEMONIC\") and save it's value as a variable named mnemonic\n",
    "mnemonic = os.getenv(\"MNEMONIC\")\n",
    "\n",
    "# Use an if-statement to check if the mnemonic variable is None\n",
    "if mnemonic is None:\n",
    "\n",
    "    # If the mnemonic variable is none, initialize a new instance of Mnemonic\n",
    "    # pass it a string value of english to use the english word list\n",
    "    # Save the instance as a variable named mnemo\n",
    "    mnemo = Mnemonic(\"english\")  \n",
    "    \n",
    "    # Call mnemo.generate(strength=256) and set it equal to the variable mnemonic \n",
    "    mnemonic = mnemo.generate(strength=256)\n",
    "    \n",
    "# Review the mnemonic seed phrase\n",
    "display(mnemonic)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a `.env` file in the same folder as the Jupyter notebook, and create an environment variable named `MNEMONIC`. Copy the new mnemonic seed phrase that you just generated and set it equal to the `MNEMONIC` variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Generate a `Wallet` instance using your `mnemonic` variable and the bip44 package.\n",
    "\n",
    "   * Instantiate a new instance of the `Wallet` class from the bip44 package, and pass it your `mnemonic` variable to create a universal wallet instance. Save the wallet instance to a variable named `wallet`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bip44.wallet.Wallet at 0x10fd33c50>"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Instantiate a new instance of Wallet and pass it the mnemonic variable\n",
    "wallet = Wallet(mnemonic)\n",
    "\n",
    "# Review your wallet instance\n",
    "wallet"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4: Derive public and private keys from your `wallet` instance. To do so, complete the following steps:\n",
    "\n",
    "   * Create two variables, `public` and `private`, and set their values by calling the `derive_account` method on your wallet instance. In order to associate the account with Ethereum, pass the string “eth” to the `derive_account` method.\n",
    "\n",
    "   * Create a new variable named `account`, and construct the Ethereum account by calling `Account.privateKeyToAccount` and passing it your private key variable.\n",
    "\n",
    "   * Call `account.address` to access the address associated with your new Ethereum account. By using this address, other participants can send you ether on the Ethereum blockchain.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#PRIVATE KEYS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b\"\\x04T\\xa0y\\xfa,\\x11\\t\\xbb\\x06RX\\x0c\\x85'VL\\x7f$\\x83@s/\\x90\\xe0p\\x9e\\xb3\\xc9\\xf8i0\""
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calling the derive_account method on your wallet instance\n",
    "# Pass the string eth to the method\n",
    "private, public = wallet.derive_account(\"eth\")\n",
    "\n",
    "# Review the byte string of your private key\n",
    "private"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Construct the Ethereum account by calling Account.privateKeyToAccount\n",
    "# Pass it your private key variable\n",
    "account = Account.privateKeyToAccount(private)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'0x670c38e67170C99844520Aae78D14e5772934D43'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Call account.address to access the address associated with your new Ethereum account\n",
    "account.address"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "HexBytes('0x0454a079fa2c1109bb0652580c8527564c7f248340732f90e0709eb3c9f86930')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Bonus:\n",
    "\n",
    "# Call account.privateKey to access the private key associated with your new Ethereum account\n",
    "account.privateKey"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Signing and Verifying Messages with Web3.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "from web3.auto import w3\n",
    "from eth_account.messages import encode_defunct"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SignableMessage(version=b'E', header=b'thereum Signed Message:\\n19', body=b'Zach owes David $20')"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Now that we’ve written our message, we need to encode it from a text format into a byte format. In a byte format, \n",
    "#the message can be read by computers and signed by our private key.\n",
    "\n",
    "msg = \"Zach owes David $20\"\n",
    "message = encode_defunct(text=msg)\n",
    "message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SignedMessage(messageHash=HexBytes('0xb4aac7e826ed228d4aca4c19e090daf7744dcab152eb82450b3493e6d8b1e9e2'), r=25111491636413753485033993269225444744270998608691558470853548403288255904694, s=54517193004044677187276730162331122421249744499662329287365465507352462653359, v=28, signature=HexBytes('0x378499c04ea5bb054c8de5ce41759c90ecc69dc1c93e7b7835bd1e55361a3bb67887a344169181c206cbb2b646c861c42e7d4d65d06aa6093243ee1157d277af1c'))"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Now, our message is ready to be signed. We'll use the w3.eth.account.sign_message function to sign our message. \n",
    "#This function accepts our message as the first argument and our private key as an argument named private_key.\n",
    "#Then it returns the encoded, signed message.The following code signs our message:\n",
    "\n",
    "signed_message = w3.eth.account.sign_message(message, private_key=private)\n",
    "signed_message"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Notice that the SignedMessage object consists of several parts. \n",
    "#The signature itself consists of a HexBytesLinks to an external site. \n",
    "#hash code. And together, the r, s, and v variables that the object \n",
    "#contains can be used to independently verify the signature."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#PUBLIC KEY "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'0x670c38e67170C99844520Aae78D14e5772934D43'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "w3.eth.account.recover_message(message, signature=signed_message.signature)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Imports\n",
    "import os\n",
    "from dotenv import load_dotenv\n",
    "load_dotenv()\n",
    "from bip44 import Wallet\n",
    "from web3 import Account\n",
    "from web3 import Web3\n",
    "w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "mnemonic = os.getenv(\"MNEMONIC\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b'\\x03\\x9e\\xd4\\xb8IrMR\\x03\\xaa\\x89d\\xec\\xef\\xb0)\\x01.\\xea\\x15\\x98Wh8\\x99\\xea\\xb4f\\xdb\\xd7\\xf2\\xd5\\xa7'"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "private, public = wallet.derive_account(\"eth\")\n",
    "public"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0x670c38e67170C99844520Aae78D14e5772934D43\n"
     ]
    }
   ],
   "source": [
    "account = Account.privateKeyToAccount(private)\n",
    "account_address = account.address\n",
    "print(account_address)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Access the balance of funds for the Ethereum account\n",
    "wei_balance = w3.eth.getBalance(account_address)\n",
    "\n",
    "# Convert the balance from a denomination in wei to ether\n",
    "ether = w3.fromWei(wei_balance, \"ether\")\n",
    "\n",
    "# Print the number of ether\n",
    "ether"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Signing Transactions with Web3.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Imports\n",
    "import os\n",
    "from dotenv import load_dotenv\n",
    "load_dotenv()\n",
    "from bip44 import Wallet\n",
    "from eth_account import Account\n",
    "from web3 import middleware\n",
    "from web3.gas_strategies.time_based import medium_gas_price_strategy\n",
    "from web3 import Web3\n",
    "w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "#CREATE THE TRANSACTION \n",
    "\n",
    "\n",
    "amount = .0001\n",
    "value = w3.toWei(amount, \"ether\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "#We'll define a new variable, receiver, and set it to the Ethereum address where we want to send our funds\n",
    "\n",
    "receiver = \"0x4b0d14BDD1E41dAdD15B66EEB7D7c454aD19A0af\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "#NOTE \n",
    "#These steps were familiar from earlier in the module. Now, we’re going to add something new. \n",
    "#Once we have defined how much ether to send and where to send it, \n",
    "#we need to configure the estimate of our gas price, or the gasEstimate.\n",
    "\n",
    "#Before we configure our gasEstimate, we first have to set a gas price strategy. \n",
    "#The setGasPriceStrategy function from Web3.pyLinks to an external site. constructs \n",
    "#a strategy that will compute a gas price such that the transaction is likely to be\n",
    "#mined within a specific amount of time. The gas price is computed by reviewing the \n",
    "#gas prices of the most recently mined blocks.\n",
    "\n",
    "#For this example, we will use the medium gas price strategy, which aims to have the \n",
    "#transaction mined within five minutes. Compare this to the following:\n",
    "\n",
    "#a fast_gas_price_strategy, which aims to have a transaction mined within one minute\n",
    "\n",
    "#a slow_gas_price_strategy, which aims to have a transaction mined within one hour\n",
    "\n",
    "#a glacial_gas_price_strategy, which aims to have a transaction mined within one day\n",
    "\n",
    "#We set the strategy by calling a function that is built into Web3.py: w3.eth.setGasPriceStrategy(medium_gas_price_strategy). \n",
    "#The following code shows this step:\n",
    "\n",
    "# Set the gas price strategy\n",
    "w3.eth.setGasPriceStrategy(medium_gas_price_strategy)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "String value expected",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/y2/8cwcjfb153g95p1_q65w3kkc0000gn/T/ipykernel_4350/4275033692.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mmnemonic\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgetenv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"MNEMONIC\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mwallet\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mWallet\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmnemonic\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0mprivate\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpublic\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwallet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mderive_account\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"eth\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0maccount\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mAccount\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprivateKeyToAccount\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprivate\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/site-packages/bip44/wallet.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, mnemonic, language, passphrase)\u001b[0m\n\u001b[1;32m     18\u001b[0m         \u001b[0;34m:\u001b[0m\u001b[0mparam\u001b[0m \u001b[0mpassphrase\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moptional\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mThe\u001b[0m \u001b[0mmnemonic\u001b[0m\u001b[0;31m'\u001b[0m\u001b[0ms\u001b[0m \u001b[0mpassphrase\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     19\u001b[0m         \"\"\"\n\u001b[0;32m---> 20\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_seed\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mMnemonic\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlanguage\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mto_seed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmnemonic\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpassphrase\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_bip32\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mBIP32\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfrom_seed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_seed\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/site-packages/mnemonic/mnemonic.py\u001b[0m in \u001b[0;36mto_seed\u001b[0;34m(cls, mnemonic, passphrase)\u001b[0m\n\u001b[1;32m    232\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mclassmethod\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    233\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mto_seed\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmnemonic\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpassphrase\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0mbytes\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 234\u001b[0;31m         \u001b[0mmnemonic\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnormalize_string\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmnemonic\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    235\u001b[0m         \u001b[0mpassphrase\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnormalize_string\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpassphrase\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    236\u001b[0m         \u001b[0mpassphrase\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"mnemonic\"\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mpassphrase\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/site-packages/mnemonic/mnemonic.py\u001b[0m in \u001b[0;36mnormalize_string\u001b[0;34m(txt)\u001b[0m\n\u001b[1;32m     98\u001b[0m             \u001b[0mutxt\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtxt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     99\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 100\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"String value expected\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    101\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    102\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0municodedata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnormalize\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"NFKD\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mutxt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: String value expected"
     ]
    }
   ],
   "source": [
    "#Now that we have set a gas price strategy, we should be able to estimate the gas that it will take to send our transaction.\n",
    "#For this step we will need the variables we've defined for our transaction so far:\n",
    "\n",
    "\n",
    "mnemonic = os.getenv(\"MNEMONIC\")\n",
    "wallet = Wallet(mnemonic)\n",
    "private, public = wallet.derive_account(\"eth\")\n",
    "account = Account.privateKeyToAccount(private)\n",
    "account_address = account.address\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "#We call w3.eth.estimateGas. We’ll pass it an object constructed with our variables. \n",
    "#This will return a value for our gas estimate, which we’ll save as a variable named gasEstimate. \n",
    "#The following code shows this step:\n",
    "\n",
    "# Calculate the gas estimate\n",
    "gasEstimate = w3.eth.estimateGas(\n",
    "    {\"to\": receiver,\n",
    "     \"from\": account_address,\n",
    "     \"value\": value\n",
    "    }\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create the transaction object\n",
    "raw_tx = {\n",
    "    \t\"to\": receiver,\n",
    "    \t\"from\": account_address,\n",
    "    \t\"value\": value,\n",
    "    \t\"gas\": gasEstimate,\n",
    "    \t\"gasPrice\": 0,\n",
    "    \t\"nonce\": w3.eth.getTransactionCount(account.address)\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "{'message': \"sender doesn't have enough funds to send tx. The upfront cost is: 100000000000000 and the sender's account only has: 0\", 'code': -32000, 'data': {'stack': \"Error: sender doesn't have enough funds to send tx. The upfront cost is: 100000000000000 and the sender's account only has: 0\\n    at VM.<anonymous> (/Volumes/Ganache 2.5.4/Ganache.app/Contents/Resources/static/node/node_modules/ganache-core/node_modules/ethereumjs-vm/lib/runTx.ts:114:11)\\n    at step (/Volumes/Ganache 2.5.4/Ganache.app/Contents/Resources/static/node/node_modules/ganache-core/node_modules/ethereumjs-vm/dist/runTx.js:33:23)\\n    at Object.next (/Volumes/Ganache 2.5.4/Ganache.app/Contents/Resources/static/node/node_modules/ganache-core/node_modules/ethereumjs-vm/dist/runTx.js:14:53)\\n    at fulfilled (/Volumes/Ganache 2.5.4/Ganache.app/Contents/Resources/static/node/node_modules/ganache-core/node_modules/ethereumjs-vm/dist/runTx.js:5:58)\\n    at runMicrotasks (<anonymous>)\\n    at processTicksAndRejections (internal/process/task_queues.js:93:5)\", 'name': 'Error'}}",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/y2/8cwcjfb153g95p1_q65w3kkc0000gn/T/ipykernel_4350/1755538058.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# Route the signed transaction to the Ethereum blockchain\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mw3\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0meth\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msendRawTransaction\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msigned_tx\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrawTransaction\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/site-packages/web3/module.py\u001b[0m in \u001b[0;36mcaller\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m     56\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mLogFilter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0meth_module\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mmodule\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfilter_id\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfilter_id\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m         \u001b[0mresult_formatters\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merror_formatters\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse_formatters\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 58\u001b[0;31m         \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mw3\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmanager\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrequest_blocking\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmethod_str\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merror_formatters\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     59\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mapply_result_formatters\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresult_formatters\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     60\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mcaller\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/dev/lib/python3.7/site-packages/web3/manager.py\u001b[0m in \u001b[0;36mrequest_blocking\u001b[0;34m(self, method, params, error_formatters)\u001b[0m\n\u001b[1;32m    156\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;34m\"error\"\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    157\u001b[0m             \u001b[0mapply_error_formatters\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0merror_formatters\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 158\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"error\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    159\u001b[0m         \u001b[0;32melif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'result'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    160\u001b[0m             \u001b[0mapply_error_formatters\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0merror_formatters\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mValueError\u001b[0m: {'message': \"sender doesn't have enough funds to send tx. The upfront cost is: 100000000000000 and the sender's account only has: 0\", 'code': -32000, 'data': {'stack': \"Error: sender doesn't have enough funds to send tx. The upfront cost is: 100000000000000 and the sender's account only has: 0\\n    at VM.<anonymous> (/Volumes/Ganache 2.5.4/Ganache.app/Contents/Resources/static/node/node_modules/ganache-core/node_modules/ethereumjs-vm/lib/runTx.ts:114:11)\\n    at step (/Volumes/Ganache 2.5.4/Ganache.app/Contents/Resources/static/node/node_modules/ganache-core/node_modules/ethereumjs-vm/dist/runTx.js:33:23)\\n    at Object.next (/Volumes/Ganache 2.5.4/Ganache.app/Contents/Resources/static/node/node_modules/ganache-core/node_modules/ethereumjs-vm/dist/runTx.js:14:53)\\n    at fulfilled (/Volumes/Ganache 2.5.4/Ganache.app/Contents/Resources/static/node/node_modules/ganache-core/node_modules/ethereumjs-vm/dist/runTx.js:5:58)\\n    at runMicrotasks (<anonymous>)\\n    at processTicksAndRejections (internal/process/task_queues.js:93:5)\", 'name': 'Error'}}"
     ]
    }
   ],
   "source": [
    "# Create a signed transaction by passing the transaction object\n",
    "# into the signTransaction function\n",
    "signed_tx = account.signTransaction(raw_tx)\n",
    "\n",
    "# Route the signed transaction to the Ethereum blockchain\n",
    "w3.eth.sendRawTransaction(signed_tx.rawTransaction)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
