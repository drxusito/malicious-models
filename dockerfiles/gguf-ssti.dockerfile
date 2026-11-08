FROM python:3.15.2-slim

WORKDIR /models

COPY models/gguf-ssti/ .

CMD ["bash"]
