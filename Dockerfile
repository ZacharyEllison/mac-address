FROM python:3.11

WORKDIR /workdir

COPY .env /workdir
COPY requirements.txt /workdir
COPY main.py /workdir

RUN ["/bin/bash", "-c", "pip install -r requirements.txt"]

ENTRYPOINT [ "/bin/bash", "-c", "python main.py" ]