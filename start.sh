#!/bin/bash

# 图像识别 Demo 快速启动脚本

echo "🧠 启动图像识别 Demo..."

# 检查虚拟环境是否存在
if [ ! -d "venv_py311" ]; then
    echo "❌ 虚拟环境不存在，请先按照 README 安装依赖"
    exit 1
fi

# 激活虚拟环境
echo "📦 激活虚拟环境..."
source venv_py311/bin/activate

# 检查 Python 版本
python_version=$(python --version 2>&1)
echo "🐍 当前 Python 版本: $python_version"

# 启动应用
echo "🚀 启动应用..."
echo "📱 应用将在浏览器中打开: http://127.0.0.1:7860"
echo "⏹️  按 Ctrl+C 停止应用"
echo ""

python app.py 