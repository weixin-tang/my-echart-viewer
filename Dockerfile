# 使用官方 Python 运行时作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将 requirements.txt 复制到工作目录
COPY requirements.txt .

# 安装所有依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 将应用代码复制到工作目录
COPY main.py .
COPY templates/ ./templates/

# 暴露应用运行的端口
EXPOSE 8091

# 定义运行应用的命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8091"]