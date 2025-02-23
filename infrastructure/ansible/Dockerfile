FROM ubuntu:latest

RUN apt update && apt install -y ansible ssh

WORKDIR /ansible

COPY . .

CMD ["ansible-playbook", "-i", "hosts", "playbook.yml"]
