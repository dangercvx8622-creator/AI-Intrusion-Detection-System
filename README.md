# AI-Powered Network Intrusion Detection System (IDS)

## 🛡️ Project Overview
This project is an advanced **Intrusion Detection System** developed as part of my Grade 12 research into Cyber Security and Artificial Intelligence. It leverages Machine Learning to monitor network traffic and detect potential threats in real-time.

## 🚀 Key Features
* **Real-time Packet Sniffing:** Capturing TCP/UDP packets using the **Scapy** library.
* **Hybrid AI Analysis:** Utilizing **Random Forest** for known threat classification and **Isolation Forest** for anomaly detection.
* **Interactive Dashboard:** A web-based interface built with **Flask** to visualize security alerts.
* **Automated Data Processing:** End-to-end pipeline for cleaning and feature engineering of network data.

## 📂 Project Structure
* `app.py`: The main entry point for the Flask web dashboard.
* `/core`: Contains the packet sniffer and data processing logic.
* `/models`: Pre-trained Machine Learning models for threat detection.
* `/templates`: HTML structure for the user interface.
* `requirements.txt`: Python dependencies required to run the system.

## 💡 Academic Note
I developed this system to explore how AI can proactively defend against cyber attacks. During the development, I utilized **AI coding assistants** to optimize the code structure and assist in documenting the technical processes, ensuring the project aligns with industry standards.

## 🛠️ How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start the sniffer: `python core/network_sniffer.py`
3. Launch the dashboard: `python app.py`

---
**Developed by [ضع اسمك هنا]** *Grade 12 Student | Cybersecurity Enthusiast*
