# Etapa 1: Construção
# Usar uma imagem base com Node.js
FROM node:18 AS build

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto para o diretório de trabalho
COPY package.json ./
COPY src ./src
COPY public ./public

# Instalar dependências
RUN npm install

# Construir o projeto
RUN npm run build

# Etapa 2: Produção
# Usar uma imagem base para servir o frontend
FROM nginx:alpine

# Copiar os arquivos construídos para o diretório do Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Expor a porta 80 para o Nginx
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]