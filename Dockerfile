FROM python:3.10

WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip

# Dependency of pdfkit
RUN apt-get install wkhtmltopdf

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
