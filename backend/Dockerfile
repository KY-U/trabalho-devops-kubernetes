#Use a imagem oficial do Python
FROM python:3.9-slim

#Define o diretório de trabalho dentro do container
WORKDIR /app

#Copie o arquivo requirements.txt para o container
COPY requirements.txt .

#Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

#Copie o conteúdo do diretório atual para o diretório de trabalho no container
COPY . .

#Expõe a porta que o Flask utilizará
EXPOSE 5000

#Variáveis de ambiente
ENV DB_HOST=mysql-service
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV DB_NAME=catalogo

#Copie o script de espera
COPY wait_for_mysql.py /app/wait_for_mysql.py

#Adicione o script para aguardar o MySQL e iniciar o backend
CMD ["sh", "-c", "python wait_for_mysql.py && python main.py"]