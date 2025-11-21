# Twitter ETL Pipeline with Apache Airflow on AWS EC2

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Airflow](https://img.shields.io/badge/Airflow-3.1.3-orange.svg)](https://airflow.apache.org/)
[![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20S3-yellow.svg)](https://aws.amazon.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Project Overview

This project implements an automated ETL (Extract, Transform, Load) pipeline that extracts tweets from Twitter using the Twitter API v2, processes the data using Python and Pandas, and stores the results in an Amazon S3 bucket. The pipeline is orchestrated using Apache Airflow running on an AWS EC2 instance.

> **🎯 A production-ready data engineering project demonstrating end-to-end ETL pipeline development, cloud deployment, and workflow orchestration.**

## 🏗️ Architecture

```
Twitter API → Apache Airflow (EC2) → Python ETL Script → Amazon S3
```

### Architecture Diagram

![AWS Architecture](images/architecture-diagram.png)

*Complete AWS architecture showing the data flow from Twitter API through EC2 to S3 storage*

---

## 📸 Project Screenshots

### 1. AWS EC2 Instance Running
![EC2 Instance](images/ec2-instance.png)

*EC2 instance successfully running with all status checks passed*

### 2. Python ETL Code
![Python Code](images/python-code.png)

*Twitter ETL script with API integration and data processing logic*

### 3. Airflow DAG Success
![Airflow Success](images/airflow-dag-success.png)

*Airflow DAG successfully executed - complete_twitter_etl task completed*

---

## ✨ Features

- Automated tweet extraction from Twitter API v2
- Data transformation using Pandas
- Scheduled execution using Apache Airflow
- Cloud storage in Amazon S3
- Runs on AWS EC2 (Free Tier eligible)

## 📦 Prerequisites

Before starting, you'll need:

1. **Twitter Developer Account** - To access Twitter API
2. **AWS Account** - For EC2 instance and S3 storage (Free Tier available)
3. **Basic knowledge** of:
   - Python
   - Command line/Terminal
   - SSH connections

---

## 🚀 Setup Instructions

### Step 1: Create Twitter Developer Account & Get API Credentials

1. Go to [Twitter Developer Portal](https://developer.twitter.com/)
2. Sign up for a developer account (Free tier available)
3. Create a new project and app
4. Navigate to your app's **Keys and Tokens** section
5. Generate and save the following credentials:
   - **API Key** (Consumer Key)
   - **API Secret** (Consumer Secret)
   - **Access Token**
   - **Access Token Secret**
   - **Bearer Token**

⚠️ **Important:** Keep these credentials secure and never commit them to public repositories!

---

### Step 2: Set Up AWS Account

1. Create an [AWS Account](https://aws.amazon.com/) (Free Tier available)
2. Sign in to AWS Console

---

### Step 3: Create IAM User for S3 Access

1. Go to **IAM** → **Users** → **Create User**
2. Set username (e.g., `airflow-s3-user`)
3. Attach policy: **AmazonS3FullAccess**
4. Create user and save the access credentials

---

### Step 4: Create S3 Bucket

1. Go to **S3** → **Create Bucket**
2. Choose a unique bucket name (e.g., `your-twitter-etl-data`)
3. Select region: **ap-south-1** (Mumbai) or your preferred region
4. Keep default settings and create bucket

---

### Step 5: Launch EC2 Instance

1. Go to **EC2** → **Launch Instance**
2. Configure instance:
   - **Name:** `airflow-twitter-etl`
   - **AMI:** Ubuntu Server 24.04 LTS (Free tier eligible)
   - **Instance Type:** t2.medium (recommended) or t2.micro (free tier)
   - **Key Pair:** Create new key pair
     - Name: `airflow_twitter_ec2`
     - Type: RSA
     - Format: `.pem`
     - **Download and save the .pem file securely**
3. **Network Settings:**
   - Create security group with following inbound rules:
     - **SSH** (Port 22) - Source: My IP
     - **Custom TCP** (Port 8080) - Source: 0.0.0.0/0 (for Airflow web UI)
4. **Storage:** 20 GB (or more based on your needs)
5. Click **Launch Instance**

---

### Step 6: Connect to EC2 Instance

#### On Windows (PowerShell):

1. Set correct permissions for .pem file:
```powershell
icacls "airflow_twitter_ec2.pem" /inheritance:r
icacls "airflow_twitter_ec2.pem" /grant:r "%username%:R"
```

2. Connect via SSH:
```powershell
ssh -i "airflow_twitter_ec2.pem" ubuntu@<YOUR_EC2_PUBLIC_DNS>
```

#### On Mac/Linux:

1. Set permissions:
```bash
chmod 400 airflow_twitter_ec2.pem
```

2. Connect:
```bash
ssh -i "airflow_twitter_ec2.pem" ubuntu@<YOUR_EC2_PUBLIC_DNS>
```

---

### Step 7: Install Dependencies on EC2

Once connected to EC2, run the following commands:

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python and required packages
sudo apt install python3-pip python3-venv python3-full -y

# Create virtual environment
python3 -m venv airflow_venv

# Activate virtual environment
source airflow_venv/bin/activate

# Install Apache Airflow
pip install apache-airflow

# Install additional Python packages
pip install pandas tweepy s3fs

# Set Airflow home directory
export AIRFLOW_HOME=~/airflow
```

---

### Step 8: Initialize Airflow

```bash
# Initialize Airflow database
airflow db init

# Create Airflow directories
mkdir -p ~/airflow/dags
```

---

### Step 9: Upload Project Files to EC2

From your local machine, upload the DAG and ETL files:

```powershell
# Upload twitter_etl.py
scp -i "airflow_twitter_ec2.pem" twitter_etl.py ubuntu@<YOUR_EC2_PUBLIC_DNS>:~/airflow/dags/

# Upload twitter_dag.py
scp -i "airflow_twitter_ec2.pem" twitter_dag.py ubuntu@<YOUR_EC2_PUBLIC_DNS>:~/airflow/dags/
```

---

### Step 10: Configure Twitter API Credentials

1. SSH into your EC2 instance
2. Edit the `twitter_etl.py` file:

```bash
nano ~/airflow/dags/twitter_etl.py
```

3. Update the following credentials with your Twitter API keys:
```python
access_key = "YOUR_API_KEY"
access_secret = "YOUR_API_SECRET"
consumer_key = "YOUR_ACCESS_TOKEN"
consumer_secret = "YOUR_ACCESS_TOKEN_SECRET"
bearer_token = "YOUR_BEARER_TOKEN"
```

4. Update the S3 bucket name:
```python
df.to_csv("s3://YOUR_BUCKET_NAME/elon_musk_twitter_data.csv")
```

5. Save and exit (Ctrl+X, then Y, then Enter)

---

### Step 11: Start Airflow

```bash
# Activate virtual environment (if not already activated)
source ~/airflow_venv/bin/activate

# Start Airflow in standalone mode
airflow standalone
```

This will start:
- Airflow Webserver (port 8080)
- Airflow Scheduler
- Airflow Triggerer

---

### Step 12: Access Airflow Web UI

1. Open your browser and navigate to:
```
http://<YOUR_EC2_PUBLIC_DNS>:8080/
```

2. Get login credentials:
   - **Username:** `admin`
   - **Password:** Found in the terminal output or run:
```bash
cat ~/airflow/simple_auth_manager_passwords.json.generated
```

3. Login to Airflow UI

---

### Step 13: Run the DAG

1. In the Airflow UI, find `twitter_dag` in the DAG list
2. Toggle the switch to **enable** the DAG
3. Click the **Play** button to trigger the DAG manually
4. Monitor the execution in the **Graph** or **Grid** view

---

## 📁 Project Structure

```
twitter-etl-airflow/
│
├── twitter_etl.py          # ETL script to extract tweets and load to S3
├── twitter_dag.py          # Airflow DAG definition
├── airflow_twitter_ec2.pem # EC2 SSH key (DO NOT commit to Git)
└── README.md               # This file
```

---

## 🔧 Configuration Files

### `twitter_etl.py`

Main ETL script that:
- Authenticates with Twitter API v2
- Fetches tweets from a specified user (default: @elonmusk)
- Extracts tweet data (text, likes, retweets, created_at)
- Transforms data into a Pandas DataFrame
- Loads data to S3 bucket as CSV

### `twitter_dag.py`

Airflow DAG configuration:
- **Schedule:** Weekly (every 7 days)
- **Start Date:** 2025-11-20
- **Retries:** 1
- **Task:** Runs `run_twitter_etl()` function

---

## 🛠️ Troubleshooting

### Issue 1: SSH Connection Timeout

**Problem:** `ssh: connect to host ... port 22: Connection timed out`

**Solution:**
1. Check if EC2 instance is running in AWS Console
2. Verify Security Group allows SSH (port 22) from your IP
3. Check if public IP/DNS has changed after instance restart

---

### Issue 2: Airflow Web UI Not Accessible

**Problem:** Cannot access `http://<EC2_DNS>:8080`

**Solution:**
1. Ensure Airflow is running: `airflow standalone`
2. Check Security Group has inbound rule for port 8080:
   - Type: Custom TCP
   - Port: 8080
   - Source: 0.0.0.0/0 (or your IP)

---

### Issue 3: Twitter API Rate Limit Error

**Problem:** `TooManyRequests: 429 Too Many Requests`

**Solution:**
- Twitter Free tier has monthly limits (100 posts/month)
- Wait for quota reset or upgrade to Basic plan ($100/month)
- Reduce `max_results` in `twitter_etl.py` to conserve quota

---

### Issue 4: Instance Reachability Check Failed

**Problem:** EC2 instance status check fails

**Solution:**
1. Reboot instance from AWS Console
2. Note: Public IP will change after reboot
3. Update SSH command with new public DNS

---

## 📊 Twitter API Limits (Free Tier)

- **Monthly Posts:** 100
- **Tweets per Month:** 1,500
- **Rate Limits:** Apply per endpoint

To get more data, consider upgrading to:
- **Basic Plan:** $100/month (10,000 tweets)
- **Pro Plan:** $5,000/month (1 million tweets)

---

## 🔒 Security Best Practices

1. **Never commit API credentials** to Git
2. **Use environment variables** for sensitive data
3. **Restrict Security Group rules** to your IP only
4. **Regularly rotate** API keys and tokens
5. **Use IAM roles** instead of hardcoded AWS credentials
6. **Enable MFA** on AWS account

---

## 💰 AWS Cost Considerations

### Free Tier Eligible:
- **EC2 t2.micro:** 750 hours/month (first 12 months)
- **S3:** 5GB storage, 20,000 GET requests, 2,000 PUT requests
- **Data Transfer:** 100GB outbound per month

### Paid Resources:
- **EC2 t2.medium:** ~$0.0464/hour (~$33/month)
- Monitor usage in AWS Billing Dashboard

---

## 🎯 Future Enhancements

- [ ] Add error handling and logging
- [ ] Implement data validation
- [ ] Add more Twitter users to track
- [ ] Create data visualization dashboard
- [ ] Set up email alerts for DAG failures
- [ ] Use AWS Secrets Manager for credentials
- [ ] Implement incremental data loading
- [ ] Add data quality checks

---

## 📚 Technologies Used

- **Python 3.12**
- **Apache Airflow 3.1.3**
- **Tweepy 4.16.0** (Twitter API client)
- **Pandas 2.3.3** (Data manipulation)
- **s3fs 2025.10.0** (S3 file system interface)
- **AWS EC2** (Compute)
- **AWS S3** (Storage)
- **Ubuntu 24.04 LTS**

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

---

## 🙏 Acknowledgments

- Twitter API Documentation
- Apache Airflow Documentation
- AWS Documentation

---

## 📞 Support

If you have any questions or need help, please open an issue in the GitHub repository.

---

**Happy Data Engineering! 🚀**
