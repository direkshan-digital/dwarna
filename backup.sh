#!/usr/bin/env bash

backup=$( date +%Y%m%d )
mkdir -p backup/$backup

# The Hyperledger Fabric backup copies the admin card and the actual data.
backup_fabric() {
	mkdir -p backup/$1/fabric/dwarna-blockchain
	cp fabric/dwarna-blockchain/admin@dwarna-blockchain.card backup/$1/fabric/dwarna-blockchain

	mkdir -p backup/$1/fabric/fabric-scripts/hlfv12/composer
	cp -r fabric/fabric-scripts/hlfv12/composer/backup_* backup/$1/fabric/fabric-scripts/hlfv12/composer
}

# The REST API backup copies the configuration, including the encryption keys.
backup_rest() {
	mkdir -p backup/$1/rest/config
	cp rest/config/*.py backup/$1/rest/config
}

backup_fabric $backup
backup_rest $backup
