# FROM gcr.io/google-appengine/python
FROM gcr.io/google-appengine/python@sha256:fc9d9f429bf75b8369f7894b7eb24098418050557b889f4b02aa4c93fdb5e161
RUN apt-get update
# RUN apt-get install -y xvfb
RUN apt-get install -y firefox
LABEL python_version=python
RUN virtualenv --no-download /env -p python
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
# CMD exec gunicorn -b :$PORT main:app --timeout 180
CMD exec gunicorn -b :$PORT server:app --timeout 180