import hatch_hash
from binascii import unhexlify, hexlify

import unittest

# hatch block #1
# getblockhash 1
# 000008920bf22af181d6fbb50ab127408e8546964902467de1c21e8c011baa8e
# getblock 000008920bf22af181d6fbb50ab127408e8546964902467de1c21e8c011baa8e
# {
#   "hash": "000008920bf22af181d6fbb50ab127408e8546964902467de1c21e8c011baa8e",
#   "confirmations": 71,
#   "size": 179,
#   "height": 1,
#   "version": 536870912,
#   "versionHex": "20000000",
#   "merkleroot": "42a3d6664f57b7fd1a62c412af52b058a00ed06cf99fa05d383672cb8d1e7835",
#   "tx": [
#     "42a3d6664f57b7fd1a62c412af52b058a00ed06cf99fa05d383672cb8d1e7835"
#   ],
#   "time": 1540647179,
#   "mediantime": 1540647179,
#   "nonce": 30038,
#   "bits": "1e0ffff0",
#   "difficulty": 0.000244140625,
#   "chainwork": "0000000000000000000000000000000000000000000000000000000000200020",
#   "previousblockhash": "000000fa6116f5d6c6ce9b60bd431469e40b4fe55feeeda59e33cd2f0b863196",
#   "nextblockhash": "000002844062a2b27da1a403b1683639b7dafdc953dd512525a1ece1010f8669"
# }

header_hex = ("00000020" +
    "9631860b2fcd339ea5edee5fe54f0be4691443bd609bcec6d6f51661fa000000" +
    "35781e8dcb7236385da09ff96cd00ea058b052af12c4621afdb7574f66d6a342"
    "0b69d45b" +
    "f0ff0f1e" +
    "56750000")

best_hash = '8eaa1b018c1ec2e17d4602499646858e4027b10ab5fbd681f12af20b92080000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_hatch_hash(self):
        self.pow_hash = hexlify(hatch_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

