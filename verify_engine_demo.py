import time
import hashlib
import random

print("DEMO VERIFY ENGINE")
print("Pipeline: INPUT → VERIFIED → CERTIFIED → ANCHORED")
print("Anchor Network: Hedera Testnet")
print("-------------------------------------------------")

def verify_cycle():
    start = time.time()

    # simulate verification
    status = "VERIFIED"

    # generate certificate id
    seed = str(random.random()).encode()
    cert_id = hashlib.sha256(seed).hexdigest()[:16]

    # simulated anchor reference
    anchor_ref = cert_id

    runtime = time.time() - start

    print("\n--- Verification Cycle ---")
    print("VERIFY:", status)
    print("CERTIFICATE ID:", cert_id)
    print("ANCHOR NETWORK: Hedera Testnet")
    print("ANCHOR REF:", anchor_ref)
    print("RUNTIME:", round(runtime,6), "seconds")

verify_cycle()
