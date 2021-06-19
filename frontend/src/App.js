import './App.css';

import MetamaskConnector from './connectors'
import React from 'react';
import { useWeb3React } from '@web3-react/core';

import {
  Container,
  Navbar,
  Tabs,
  Tab
} from 'react-bootstrap'

import WhitelistSigning from './components/WhitelistSigning';
import WhitelistCreation from './components/WhitelistCreation';
import NFTClaimList from './components/NFTClaimList';

function App() {
  const { activate } = useWeb3React()
  React.useEffect(() => {
    activate(MetamaskConnector, (err) => alert(err))
  }, [activate])

  return (
    <>
      <Navbar>
        <Navbar.Brand>
          test
        </Navbar.Brand>
      </Navbar>
      <Container>
        <Tabs defaultActiveKey="sign">
          <Tab eventKey="sign" title="Sign">
            <WhitelistSigning />
          </Tab>
          <Tab eventKey="register" title="Register NFT">
            <WhitelistCreation />
          </Tab>
          <Tab eventKey="claim" title="Claim NFT">
            <NFTClaimList />
          </Tab>
        </Tabs>
      </Container>
    </>
  );
}

export default App;
