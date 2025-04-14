import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from helper_utils import clean_text
# Sidebar contents
with st.sidebar:
    st.title("🤗💬 LLM Chat App")
    st.markdown(
        """
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [PaLM](https://makersuite.google.com/app/home) Embeddings & LLM model
 
    """
    )
    add_vertical_space(5)
    st.write("Made with ❤️ by [Dharmik](https://github.com/codemasterds)")



def main():
    st.header("Chat with PDF")
    
    
    #upload a PDF file
    pdf= st.file_uploader("Upload your PDF", type="pdf")
    
    if pdf:
        #read the PDF file
        pdf_reader= PdfReader(pdf)
        #st.write(Pdfreader)
        
        pdf_text= ""
        for page in pdf_reader.pages:
            page_text= page.extract_text()            
            if page_text:           
                pdf_text+= clean_text(page_text) 
                  
        #st.write(pdf_text)
        
        
        
        
        


if __name__ == "__main__":
    main()