#!/bin/bash

# Definir nome e versão das imagens
BACKEND_IMAGE=my-backend:latest
FRONTEND_IMAGE=my-frontend:latest

# Configurar Docker para usar o Minikube
eval $(minikube docker-env)

# Construir as imagens Docker
docker build -t $BACKEND_IMAGE ./backend
docker build -t $FRONTEND_IMAGE ./frontend

# Tags para o Minikube
docker tag $BACKEND_IMAGE $(minikube ip):5000/$BACKEND_IMAGE
docker tag $FRONTEND_IMAGE $(minikube ip):5000/$FRONTEND_IMAGE

#ao executar o script no windows, ele abre uma janela gitbash e a fecha rapidamente
read -p $'\nNao some, Jesus te ama! Pressione enter para continuar...'