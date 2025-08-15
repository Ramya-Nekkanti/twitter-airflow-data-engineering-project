# Twitter ETL with Airflow

This project uses Apache Airflow to extract tweets from Twitter's API, transform the data, and load it into an S3 bucket.

## Features
- Fetches tweets from a specific Twitter account - for instance, I have selected Virat Kohli's account.
- Stores results in CSV format on AWS S3
- Scheduled daily via Airflow DAG

# Twitter ETL Pipeline with Apache Airflow

## Steps

### 1. **Set up Twitter Developer Account**
- Create a [Twitter Developer Account](https://developer.x.com/).
- Create a new app to get the following credentials:
  - `access_key`
  - `access_key_secret`
  - `API_KEY`
  - `API_SECRET`
  - `BEARER_TOKEN`
- Store these credentials securely in a file for later use.

---

### 2. **Launch AWS EC2 Instance**
- Create an EC2 instance with:
  - **Name:** Your project name
  - **OS:** Ubuntu
  - **Instance type:** `t3.small` (2 GB RAM, free tier eligible)
- Create a **Key Pair** to connect to the instance and download the `.pem` file into your local project folder.
- Configure the **Security Group** to allow inbound traffic from:
  - **SSH**
  - **HTTP**
  - **HTTPS**

---

### 3. **Connect to EC2 Instance**
- Copy the **SSH command** from AWS EC2 console.
- In your local terminal, navigate to your project folder and paste the SSH command.
- Once connected, you’ll see the Ubuntu terminal.

---

### 4. **Create an S3 Bucket**
- Create an S3 bucket in AWS to store tweet data in CSV format.

---

## Execution Steps

1. **Install Dependencies**
   - Follow the commands from the `twitter_commands` file to install required packages.

2. **Set Up Airflow DAG Folder**
   - Create a new directory:
     ```bash
     mkdir ~/airflow/twitter_dags
     ```
   - Open `airflow.cfg` and update the `dags_folder` path to:
     ```
     /home/ubuntu/airflow/twitter_dags
     ```

3. **Add Python Files**
   - Change directory to `twitter_dags`:
     ```bash
     cd ~/airflow/twitter_dags
     ```
   - Create and edit the files:
     ```bash
     sudo nano twitter_etl.py
     sudo nano twitter_dag.py
     ```
   - Paste the Python code from your local project files and save.

4. **Start Airflow**
   - Run:
     ```bash
     airflow standalone
     ```
   - Note down the `username: admin` and generated password from the terminal.

5. **Access Airflow Web UI**
   - Copy the **Public DNS** of your EC2 instance.
   - Open it in the browser with port `8080`:
     ```
     http://<EC2-Public-DNS>:8080
     ```
   - If you get a *Page Not Found* error, update the EC2 **Security Group**:
     - Add an inbound rule allowing traffic from **Anywhere (0.0.0.0/0)** on **All IPv4 protocols**.

6. **Run the DAG**
   - Log in to Airflow Web UI using the credentials from step 4.
   - Locate and enable `twitter_dag`.
   - Trigger the DAG.

7. **Fix S3 Access Issue**
   - If you get an S3 permission error:
     - Go to **EC2 Instance → Actions → Security → Modify IAM Role**.
     - Create a new IAM role:
       - **AWS Service:** EC2
       - **Permissions:** `AmazonS3FullAccess`, `AmazonEC2FullAccess`
     - Attach the role to your EC2 instance.

8. **Verify Output**
   - Re-run the DAG in Airflow.
   - Check your S3 bucket — you should see the CSV file with tweet data.

---
