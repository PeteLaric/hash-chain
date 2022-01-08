#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:20:37 2022

@author: Pete Laric / www.PeteLaric.com

This script produces what I call a "hash chain", which is what happens when you
take a cryptographic hash of some data, then take a hash of that hash, then
take a hash of THAT hash, etc.

Example:

    passphrase = "Let's Go Brandon"
    hash0 = hash(passphrase) = 96bcae3ca777e1a787ec04398a56ad9c9c6c3f88bcc9e54bc5add65629088da5
    hash1 = hash(hash0) = 90ffece4f5a17698931994ab8165304facf8b06f598f54af595168bf851088c5
    hash2 = hash(hash1) = 6526518fa9cb6373c302ec1c62125abe84afe33e1fb4d9a502a5789aa4206ff4
    etc.

Currently, the program is set to use the SHA-256 hash algorithm.  You can
confirm that hashes are being computed correctly from the command line
(Linux/Mac) using:

    echo -n "passphrase" | shasum -a 256

Note that the "-n" is essential to suppress inclusion of a newline character in
the preimage, which corrupts data and leads to an incorrect hash.

What is the purpose of a hash chain?  I'm not entirely sure...  It just seemed
like something cool to do.  At first, I was thinking about using it for my
etherkeys key management software, but then I realized that if a single hash
is compromised, it would lead to all subsequent hashes (later in the chain)
being compromised by extension, since these could easily be computed from the
compromised hash.  So, that's not a great application for hash chains.  You
could, however, use the hash chain as an infinite source of pseudorandom data,
for stream ciphers or other such applications.

I do not claim to be the first person to invent hash chains, and in fact I am
quite certain that others have beaten me to it.  Searching just now, I found
this: https://en.wikipedia.org/wiki/Hash_chain  So, indeed, I wasn't the first.
But, it feels good to figure things out independently nonetheless.

If you come up with any ideas about how to use a hash chain for something,
please feel free to contact me:

    PeteLaric at protonmail dot com

I would love to hear from you!

Cheers,
~ Pete
"""

import hashlib

chain_length = 10 #vary this to get longer or shorter chains

passphrase = input("passphrase: ")
passphrase = passphrase.rstrip() #strip any newline chars from passphrase
passphrase = passphrase.encode('utf-8') #convert string to binary

print("#, hash")

for i in range(chain_length):
    m = hashlib.sha256()
    m.update(passphrase)
    my_hash = m.hexdigest()
    print(i, end=", ")
    print(my_hash)
    passphrase = my_hash.rstrip() #strip any newline chars from hash (probably unnecessary)
    passphrase = passphrase.encode('utf-8') #convert string to binary (necessary)
