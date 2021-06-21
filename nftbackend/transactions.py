from django.conf import settings
import web3

from .models import Claimant

ERC1155_TRANSFER_ABI = [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_tokenId",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_value",
				"type": "uint256"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	}
]


ERC721_TRANSFER_ABI = [
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_tokenId",
				"type": "uint256"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	}
]

def execute_claim(claimant: Claimant) -> str:
    web3.Account.enable_unaudited_hdwallet_features()
    w3 = web3.Web3(web3.HTTPProvider(settings.ETH_RPC_URL))
    signer : web3.Account = web3.Account.from_mnemonic(settings.ETH_MNEMONIC)
    w3.eth.default_account = signer._address

    abi = ERC721_TRANSFER_ABI if claimant.whitelist.nft.contract_type == "721" else ERC1155_TRANSFER_ABI

    contract = w3.eth.contract(abi=abi, address=claimant.whitelist.nft.contract_address)
    nonce = w3.eth.get_transaction_count(signer._address)

    tx = contract.functions.safeTransferFrom(signer._address, claimant.address, claimant.whitelist.nft.token_id).buildTransaction({
        "nonce": nonce
    })
    signed_tx = signer.sign_transaction(tx)
    w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return w3.toHex(signed_tx.hash)
