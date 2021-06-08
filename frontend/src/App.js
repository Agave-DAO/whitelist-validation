import './App.css';

import MetamaskConnector from './connectors'
import React from 'react';
import { useWeb3React } from '@web3-react/core';

import {
  Container,
  Navbar
} from 'react-bootstrap'
import WhitelistSelector from './components/WhitelistSelector';

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
        <WhitelistSelector />
      </Container>
    </>
  );
}

export default App;
