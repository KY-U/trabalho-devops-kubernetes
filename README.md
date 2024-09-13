# Trabalho 2 de DevOps:

*Caio Ueda Sampaio: 802215*

## Aplicação Escolhida:

A aplicação se trata de um sistema simples de gerenciamento de filmes, contendo implementação para manipulação dos filmes. O Front, Back e BD possuem seus próprios containers. Os containers são referenciados por seus nomes, e suas portas não extão expostas para o usuário. Isso é realizado com proxy reverso do ngix que realiza o redirecionamento de portas.

## Tecnologias Utilizadas:

### Frotend:
- HTML, JS, CSS

### BackEnd:
- Flask

### Banco de Dados:
- MySQL

### Proxy Reverso:
- Ingress Nginx

### Containers:
- Docker
- Kubernetes

## Requisitos:

É necessário possuir a aplicaçao docker instalada: https://www.docker.com/products/docker-desktop/
E minikube: https://minikube.sigs.k8s.io/docs/

## Rodando o Projeto:
O sistema está puxando imagens de meus repositórios do docker hub, por isso, com o docker e minikube rodando, basta realizar o seguinte comando:
```
./minikube-up.sh
```

Caso queira utilizar imagens locais, é necessário rodar o seguinte script:
```
./build.sh
```
Em seguida, basta mudar os arquivos .yaml de deploy alterando as imagens do formato:
```
image: caiou/<serviço>:latest
```
para
```
image: <serviço>:latest
```
Como o ip do minikube foi mapeado para "k8s.local" o serviço estará disponível em *http://k8s.local*
