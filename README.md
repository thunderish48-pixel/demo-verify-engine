




# Demo Verify Engine

Lightweight verification pipeline that produces a certificate ID and anchors a verification reference on Hedera Testnet.

## Overview

The Demo Verify Engine demonstrates a simple verification workflow:

INPUT → VERIFIED → CERTIFIED → ANCHORED

The system simulates a verification event, generates a certificate hash, and records a reference suitable for anchoring on a distributed ledger.

## How It Works

1. Input data enters the verification pipeline.
2. The system validates the input.
3. A certificate ID is generated using a cryptographic hash.
4. The verification reference is anchored to Hedera Testnet.

## Demo Output

Example output when running the script:

DEMO VERIFY ENGINE  
Pipeline: INPUT → VERIFIED → CERTIFIED → ANCHORED  
Anchor Network: Hedera Testnet  

--- Verification Cycle 1 ---  
VERIFY: VERIFIED  
CERTIFICATE ID: <generated hash>  
ANCHOR NETWORK: Hedera Testnet  
ANCHOR REF: <hash reference>  
RUNTIME: <execution time>

## Running the Demo

Run the Python script:
