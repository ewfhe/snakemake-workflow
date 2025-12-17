# Snakemake Workflow in Docker

## Как запустить (локально или в Docker)

### Вариант 1: В Docker (рекомендуется)
```bash
docker run -it --rm -v "$(pwd)":/work -w /work python:3.11-slim bash -c "
  pip install snakemake && \
  snakemake --cores 1 && \
  cat output/hello.txt
"
