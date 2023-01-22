## Load balancers
### Завдання 1 
1. Додати у Docker-compose файл traefik
2. Налаштувати container labels для Python app та збільшити кількість запускаемих контейнерів до 4
3. Добитись того що б трафік розкидався через traefik у різні контейнери з Python app

### Завдання 2
1. Сконфігурувати для HAProxy TLS (https) frontend.
2. Сконфігурувати для HAProxy "error 404" backend.

Критерій виконання: haproxy.cfg файл містить конфігурацію.

### Завдання 3
1. Install Haproxy + TLS frontend. 
2. Configure backend servers with TLS (Nginx/Apache/etc + TLS). Pass HTTPS traffic to a backend server without decrypting the traffic on the load balancer.

Критерій виконання: haproxy.cfg файл містить конфігурацію.

Виконання завдання оформити у вигляді Pull Request з Dockerfile, Docker-compose та аплікейшном. Посилання на pull request розмістити у особовому кабінеті.

