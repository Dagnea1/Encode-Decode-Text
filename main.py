import streamlit as st

from app import encode, decode, load_lookup_table

load_lookup_table()

# State
if 'output' not in st.session_state:
    st.session_state["output"] = ""

# UI
st.title("WordGame")
input_text = st.text_area("Enter Input Text:")

columns = st.columns([1] * 7)
with columns[-1]:
    encode_btn = st.button("Encode")

with columns[-2]:
    decode_btn = st.button("Decode")

if encode_btn:
    output = encode(input_text)
    st.session_state["output"] = output
elif decode_btn:
    output = decode(input_text)
    st.session_state["output"] = output

if st.session_state["output"]:
    st.text("Output:")
    st.code(st.session_state["output"], language="text")
