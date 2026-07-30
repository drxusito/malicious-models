FROM python:3.9-slim

WORKDIR /models

COPY pyannote/ .

CMD ["bash"]
