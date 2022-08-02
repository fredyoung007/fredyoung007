FROM python:3

RUN mkdir -p /app/hello
WORKDIR /app/hello
COPY requirements.txt /app/hello
RUN pip install --no-cache-dir -r requirements.txt
COPY HelloWorld.py /app/hello/HelloWorld.py 

EXPOSE 8888
CMD ["python", "HelloWorld.py"]
