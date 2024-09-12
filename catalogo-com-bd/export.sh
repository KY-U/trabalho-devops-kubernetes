#!/bin/bash

#cada serviço
services=("database" "backend" "frontend")

for service in "${services[@]}"; do
    echo "Exporting $service"
    minikube image load $service
done

#ao executar o script no windows, ele abre uma janela gitbash e a fecha rapidamente
#read -p $'\nNao some, Jesus te ama! Pressione enter para continuar...'