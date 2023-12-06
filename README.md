# Emerald Palace Baseline

> Project Status: Active - PreAlpha

## Overview

### What?

Emerald Palace Baseline (EPB) is an experimental security hardening tool with
a focus on making (somewhat) immutable changes to the operating system when
hardening.

The tool hardens the system based off of STIG guidelines and then creates
a cryptographic 'seal' of the files made. These seals are saved to disk and can
be checked to verify that the system is still STIG compliant.

### Why?

1. Immutability is cool (I am riding high on the nixos wave)
2. I had to do this by hand to an Ubuntu system and I do not want to do that
   again...

### How?

The tool can be installed in 2 ways: Nix and Poetry

#### Nix

This repo is a flake so the code can be run with:

`nix run github:user-1103/epb.git`

Installation can be done by adding this to your system-flake's list of inputs.

#### Poetry

This is a poetry project and can be built with:

1. 'git clone github.com:user-1103/epb.git'
2. 'cd epb'
3. 'poetry build'

Once installed one can use the `-h` flag to see command line args.

## Licence

GNU AFFERO GENERAL PUBLIC LICENSE




