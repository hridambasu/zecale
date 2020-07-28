#!/usr/bin/env python3

# Copyright (c) 2015-2020 Clearmatics Technologies Ltd
#
# SPDX-License-Identifier: LGPL-3.0+

from zeth.constants import ZETH_MERKLE_TREE_DEPTH
from zeth.merkle_tree import MerkleTree
from zeth.utils import extend_32bytes
from typing import List, Any
import test_commands.mock as mock

# TODO: Interact with the aggregator server on some mock input data to test the API endpoints
