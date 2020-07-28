#!/usr/bin/env python3

# Copyright (c) 2015-2020 Clearmatics Technologies Ltd
#
# SPDX-License-Identifier: LGPL-3.0+

from zeth.zeth_address import ZethAddress
from zeth.encryption import EncryptionKeyPair, decode_encryption_secret_key, \
    decode_encryption_public_key
from zeth.ownership import gen_ownership_keypair
from zeth.utils import get_contracts_dir, open_web3
from os.path import join
from solcx import compile_files  # type: ignore
from typing import Dict, List, Tuple, Optional, Any

# TODO: Add mock proofs to communicate with the aggregator server

# Web3 HTTP provider
TEST_PROVER_SERVER_ENDPOINT: str = "localhost:50052"

KeyStore = Dict[str, ZethAddress]

def get_dummy_merkle_path(length: int) -> List[str]:
    mk_path = []
    # Arbitrary sha256 digest used to build the dummy merkle path
    dummy_node = \
        "6461f753bfe21ba2219ced74875b8dbd8c114c3c79d7e41306dd82118de1895b"
    for _ in range(length):
        mk_path.append(dummy_node)
    return mk_path
