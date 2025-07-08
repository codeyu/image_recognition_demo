import gradio as gr
from detector_deepface import analyze_face
from detector_yolo import analyze_object

with gr.Blocks(title="图像识别 Demo") as demo:
    gr.Markdown("# 🧠 图像识别 Demo（人脸 & 物体）")

    with gr.Tabs():
        with gr.Tab("👤 人脸识别（性别 / 年龄 / 情绪）"):
            face_input = gr.Image(type="filepath", label="上传图片或拍摄")
            face_output = gr.Textbox()
            face_button = gr.Button("开始识别")
            face_button.click(fn=analyze_face, inputs=face_input, outputs=face_output)

        with gr.Tab("📦 物体识别（YOLOv8）"):
            obj_input = gr.Image(type="filepath", label="上传图片或拍摄")
            obj_output = gr.Image(type="filepath", label="识别结果")
            obj_button = gr.Button("开始识别")
            obj_button.click(fn=analyze_object, inputs=obj_input, outputs=obj_output)

demo.launch()