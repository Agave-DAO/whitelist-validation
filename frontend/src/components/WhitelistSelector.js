import React from 'react'
import axios from 'axios'

import NFTCard from './NFTCard'

export default function WhitelistSelector() {
    const [NFTs, setNFTs] = React.useState([])

    React.useEffect(() => {
        axios.get(process.env.REACT_APP_API_URL + "/nfts", {mode: 'no-cors'}).then(
            response => setNFTs(() => response.data)
        )
    }, [setNFTs])

    return (
        <ol>
            {NFTs.map(nft => <NFTCard nft={nft} key={nft.id}/>)}
        </ol>
    )
}