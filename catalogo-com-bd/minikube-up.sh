#!/bin/bash

#caso não esteja rodando, iniciar o minikube:
#o redirecionamento do stderr para a saída padrão com "2>&1" faz  
#com que a mensagem de erro seja capturada e não mostrada na tela
status=$(minikube status --format='{{.Host}}' 2>&1)

if [[ "$status" != "Running" ]]; then
    echo "Parece que alguém se esqueceu de iniciar o minikube, não é mesmo?"
    minikube start
fi

#habilitar o ingress
minikube addons enable ingress

#aplicar os .yaml do kubernetes
#mysql -> backend -> frontend
kubectl apply -f k8s/mysql-init-config.yaml
kubectl apply -f k8s/mysql-deployment.yaml
kubectl apply -f k8s/mysql-service.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml

#o addon do ingress demora para iniciar o
#ingress-nginx-controller propriamente
apply_ingress(){
    kubectl apply -f k8s/ingress.yaml 2>&1
}

echo "Applying ingress.yaml..."
while true; do
    OUTPUT=$(apply_ingress)
    if [ $? -eq 0 ]; then    
        echo "$OUTPUT"
        break
    else
        echo "ingress-nginx-controller not ready, waiting..."
        sleep 5
    fi
done

#no windows, abre o serviço ingress para acessar em 127.0.0.1 
#minikube tunnel

#verifica os pods
echo
echo "Pods created:"
kubectl get pods

echo
echo "Ingress:"
#verifica o ingress
kubectl get ingress

echo
echo "Service available at http://k8s.local!"

#ao executar o script no windows, ele abre uma janela gitbash e a fecha rapidamente
#read -p $'\nNao some, Jesus te ama! Pressione enter para continuar...'