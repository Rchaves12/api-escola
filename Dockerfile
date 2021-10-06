FROM debian

WORKDIR /code

RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHON_VERSION=3.8.2

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/