import React from 'react'
import axios from 'axios'

import NFTClaimCard from './NFTClaimCard'

export default function NFTClaimList() {
    const [NFTList, setNFTList] = React.useState([])

    React.useEffect(() => {
        axios.get(process.env.REACT_APP_API_URL + "/nfts", {mode: 'no-cors'}).then(
            response => setNFTList(() => response.data)
        )
    }, [setNFTList])

    return (
        <ul>
            {NFTList.map(nft => <NFTClaimCard key={nft.id} nft={nft} />)}
        </ul>
    )
}