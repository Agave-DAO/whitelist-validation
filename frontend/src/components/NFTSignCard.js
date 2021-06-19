import { useWeb3React } from '@web3-react/core'
import React from 'react'
import axios from 'axios'
import { Card, Button, Alert } from 'react-bootstrap'

export default function NFTSignCard({nft}) {
    const [ error, setError ] = React.useState("")
    const { library, account } = useWeb3React()

    const signWhitelist = React.useCallback(() => {
        const signer = library.getSigner()

        console.log(nft.whitelist.whitelist_file)

        axios.get(nft.whitelist.whitelist_file).then(response => {
            signer.signMessage(response.data).then(signature => {
                axios.post(process.env.REACT_APP_API_URL + "/sign/", {
                    signer: account,
                    signature: signature,
                    whitelist: nft.whitelist.id
                }).then(() => {
                    alert("Successfully signed!")
                }).catch(err => {
                    setError(`Failed to sign: ${err.response.data.non_field_errors}`)
                })
            })
        })
    }, [setError, account, library, nft])

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
                <Button onClick={signWhitelist}>Sign this whitelist</Button>
            </Card.Footer>
        </Card>
    )
}