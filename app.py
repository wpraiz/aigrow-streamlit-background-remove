import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## AiGrow Tools - Remove Background de Imagens")
st.write(
    ":dog: Tente fazer upload de uma imagem para ver o plano de fundo removido magicamente. Imagens de qualidade total podem ser baixadas na barra lateral."
)
# criar sidebar na esquerda
st.sidebar.image("https://aigrow.com.br/wp-content/uploads/2023/01/Ativo-3@4x.png", width=300)
st.sidebar.title("aiGrow Brazil") 
# Inserir imagem


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Imagem Original: :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Imagem Tratada :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Fazer download da imagem alterada.", convert_image(fixed), "aigrow-bg-remove-fix12333.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Enviar Imagem", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("./zebra.jpg")
