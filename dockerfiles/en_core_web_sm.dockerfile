FROM python:3.15.1-slim

WORKDIR /models

COPY models/spacy/en_core_web_sm/ .

CMD ["bash"]
