FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]
