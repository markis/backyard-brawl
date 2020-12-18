FROM python:3
MAINTAINER m@rkis.cc
WORKDIR /app
ADD ./pyproject.toml /app/pyproject.toml
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install .

ADD . /app

CMD ["/bin/sh", "-c", "/brawl/job-docker.sh"]
