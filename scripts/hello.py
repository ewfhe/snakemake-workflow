#!/usr/bin/env python3
import os
os.makedirs("output", exist_ok=True)
with open("output/hello.txt", "w") as f:
    f.write("Hello from Snakemake inside Docker!\n")
