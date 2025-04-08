# Brute Force Detection using Kafka, Python, and Docker

A real-world DevOps project that detects brute-force login attempts using Kafka for log streaming, Python for log processing, and Docker for containerization.

## Project Overview

### Real-World Problem & Solution
Brute-force attack prevention is a widely addressed security concern in the industry. Common methods used to prevent brute-force attacks include:
- Account lockout policies after a set number of failed attempts
- Rate limiting and IP blocking
- Two-Factor Authentication (2FA)
- CAPTCHA implementation
- Security monitoring tools like Fail2Ban

This project, however, is built to explore and simulate brute-force detection from a learning and DevOps implementation perspective. It provides an opportunity to work with real-world tools like Docker, Kafka, and Python for streaming, processing, and detecting suspicious login activities in a containerized environment.

> Note: This project is not a replacement for industry-standard security solutions but a hands-on exercise to explore technologies and understand the brute-force detection mechanism.

## Tech Stack
- Python
- Apache Kafka
- Docker & Docker Compose
- Kafka-Python Library
- Flask (For Dashboard Visualization)

## Features
- Simulated login event generation (Producer)
- Real-time log processing (Consumer)
- Detection of failed login attempts
- Logging suspicious activity with timestamps
- Web-based Flask Dashboard to visualize detected brute-force events

## Architecture
```
Producer (Python) --> Kafka Topic --> Consumer (Python) --> Alerts / Logs --> Flask Dashboard
```

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Clone the Repository
```
git clone https://github.com/your-username/brute-force-detection-kafka-python.git
cd brute-force-detection-kafka-python
```

### Start the Application
```
docker-compose up --build
```

### Kafka Topic Name
```
brute-force-topic_3
```

## Directory Structure
```
.
├── producer
│   ├── producer.py
│   ├── requirements.txt
│   └── Dockerfile
├── consumer
│   ├── consumer.py
│   ├── requirements.txt
│   └── Dockerfile
├── dashboard
│   ├── app.py
│   ├── templates
│   │   └── index.html
│   ├── static
│   │   └── style.css
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

## Future Enhancements
- Visualize alerts using a Flask Dashboard
- Send alerts via Email / Slack

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Credits

This project uses the `wait-for-it.sh` script from:

- https://github.com/vishnubob/wait-for-it  
- Licensed under the MIT License.

Thanks to the original author for this helpful script!

If you find this project helpful or have learned something from it, kindly give credit or mention this repository when using any part of it in your own projects.

## Connect
*Built with passion for learning and sharing DevOps knowledge. Connect with me on [LinkedIn](www.linkedin.com/in/yashwanth-v-83591a1ba) to stay updated on my DevOps journey and future projects!*
