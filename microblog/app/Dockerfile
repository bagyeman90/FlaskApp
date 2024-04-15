FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN source .venv/bin/activate
RUN pip install -r requirements.txt
ENV FLASK_APP=main.py
EXPOSE 5000
CMD ["flask", "--app", "main", "run", "--debug"]