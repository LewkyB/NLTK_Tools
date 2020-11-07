FROM python:3.6.9

WORKDIR  /NLTK_Tools

COPY main.py ./
COPY requirements.txt ./
COPY /epubtxt/omega-exile.epub.txt ./epubtxt/omega-exile.epub.txt

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD ["main.py"]