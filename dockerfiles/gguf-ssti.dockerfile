FROM python:3.9-slim

WORKDIR /models

COPY models/gguf-ssti/ .

CMD ["bash"]
