import json
import argparse
import threading
from web3 import Web3
from progress.bar import IncrementalBar

parser = argparse.ArgumentParser()

parser.add_argument(
    "--contract", type=str,
    default="0x15F4272460062b835Ba0abBf7A5E407F3EF425d3",
    dest="address", help="contract address",
)
parser.add_argument("--output", type=str, default="snapshot.csv", dest="output", help="output file")
parser.add_argument("--max", type=int, default=1, dest="max_claimable", help="max claimable")
parser.add_argument("--abi", type=str, default="thirdweb.json", dest="abi")

args = parser.parse_args()

if args.abi.endswith(".json"):
    with open(args.abi, "r") as f:
        abi = json.load(f)
else:
    raise Exception("Invalid ABI file")


w3 = Web3(Web3.HTTPProvider("https://polygon.rpc.thirdweb.com"))
contract = w3.eth.contract(args.address, abi=abi)

suply = int(contract.functions.totalSupply().call())
print("Total supply: ", suply)

bar = IncrementalBar("Processing", max=suply)


def get_owner(i):
    owner = contract.functions.ownerOf(i).call()
    if owner not in owners:
        owners.append(owner)
    bar.next()


owners = []
threads = []
for i in range(0, suply):
    t = threading.Thread(target=get_owner, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

with open(args.output, "w") as f:
    f.write("address,maxClaimable\n")
    for owner in owners:
        f.write(f"{owner},{args.max_claimable}\n")

print("\nSaved to", args.output)
