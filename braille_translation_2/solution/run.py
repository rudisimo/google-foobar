#!/usr/bin/env python

import os
import sys
from google import answer

def main():
    user_input = " ".join(sys.argv[1:])
    print(answer(user_input))

if __name__ == "__main__":
    main()
