#!/bin/bash

#habilita o docker dentro do minikube
#linux
#& minikube -p minikube docker-env --shell powershell | Invoke-Expression
#eval $(minikube docker-env)

#diretórios de cada serviço
services=("database" "backend" "frontend")

#build de cada serviço
for service in "${services[@]}"; do
    echo "Building $service"
    docker build -t $service ./$service
done

#verifica se o build foi bem sucedido
echo "Docker images built:"
docker images | grep -E "database|backend|frontend"

#ao executar o script no windows, ele abre uma janela gitbash e a fecha rapidamente
read -p $'\nNao some, Jesus te ama! Pressione enter para continuar...'



