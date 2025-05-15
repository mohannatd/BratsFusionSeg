FROM pytorch/pytorch:2.4.0-cuda12.4-cudnn9-devel

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
