# Use uma imagem base do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que o Flask estará rodando
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]