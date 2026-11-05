FROM python:3.15.1-slim

WORKDIR /models

COPY models/pyannote/ .

CMD ["bash"]
