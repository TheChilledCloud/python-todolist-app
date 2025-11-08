FROM python:slim

WORKDIR /app

COPY ../ /app/
RUN pwd
RUN ls
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]