from deepface import DeepFace

def analyze_face(img_path):
    try:
        result = DeepFace.analyze(img_path=img_path, actions=['gender', 'age', 'emotion'], enforce_detection=False)
        info = result[0]
        return f"性别: {info['dominant_gender']}｜年龄: {info['age']}｜情绪: {info['dominant_emotion']}"
    except Exception as e:
        return f"识别失败: {str(e)}"