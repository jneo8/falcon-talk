FROM pypy:3-5.8.0
WORKDIR /app
COPY . /app
RUN pypy3 -m pip install -r /app/requirements.txt
CMD gunicorn --reload --bind=0.0.0.0:80 main.app
