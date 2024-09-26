from transformers import pipeline
model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")

# 로컬저장하기
model.save_pretrained("./saved_model")

# 로컬 불러오기
load_model = pipeline("image-classification", model="note/saved_model")
