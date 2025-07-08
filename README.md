# 🧠 图像识别 Demo

一个基于 Gradio 的 Web 应用，集成了人脸识别（性别/年龄/情绪）和物体检测（YOLOv8）功能。

## ✨ 功能特性

- **人脸识别**: 使用 DeepFace 分析性别、年龄和情绪
- **物体检测**: 使用 YOLOv8 进行实时物体检测
- **Web 界面**: 基于 Gradio 的友好用户界面
- **多标签页**: 支持人脸识别和物体检测的切换

## 🛠️ 环境要求

- macOS (Apple Silicon 推荐)
- Python 3.11
- 8GB+ RAM
- 2GB+ 可用磁盘空间

## 📦 安装步骤

### 1. 克隆项目

```bash
git clone <your-repo-url>
cd image_recognition_demo
```

### 2. 安装 Python 3.11

如果你的系统没有 Python 3.11，请先安装：

```bash
# 安装 pyenv (如果还没有)
brew install pyenv

# 安装 Python 3.11.9
pyenv install 3.11.9

# 为项目设置 Python 版本
pyenv local 3.11.9
```

### 3. 创建虚拟环境

```bash
# 使用 Python 3.11 创建虚拟环境
~/.pyenv/versions/3.11.9/bin/python -m venv venv_py311

# 激活虚拟环境
source venv_py311/bin/activate
```

### 4. 安装依赖

```bash
# 升级 pip
pip install --upgrade pip

# 安装项目依赖
pip install -r requirements.txt
```

**注意**: 首次安装可能需要较长时间，因为需要下载 TensorFlow 等大型依赖包。

## 🤖 模型下载

### YOLOv8 模型

YOLOv8 模型会在首次运行时自动下载：

```bash
# 运行应用时会自动下载 yolov8n.pt 模型
python app.py
```

模型文件将保存在项目根目录，大小约 6MB。

### DeepFace 模型

DeepFace 会在首次使用时自动下载以下模型：

- **人脸检测模型**: MTCNN, RetinaFace
- **年龄预测模型**: 约 100MB
- **性别预测模型**: 约 100MB  
- **情绪识别模型**: 约 100MB

**首次运行可能需要几分钟下载时间**，请确保网络连接稳定。

## 🚀 运行应用

### 启动 Application

#### Method 1: Using Quick Start Script (Recommended)

```bash
# Use quick start script
./start.sh
```

#### Method 2: Manual Start

```bash
# Ensure virtual environment is activated
source venv_py311/bin/activate

# Start application
python app.py
```

### 访问应用

应用启动后，在浏览器中访问：
- 本地地址: `http://127.0.0.1:7860`
- 网络地址: `http://0.0.0.0:7860`

## 📱 使用说明

### 人脸识别

1. 切换到 "👤 人脸识别" 标签页
2. 上传图片或使用摄像头拍摄
3. 点击 "开始识别" 按钮
4. 查看识别结果（性别、年龄、情绪）

### 物体检测

1. 切换到 "📦 物体识别" 标签页
2. 上传图片或使用摄像头拍摄
3. 点击 "开始识别" 按钮
4. 查看检测结果（带边界框的图片）

## 📁 项目结构

```
image_recognition_demo/
├── app.py                 # 主应用文件
├── detector_deepface.py   # 人脸识别模块
├── detector_yolo.py       # 物体检测模块
├── requirements.txt       # 依赖列表
├── README.md             # 英文项目说明
├── README_中文.md        # 中文项目说明
├── start.sh              # 快速启动脚本
├── venv_py311/           # Python 3.11 虚拟环境
└── runs/                 # YOLO 检测结果输出目录
    └── detect/
        └── predict/
```

## 🔧 故障排除

### 常见问题

1. **TensorFlow 安装失败**
   - 确保使用 Python 3.11
   - 检查网络连接
   - 尝试使用国内镜像源

2. **模型下载失败**
   - 检查网络连接
   - 确保有足够的磁盘空间
   - 可以手动下载模型文件

3. **内存不足**
   - 关闭其他应用程序
   - 使用较小的图片进行测试

### 手动下载模型

如果自动下载失败，可以手动下载：

```bash
# 下载 YOLOv8 模型
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt

# 或使用 curl
curl -L https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt -o yolov8n.pt
```

## 📊 性能说明

- **人脸识别**: 首次运行较慢（需要下载模型），后续运行较快
- **物体检测**: 实时检测，支持多种物体类别
- **内存使用**: 约 2-4GB RAM
- **GPU 支持**: 自动检测并使用可用的 GPU

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

- [Gradio](https://gradio.app/) - Web 界面框架
- [DeepFace](https://github.com/serengil/deepface) - 人脸识别库
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - 物体检测模型
- [OpenCV](https://opencv.org/) - 计算机视觉库 