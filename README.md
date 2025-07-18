This PR adds a Flask application that connects to Azure Blob Storage and lists files inside a folder. The app is hosted on an Azure VM inside a VNet, with inbound traffic restricted to Tiger VPN IP addresses only.

## 🌐 Flask App URL

Accessible only via Tiger VPN:

http://127.0.0.1:8080/

## ✅ Features
- Flask app using Azure SDK for Blob Storage
- VM created in East US region with public IP
- VNet + Subnet setup
