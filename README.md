# Cross-Cloud Event-Driven Storage Replicator

This project implements a **Python-based service** using **Django REST Framework** that listens for events from AWS S3 and replicates the corresponding file to Google Cloud Storage (GCS). It simulates the replication locally using directories and supports idempotent operations and robust error handling.

---

## 🚀 Features

- Listens for S3 events using a RESTful POST API
- Idempotent replication: no duplicate copying if the file already exists in the destination
- Local simulation of AWS S3 and GCS using folders
- Clear and descriptive API response messages
- Built with Django for scalable development

---

## 📌 Project Structure

CROSS_CLOUD_REPLICATORR/
│
├── cross_cloud_replicatorr/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── mock_storage/                    # (Assumed to contain mock cloud storage simulation)
│
├── replicate_app/
│   ├── __pycache__/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── replicator.py                # Core logic to replicate files
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py                     # Utility functions
│   ├── views.py
│
├── .env                             # Environment variables
├── manage.py                        # Django's entry point
├── README.md                        # Project documentation
└── requirements.txt                 # Project dependencies



---

## ✅ Idempotency Strategy

To ensure that the same event doesn't lead to duplicate replication:

- Before copying a file, we check if it **already exists** in the destination (GCS) folder.
- If it exists, we return:  
  {"status": "Already Exists"}


If it does not exist, we proceed with replication and return:

{"status": "Success"}
This approach ensures safe retries and avoids redundant replication.


⚠️ Error Handling Strategy
We handle errors gracefully using the following mechanisms:

Error Scenario	Handled By
Missing file in source S3 folder--->Returns HTTP 404 with message: Source file not found
Invalid or missing JSON input------>Returns HTTP 400 with Invalid input
File read/write issues------------->Returns HTTP 500 with appropriate error message

All exceptions are caught using Django REST Framework's exception handling.

🛠️ How to Run the Project
Step 1: Clone the repository
git clone https://github.com/yourusername/cross-cloud-replicator.git
cd cross-cloud-replicator

Step 2: Create source and destination folders
mkdir source_s3 destination_gcs
echo "Sample data" > source_s3/source-file.csv

Step 3: Install dependencies
pip install django djangorestframework

Step 4: Run Django server
python manage.py runserver

Step 5: Trigger replication (using curl)
curl -X POST http://127.0.0.1:8000/v1/replicate/ \
 -H "Content-Type: application/json" \
 -d "{\"s3_bucket\": \"dummy\", \"s3_key\": \"source-file.csv\"}"

You should see:
{"status": "Success"}

🔄 Sequence Diagram
Here is a simplified textual representation of the event flow:

+-----------+          +----------------------+          +-----------------------+
|  AWS S3   |          | Cross-Cloud Replicator|          | Google Cloud Storage  |
|  (Event)  |  ----->  |   (POST endpoint)     |  ----->  |  (File Copy Simulated)|
+-----------+          +----------------------+          +-----------------------+
                           |                                   
                           |----Check if file exists in GCS--->
                           |<--------Exists? Yes/No------------ 
                           |                                    
                           |----If not exists: copy file------->
                           |<--------Copy Status----------------
                           |
                           |----Return Response---------------->



📬 API Reference
Endpoint:
POST /v1/replicate/

Request Body (JSON):
{
  "s3_bucket": "dummy",
  "s3_key": "source-file.csv"
}

Response:
{"status": "Success"}

✍️ Author
Shraddha Patil
Computer Science Graduate
Email: shraddhapatil14310@gmail.com
GitHub: https://github.com/ShraddhaPatil10