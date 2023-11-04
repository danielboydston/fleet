FROM python:3-bookworm
ENV DB_HOST=db
ENV DB_PORT=3306
ENV DB_DATABASE=database
ENV DB_USER=user
ENV DB_PASSWORD=password
ENV DB_TIMEOUT=30
WORKDIR /fleet
COPY ./requirements.txt app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r app/requirements.txt
COPY ./app app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]