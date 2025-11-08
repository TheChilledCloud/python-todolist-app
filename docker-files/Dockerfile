FROM python:slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r $HOME/requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]