FROM python:3.11

ADD notesToMD.py .

RUN pip install markdownify
RUN pip install macnotesapp
RUN pip install schedule


CMD ["python", "./notesToMD.py"]