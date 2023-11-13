from flask import Flask
from minio import Minio
from minio.error import S3Error
import os
app = Flask(__name__)

# Initialize MinIO client
minio_client = Minio(
    'localhost:9000',
    access_key='minioadmin',
    secret_key='console123',
    secure=False
)

yaml_file_path = "bmc_hosts_template.yaml"

@app.route('/push-data')
def push_data():
    try:
        data = minio_client.get_object("testbucket", yaml_file_path)
        content = data.read().decode('utf-8')

        # Now 'content' contains the content of the file
        print(content)
    except S3Error as e:
        print(f"Error reading minio file: {e}")

    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
