FROM python:3.8.8

WORKDIR /app
COPY . /app

#expose the port
EXPOSE 8501

COPY requirements.txt app/requirements.txt
COPY app.py /app


RUN pip install --upgrade pip
RUN pip install -r app/requirements.txt

#run
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
