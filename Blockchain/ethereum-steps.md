# Steps for Ethereum
## Create a new dir - 
```
mkdir gethdata
```

## Create few accounts
```
geth account new --datadir gethdata
```

> b1ff0a9b446096049d72bbd677b1ae0734db0693
```
geth account new --datadir gethdata
```
> eb258606d2779567cd0bd96c6652ccd267ff584a


## Update the genesis block with the seed accounts 
genesis.json - update the allocation using the account/ accounts generated above
```
{
  "config": {
    "chainId": 15,
    "homesteadBlock": 0,
    "eip155Block": 0,
    "eip158Block": 0
  },

   "coinbase"   : "0x0000000000000000000000000000000000000000",
  "difficulty" : "0x400",
  "extraData"  : "",
  "gasLimit"   : "0x2fefd8",
  "nonce"      : "0x0000000000000042",
  "mixhash"    : "0x0000000000000000000000000000000000000000000000000000000000000000",
  "parentHash" : "0x0000000000000000000000000000000000000000000000000000000000000000",
  "timestamp"  : "0x00",
  	"alloc":{
	        "b1ff0a9b446096049d72bbd677b1ae0734db0693": {
			"balance": "130000000"
		},
		"eb258606d2779567cd0bd96c6652ccd267ff584a": {
			"balance": "1400000"
		}
	}
}
```

## Initiate the chain -- pass the data directory and the genesis block
```
geth --datadir ./gethdata init ./gethdata/genesis.json
```
## Once the chain is initialized , run it using , unlock only if you need an account unlocked -
```
geth --identity "nodeA" --rpccorsdomain "*" --datadir=./geth-amalto -verbosity 6 --port 30303  --rpc  --rpcapi=eth,web3,net,debug,shh,personal --rpcvhosts=*  --wsapi=eth,web3,net,shh,debug,pubsub,personal  --rpcaddr localhost --rpcport 8545  --networkid 15 --ws --wsport=8546 --maxpeers=0   --nodiscover --mine --minerthreads 1 --unlock "abf41a21448dee7edcf44fa76bd847a59b3f38a5" console
```

## With metamask extension integration
```
geth --identity "nodeA" --rpccorsdomain "*" --datadir=./geth-amalto -verbosity 6 --port 30303  --rpc  --rpcapi=eth,web3,net,debug,shh,personal --rpcvhosts=*  --wsapi=eth,web3,net,shh,debug,pubsub,personal  --rpcaddr localhost --rpcport 8545  --networkid 15 --ws --wsport=8546 --maxpeers=0   --nodiscover --mine --minerthreads 1 --unlock "abf41a21448dee7edcf44fa76bd847a59b3f38a5" --rpccorsdomain="chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn 
```

## Attach a terminal to a running geth node
```
geth attach http://127.0.0.1:8545
```

## to get the coinbase
eth.coinbase

## to get the balance of an account
web3.fromWei(eth.getBalance(eth.coinbase), "ether")


https://medium.com/cybermiles/running-a-quick-ethereum-private-network-for-experimentation-and-testing-6b1c23605bce