FROM python:3.11
WORKDIR / app
COPY. /app/
run pip install -r requirements.txt
CMD ["python", "main.py"
