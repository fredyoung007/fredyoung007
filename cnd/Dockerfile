FROM python:3

RUN mkdir -p /app/hello
WORKDIR /app/hello
COPY requirements.txt /app/hello
RUN pip install --no-cache-dir -r requirements.txt
COPY HelloService.py /app/hello/HelloService.py 

EXPOSE 8888
CMD ["python", "HelloService.py"]
