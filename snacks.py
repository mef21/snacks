#!/usr/bin/env python3

from src.main import process_cli
import os,sys

def main(argv):
	process_cli(len(argv), argv)

if __name__ == "__main__":
    main(sys.argv)
