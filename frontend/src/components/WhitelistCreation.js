import { useWeb3React } from '@web3-react/core'
import axios from 'axios'
import React from 'react'
import {
    Form,
    Button,
} from 'react-bootstrap'

export default function WhitelistCreation() {
    const { library } = useWeb3React()
    const [address, setAddress] = React.useState("")
    const [tokenID, setTokenID] = React.useState(0)
    const [whitelistData, setWhitelistData] = React.useState("")

    const submit = () => {
        console.log(address, tokenID, whitelistData)
        const formData = new FormData()
        const whitelistDataFile = new File([whitelistData], "whitelist.txt")

        formData.append('contract_address', address)
        formData.append('token_id', tokenID)
        formData.append('whitelist.whitelist_file', whitelistDataFile)

        axios.post(process.env.REACT_APP_API_URL + "/nfts/", formData, {
            headers: {
                "Content-Type": "multipart/form-data"
            }
        }).then(() => alert("successfully uploaded whitelist")).catch(console.error)
    }

    return (
        <Form>
            <Form.Group controlId="formContractAddress">
                <Form.Label>Contract address</Form.Label>
                <Form.Control onChange={evt => setAddress(evt.target.value)}></Form.Control>
            </Form.Group>
            <Form.Group controlId="formTokenID">
                <Form.Label>Token ID</Form.Label>
                <Form.Control type="number" onChange={evt => setTokenID(evt.target.value)}></Form.Control>
            </Form.Group>
            <Form.Group controlId="formWhitelist">
                <Form.Label>Whitelist Data</Form.Label>
                <Form.Control as="textarea" onChange={evt => setWhitelistData(evt.target.value)}></Form.Control>
            </Form.Group>
            <Button onClick={submit}>
                Submit
            </Button>
        </Form>
    )
}