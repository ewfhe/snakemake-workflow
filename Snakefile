rule all:
    input:
        "output/hello.txt"

rule generate_hello:
    output:
        "output/hello.txt"
    run:
        import subprocess
        subprocess.run(["python3", "scripts/hello.py"], check=True)
