FROM python:3.9-slim

WORKDIR /models

COPY models/pyannote/ .

CMD ["bash"]
