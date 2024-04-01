import streamlit as st
import requests
import time
import random


def call_apiv2(prompt, api_key):
    start_time = time.time()  # Record start time
    url = "https://api.worqhat.com/api/ai/images/generate/v2"
    payload = {
        "orientation": "square",
        "output_type": "url",
        "prompt": [prompt]
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    end_time = time.time()  # Record end time
    duration = end_time - start_time  # Calculate duration
    if response.status_code == 200:
        return response.json()['image'], round(duration, 2)
    else:
        return None, round(duration, 2)


def call_apiv3(prompt, api_key):
    start_time = time.time()  # Record start time
    url = "https://api.worqhat.com/api/ai/images/generate/v3"
    payload = {
        "orientation": "square",
        "output_type": "url",
        "prompt": [prompt]
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    end_time = time.time()  # Record end time
    duration = end_time - start_time  # Calculate duration
    if response.status_code == 200:
        return response.json()['image'], round(duration, 2)
    else:
        return None, round(duration, 2)


st.title("Compare ImageCon V2 and ImageCon V3 Capabilities")
st.markdown(
    "**ImageCon V2 & ImageCon V3:** Enter a descriptive text to generate an image.")


prompt = st.text_input("Enter prompt:")
api_key = st.text_input("Enter Worqhat API Key:", type="password")

col1, col2 = st.columns([1,1])

st.write(prompt)

if st.button("Send"):
    st.write("Generating Image...")
    response_v2, duration_v2 = call_apiv2(prompt, api_key)
    with col1:
        st.image(
            response_v2, caption=f"Generated Image (v2) - Time taken: {duration_v2} seconds", use_column_width=True)
    response_v3, duration_v3 = call_apiv3(prompt, api_key)
    with col2:
        st.image(
            response_v3, caption=f"Generated Image (v3) - Time taken: {duration_v3} seconds", use_column_width=True)

if st.button("Surprise Me !"):
    st.write("Generating Image...")
    prompts = ["ethereal glowing holographic crystalised moth on a frosty spring morning", "high quality, 8K Ultra HD, A beautiful double exposure that combines an goddess silhouette with sunset coast, sunset coast should serve as the underlying backdrop, with its details incorporated into the goddess , crisp lines, The background is monochrome, sharp focus, double exposure, awesome full color",
               "A cat bunny hybrid", "whimiscally cute and adorable little baby foxy cuteness overload, wonderfully dreamy atmosphere filled with a whimsical mix of pastel colors, with, golden shaded background, huge flower explosion"]
    prompt = random.choice(prompts)
    response_v2, duration_v2 = call_apiv2(prompt, api_key)
    with col1:
        st.image(
            response_v2, caption=f"Generated Image (v2) - Time taken: {duration_v2} seconds", use_column_width=True)
    response_v3, duration_v3 = call_apiv3(prompt, api_key)
    with col2:
        st.image(
            response_v3, caption=f"Generated Image (v3) - Time taken: {duration_v3} seconds", use_column_width=True)

st.write("These APIs enable the generation of images from textual descriptions, offering two versions with varying capabilities. Version 3 is more powerful, accurate, and provides better results compared to Version 2.")

st.markdown(
    "For more information, visit the [Documentation page](https://docs.worqhat.com/ai-models/image-generation/imagecon-v3) and the [API Reference page](https://docs.worqhat.com/api-reference/ai-models/image-generation/imagecon-v3).")
