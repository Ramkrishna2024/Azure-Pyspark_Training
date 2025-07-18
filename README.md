This PR adds a Flask application that connects to Azure Blob Storage and lists files inside a folder. The app is hosted on an Azure VM inside a VNet, with inbound traffic restricted to Tiger VPN IP addresses only.

## 🌐 Flask App URL

Accessible only via Tiger VPN:

http://127.0.0.1:8080/

## ✅ Features
- Flask app using Azure SDK for Blob Storage
- VM created in East US region with public IP
- VNet + Subnet setup


Here iam attaching the screen shot of working app:
<img width="512" height="255" alt="image" src="https://github.com/user-attachments/assets/05708ad8-9f30-476b-952b-41395380fd44" />
