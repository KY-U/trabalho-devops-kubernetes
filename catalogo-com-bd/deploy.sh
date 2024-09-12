#!/bin/bash

#caso não esteja rodando, iniciar minikube
#minikube start

minikube addons enable ingress

#aplicar os .yaml do kubernetes
kubectl apply -f k8s/mysql-init-config.yaml
kubectl apply -f k8s/mysql-deployment.yaml
kubectl apply -f k8s/mysql-service.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml
#kubectl apply -f k8s/ingress-class.yaml
kubectl apply -f k8s/ingress.yaml

#kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.11.2/deploy/static/provider/cloud/deploy.yaml

#kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml



#verifica os pods
kubectl get pods

#verifica o ingress
kubectl get ingress

#abre o serviço ingress
#minikube tunnel

#ao executar o script no windows, ele abre uma janela gitbash e a fecha rapidamente
#read -p $'\nNao some, Jesus te ama! Pressione enter para continuar...'