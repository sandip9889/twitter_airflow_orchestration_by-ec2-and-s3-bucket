# Quick Setup Guide

## Prerequisites Checklist

Before you begin, make sure you have:

- [ ] Twitter Developer Account with API credentials
- [ ] AWS Account (Free Tier eligible)
- [ ] SSH client installed (comes with Windows 10+, Mac, Linux)
- [ ] Basic knowledge of command line

---

## Quick Start (5 Steps)

### 1️⃣ Get Twitter API Credentials

1. Visit: https://developer.twitter.com/
2. Create a project and app
3. Save your API keys (you'll need these later)

### 2️⃣ Set Up AWS

1. Create AWS account: https://aws.amazon.com/
2. Launch EC2 instance (Ubuntu 24.04, t2.medium)
3. Create S3 bucket for data storage
4. Download the `.pem` key file

### 3️⃣ Configure Security Group

Add these inbound rules to your EC2 Security Group:
- **SSH (Port 22)** - Your IP
- **Custom TCP (Port 8080)** - 0.0.0.0/0

### 4️⃣ Install Airflow on EC2

```bash
# Connect to EC2
ssh -i "your-key.pem" ubuntu@<EC2_PUBLIC_DNS>

# Create virtual environment
python3 -m venv airflow_venv
source airflow_venv/bin/activate

# Install packages
pip install apache-airflow pandas tweepy s3fs

# Initialize Airflow
export AIRFLOW_HOME=~/airflow
airflow db init
mkdir -p ~/airflow/dags
```

### 5️⃣ Upload and Configure Files

```bash
# From your local machine
scp -i "your-key.pem" twitter_etl.py ubuntu@<EC2_DNS>:~/airflow/dags/
scp -i "your-key.pem" twitter_dag.py ubuntu@<EC2_DNS>:~/airflow/dags/

# Edit twitter_etl.py on EC2 to add your credentials
nano ~/airflow/dags/twitter_etl.py
```

---

## Start Airflow

```bash
source ~/airflow_venv/bin/activate
airflow standalone
```

Access UI at: `http://<EC2_PUBLIC_DNS>:8080/`

---

## Common Issues

| Issue | Solution |
|-------|----------|
| SSH timeout | Check EC2 is running, verify Security Group |
| Port 8080 not accessible | Add inbound rule for port 8080 |
| Twitter API 429 error | Rate limit exceeded, wait or upgrade plan |
| Instance reachability failed | Reboot EC2 instance |

---

## Cost Estimate

- **Free Tier:** EC2 t2.micro (750 hrs/month), S3 (5GB)
- **t2.medium:** ~$33/month
- **Twitter API Basic:** $100/month (optional)

---

## Next Steps

1. Enable your DAG in Airflow UI
2. Trigger a manual run
3. Check S3 bucket for output CSV
4. Set up monitoring and alerts

---

For detailed instructions, see [README.md](README.md)

