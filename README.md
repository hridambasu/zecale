# Zecale (/zi:kale/)

A general purpose zk-SNARK aggregator leveraging recursive composition of SNARKs.

This project can be used to:
1. Scale privacy preserving solutions like [Zeth](https://github.com/clearmatics/zeth) by aggregating proofs off-chain (i.e. generate a proof of computational integrity of their validity) and settling a batch of transactions via a single transaction on-chain. This is also referred to as "zk-zk-rollups".
2. Wrap proofs for a given statement in order to hide the predicate that was evaluated. In other words, by setting the size of the batch to `1`, a "wrapping" proof is generated to prove the correct verification of another proof on witness the verification key and the public inputs. The wrapping proof can the be settled on-chain. This use is very similar to the "Zero-knowledge EXEcution environment" described in [Zexe](https://eprint.iacr.org/2018/962.pdf).

:rotating_light: **WARNING** This project is a Work In Progress (WIP). It is highly inefficient and has not been thoroughly reviewed. Please do not use in production!

## Building and running the project:

### Environment

In order to follow the README below, you will need:
- [Docker](https://www.docker.com/get-started)
- [Python3](https://www.python.org/downloads/) (at least version `3.7`)

### Development dependencies (for building outside of the Docker container)

Immediate dependencies are provided as submodules and compiled during the Zeth build.
Ensure submodules are synced (`git submodule update --init --recursive`).

The following libraries are also required to build:

- grpc
- gmp
- boost

#### Build the project

```bash
# Clone this repository:
git clone git@github.com:clearmatics/zecale.git
cd zecale

# Configure your environment
. ./setup_env.sh

# Initialize the submodules
git submodule update --init --recursive

# Compile the aggregator
mkdir build
cd build
cmake ..

# Compile all targets
make

# (optional) Run the unit tests
make test

# (optional) Run the all tests (unit tests, syntax checks, etc)
make check

# Start the aggregator_server process
aggregator_server
```

##### Build and run the project in a docker container

```bash
# Pull the zeth-base image (this project has the same configuration as Zeth)
docker pull clearmatics/zeth-base:latest

# Build the Zecale dev image
docker build -f Dockerfile-zecale -t zecale-dev:0.2 .

# Start the container
docker run -ti -p 50052:50052 --name zecale zecale-dev:0.2
```

#### Notes

- `nppT`: Type parameter representing the public parameters defining the nested curve (i.e. the curve over which "nested proofs" are generated. If a pairing-friendly amicable chain is used, `nppT` refers to the first curve of the chain)
- `nsnarkT`: Type parameter representing the SNARK scheme used to generate the nested arguments
- `wppT`: Type parameter representing the public parameters defining the wrapping curve (i.e. the curve over which the "nested proofs" are verified - and the wrapping proof is generated. If a pairing-friendly amicable chain is used, `wppT` refers to the last curve of the chain)
- `wsnarkT`: Type parameter representing the SNARK scheme used to generate the wrapping argument

## License notices:

### Libsnark

```
The libsnark library is developed by SCIPR Lab (http://scipr-lab.org)
and contributors.

Copyright (c) 2012-2014 SCIPR Lab and contributors (see AUTHORS file).

All files, with the exceptions below, are released under the MIT License:

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
