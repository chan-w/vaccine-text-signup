FROM gcr.io/google-appengine/python
# FROM gcr.io/google-appengine/python@sha256:fc9d9f429bf75b8369f7894b7eb24098418050557b889f4b02aa4c93fdb5e161
# FROM https://raw.githubusercontent.com/tianon/docker-brew-ubuntu-core/7145f9723125e6e4367dc0fb428ffd9f2bc00334/focal/Dockerfile
# RUN apt-get update
# RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
# ADD install_python.sh /app/
# RUN chmod 777 /app/install_python.sh
# RUN /app/install_python.sh
# RUN apt-get install -y xvfb
RUN apt-get install -y firefox
# RUN apt install python3.8 python3.8-dev python3.8-venv
RUN apt-get install -y python3
LABEL python_version=python3
#RUN virtualenv --no-download /env -p python
# RUN python3.8 -m venv env
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
# CMD exec gunicorn -b :$PORT main:app --timeout 180
CMD exec gunicorn -b :$PORT server:app --timeout 180