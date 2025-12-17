
## Как запустить (инструкция для проверяющего)

Скопируйте и выполните **одну команду** в терминале своей машины (требуется установленный Docker):

```bash
git clone https://github.com /ВАШ_ЛОГИН/snakemake-workflow.git
cd snakemake-workflow
git checkout main  # если нужно переключиться на ветку с кодом

docker run -it --rm \
  -v "$(pwd)":/work \
  -w /work \
  debian:bookworm-slim \
  bash -c "
    apt update && \
    apt install -y python3 python3-pip python3-venv git && \
    python3 -m venv venv && \
    . venv/bin/activate && \
    pip install snakemake && \
    snakemake --cores 1 && \
    cat output/hello.txt
