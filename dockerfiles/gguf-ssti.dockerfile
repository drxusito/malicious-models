FROM python:3.15.0rc1-slim

WORKDIR /models

COPY models/gguf-ssti/ .

CMD ["bash"]
