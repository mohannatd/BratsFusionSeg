FROM pytorch/pytorch:2.4.0-cuda12.4-cudnn9-devel

COPY . .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
