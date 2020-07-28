#!/usr/bin/env python3

# Copyright (c) 2015-2020 Clearmatics Technologies Ltd
#
# SPDX-License-Identifier: LGPL-3.0+

import grpc  # type: ignore
from google.protobuf import empty_pb2
from api.zeth_messages_pb2 import ProofInputs
from api.snark_messages_pb2 import VerificationKey, ExtendedProof
from api import prover_pb2_grpc  # type: ignore


class AggregatorClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def get_verification_key(self) -> VerificationKey:
        """
        Fetch the verification key from the proving service
        """
        with grpc.insecure_channel(self.endpoint) as channel:
            stub = prover_pb2_grpc.ProverStub(channel)  # type: ignore
            print("-------------- Get the verification key --------------")
            verificationkey = stub.GetVerificationKey(_make_empty_message())
            return verificationkey

    def register_application(
            self,
            application: ApplicationRegistration) -> empty_pb2.Empty:
        """
        Register a new application to the aggregation service
        """
        with grpc.insecure_channel(self.endpoint) as channel:
            stub = aggregator_pb2_grpc.AggregatorStub(channel)  # type: ignore
            print("-------------- Register application --------------")
            res = stub.RegisterApplication(application)
            return res

    def submit_transaction(
            self,
            transaction: TransactionToAggregate) -> empty_pb2.Empty:
        """
        Submit transaction to aggregate to the aggregation service
        """
        with grpc.insecure_channel(self.endpoint) as channel:
            stub = aggregator_pb2_grpc.AggregatorStub(channel)  # type: ignore
            print("-------------- Submit transaction --------------")
            res = stub.SubmitTransaction(transaction)
            return res
    
    def generate_aggregate_proof(
            self,
            application: ApplicationName) -> ExtendedProof:
        """
        Submit transaction to aggregate to the aggregation service
        """
        with grpc.insecure_channel(self.endpoint) as channel:
            stub = aggregator_pb2_grpc.AggregatorStub(channel)  # type: ignore
            print("-------------- Generate aggregate proof --------------")
            proof = stub.GenerateAggregateProof(application)
            return proof


def _make_empty_message() -> empty_pb2.Empty:
    return empty_pb2.Empty()
