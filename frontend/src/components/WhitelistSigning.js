import React from 'react'
import axios from 'axios'

import NFTSignCard from './NFTSignCard'

export default function WhitelistSigning() {
    const [NFTs, setNFTs] = React.useState([])

    React.useEffect(() => {
        axios.get(process.env.REACT_APP_API_URL + "/nfts", {mode: 'no-cors'}).then(
            response => setNFTs(() => response.data)
        )
    }, [setNFTs])

    return (
        <ol>
            {NFTs.map(nft => <NFTSignCard nft={nft} key={nft.id}/>)}
        </ol>
    )
}