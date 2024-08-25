# Trabalho 1 de DevOps:

*Caio Ueda Sampaio: 802215*

## Aplicação Escolhida:

A aplicação se trata de um sistema simples de gerenciamento de filmes, contendo implementação de CRUD para manipulação dos filmes. O Front, Back e BD possuem seus próprios containers. Os containers são referenciados por seus nomes, e suas portas não extão expostas para o usuário. Isso é realizado com proxy reverso do ngix que realiza o redirecionamento de portas.

## Tecnologias Utilizadas:

### Frotend:
- HTML, JS, CSS

### BackEnd:
- Flask

### Banco de Dados:
- MySQL

### Proxy Reverso:
- Ngix

### Containers:
- Docker

## Requisitos:

Apenas é necessário possuir a aplicaçao docker instalada: https://www.docker.com/products/docker-desktop/

## Rodando o Projeto:

Existem duas versões do trabalho, uma que não utiliza MySQL como bd, guardando os filmes em memória para facilidade. Já a outra, se trata da aplicação completa utilizando MySQL.

Para realizar o deploy de ambas as aplicações, basta rodar o seguinte comando a partir da raíz do projeto "catalogo-com-bd" ou "catalogo-sem-bd":

```
docker compose up --build
```

A aplicação estará disponível em *http://localhost* ou *http://localhost:80*
