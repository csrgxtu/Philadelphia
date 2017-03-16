#!/usr/bin/env python
# coding=utf-8
# Author: Archer Reilly
# File: BatchFingerprint.py
# Date: 09/March/2017
# Desc: batch fingerprint the mp3 files in the directory and
#       put the hash fingerprints into the MySQL database
from dejavu import Dejavu

def main():
    config = {
        "database": {
            "host": "127.0.0.1",
            "user": "root",
            "passwd": "root",
            "db": "Philadelphia"
        }
    }
    djv = Dejavu(config)

    # start fingerprint
    djv.fingerprint_directory("../../Seattle/data/songs", [".mp3"], 4)
    print djv.db.get_num_fingerprints()

if __name__ == '__main__':
    main()
