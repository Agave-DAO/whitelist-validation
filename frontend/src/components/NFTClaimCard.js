import { useWeb3React } from '@web3-react/core'
import React from 'react'
import axios from 'axios'
import { Card, Button, Alert } from 'react-bootstrap'

export default function NFTClaimCard({nft}) {
    const [ error, setError ] = React.useState("")
    const { account } = useWeb3React()

    function claim() {
        return axios.post(process.env.REACT_APP_API_URL + `/nfts/${nft.id}/claim/`, {
            address: account
        }).then(() => console.log("success")).catch(e => setError(e.toString()))
    }


    return (
        <Card>
            <Card.Header>
                NFT #{nft.id}
            </Card.Header>
            <Card.Body>
                <p>ID #{nft.token_id} on contract {nft.contract_address}</p>
                <p><a href={nft.whitelist.whitelist_file}>See the whitelist</a></p>
            </Card.Body>
            <Card.Footer>
                {error?<Alert variant="danger">{error}</Alert>:""}
                <Button onClick={claim}>Claim this NFT</Button>
            </Card.Footer>
        </Card>
    )
}