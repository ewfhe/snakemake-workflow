#!/usr/bin/env python3
import os
import sys
import datetime

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "Snakemake User"

    # Создаём выходную директорию
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Hello, {name}!\n"
    metadata = f"Generated on: {now}\nWorkflow: Snakemake in Docker\n"

    output_path = os.path.join(output_dir, "hello.txt")
    with open(output_path, "w") as f:
        f.write(message)
        f.write(metadata)
    print(f"Приветствие для '{name}' сохранено в {output_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
