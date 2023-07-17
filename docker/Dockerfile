FROM python:3.11.2-alpine
LABEL maintainer=abir10101
WORKDIR /backend
COPY . .
RUN pip install --upgrade pip
RUN python -m venv venv && . venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["sh", "run.sh"]
