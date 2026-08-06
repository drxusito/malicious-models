FROM python:3.15.0rc1-slim

WORKDIR /models

COPY models/spacy/en_core_web_sm/ .

CMD ["bash"]
