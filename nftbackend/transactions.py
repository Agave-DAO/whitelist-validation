from django.conf import settings
import web3

from .models import Claimant

web3.Account.enable_unaudited_hdwallet_features()
w3 = web3.Web3(web3.HTTPProvider(settings.ETH_RPC_URL))
signer : web3.Account = web3.Account.from_mnemonic(settings.ETH_MNEMONIC)
w3.eth.default_account = signer._address


## ABIs
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

def handle_erc721_claim(claimant: Claimant):
    contract = w3.eth.contract(abi=ERC721_TRANSFER_ABI, address=claimant.whitelist.nft.contract_address)
    nonce = w3.eth.get_transaction_count(signer._address)

    tx = contract.functions.safeTransferFrom(signer._address, claimant.address, claimant.whitelist.nft.token_id).buildTransaction({
        "nonce": nonce
    })
    return tx


def handle_erc1155_claim(claimant: Claimant):
    contract = w3.eth.contract(abi=ERC1155_TRANSFER_ABI, address=claimant.whitelist.nft.contract_address)
    nonce = w3.eth.get_transaction_count(signer._address)

    # TODO value is hardcoded to 1 unit. we might want to airdop more than one, possibly.
    tx = contract.functions.safeTransferFrom(signer._address, claimant.address, claimant.whitelist.nft.token_id, 1).buildTransaction({
        "nonce": nonce
    })
    return tx


def execute_claim(claimant: Claimant) -> str:
    if claimant.whitelist.nft.contract_type == "721":
        raw_transaction = handle_erc721_claim(claimant)
    else:
        raw_transaction = handle_erc1155_claim(claimant)

    signed_tx = signer.sign_transaction(raw_transaction)
    w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return w3.toHex(signed_tx.hash)
