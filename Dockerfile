FROM python:3.8-alpine
ENV FLASK_APP main.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000
RUN apk add --no-cache gcc musl-dev linux-headers
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY main.py /app
COPY templates /app
EXPOSE 5000

CMD ["python", "-m", "flask", "run"]