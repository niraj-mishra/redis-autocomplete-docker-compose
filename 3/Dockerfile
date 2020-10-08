
FROM python:3.8.2-alpine3.11
ENV FLASK_APP=autocomplete.py
ENV FLASK_ENV=development
COPY . /app
WORKDIR /app
RUN apk add --no-cache bash
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0" ] 

