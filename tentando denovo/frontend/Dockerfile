# Use uma imagem base de Node.js
FROM node:18

# Define o diretório de trabalho
WORKDIR /app

# Copie os arquivos do frontend para o container
COPY . .

# Instale o servidor estático http-server
RUN npm install -g http-server

# Exponha a porta 8080
EXPOSE 8080

# Comando para iniciar o servidor
CMD ["http-server", ".", "-p", "8080"]