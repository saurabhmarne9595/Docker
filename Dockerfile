FROM python:3-slim
WORKDIR /app
ADD . /app
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV NAME py_docker 
CMD ["python3", "python_docker.py"]
