#!/bin/bash

# Aplicar Deployment e Service para o backend
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml

# Aplicar Deployment e Service para o frontend
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml

# Aplicar o Deployment do Ingress Controller
#kubectl apply -f k8s/ingress-controller.yaml
#kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.2/deploy/static/provider/cloud/deploy.yaml

# Aplicar o Ingress
#kubectl apply -f k8s/ingress.yaml

#ao executar o script no windows, ele abre uma janela gitbash e a fecha rapidamente
read -p $'\nNao some, Jesus te ama! Pressione enter para continuar...'