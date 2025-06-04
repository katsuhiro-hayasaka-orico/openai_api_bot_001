import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets["OpenAIAPI"]["openai_api_key"]

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは優秀なアシスタントAIです。"}
    ]

# チャットボットとやりとりする関数
def communicate():
    """OpenAI APIと対話し、ストリーミングで結果を表示する。"""

    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,  # ストリーミングで受信
    )

    result_area = st.empty()  # 結果を表示する空のエリアを作成
    text = ""  # テキストの初期化

    for chunk in response:
        content = chunk["choices"][0]["delta"].get("content", "")
        text += content
        result_area.write("🤖: " + text)  # テキストを更新して表示

    messages.append({"role": "assistant", "content": text})

    st.session_state["user_input"] = ""  # 入力欄を消去

# ユーザーインターフェースの構築
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

user_input = st.text_input(
    "メッセージを入力してください。",
    key="user_input",
    on_change=communicate,
)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂" if message["role"] == "user" else "🤖"
        st.write(speaker + ": " + message["content"])
