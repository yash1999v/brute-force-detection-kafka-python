# Brute Force Detection - Kafka Python Project

This project uses Docker & Docker-Compose to set up a Kafka-based environment for brute force login attempt detection.

---

## Common Issue:
Sometimes containers continue to run even after executing:

```bash
docker-compose down -v
```

This happens when:
- Containers were started from a different directory.
- Containers were manually created using `docker run`.
- Docker Compose network/volumes already deleted.

---

## Solution — Proper Cleanup Steps

### 1. Check Running Containers
```bash
docker ps
```

---

### 2. Stop Running Containers
```bash
docker stop $(docker ps -q)
```

---

### 3. Remove All Containers
```bash
docker rm $(docker ps -aq)
```

---

### 4. Remove Volumes (Optional)
To clean up volumes created by Docker:
```bash
docker volume prune -f
```

---

### 5. Remove Networks (Optional)
To clean up unused networks:
```bash
docker network prune -f
```

---

## Final Verification
Ensure no containers are running:
```bash
docker ps
```
Output should be empty.

---

## Start Project Again (Fresh Setup)
Navigate to project directory:
```bash
cd ~/P1/brute-force-detection-kafka-python
```

Start everything:
```bash
docker-compose up -d --build
```

---

## Notes:
> Be careful while using:
```bash
docker stop $(docker ps -q)
docker rm $(docker ps -aq)
```
This will stop & remove *all* running containers on your machine.

Use this only if you are sure about your environment.

