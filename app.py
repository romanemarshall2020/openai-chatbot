
import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

def get_pdf_text(pdf_docs):
    # initialized a variable call text to store all text from our PDFs
    text = ""
    #from each pdf we, started looping through all of our PDFs
    for pdf in pdf_docs:
        # we initialized one pdf_reader object for each pdf
        pdf_reader = PdfReader(pdf)
        # then we loop through all of the pages of each pdf
        for page in pdf_reader.pages:
            # extract the text from pages and append it to our text variable 
            text += page.extract_text()
    return text

def get_text_chunks(text):
    # function that takes in a few parameters and returns text chunks based on arguements recieved
    text_spiltter = CharacterTextSplitter(
        separator="\n",
        # chuunk_size determines how many characters are allowed inside of each text_chunk
        chunk_size=1000,
        chunk_overlap=20,
        length_function=len
    )
    chunks = text_spiltter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    # define our varaible that will be holding embeddings
    # needs API key in order to run
    # to embed using openAI embeddings
    key = os.getenv('OPENAI_API_KEY')
    embeddings = OpenAIEmbeddings(openai_api_key=key)


    # INSTRUCT EMBEDDINGS
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")


    # vectoreStore variable is the the vector storeage for our embedded data
    # takes in text chunks and embeddings variable
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    converstion_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory

    )
    return converstion_chain


def handle_userinput(user_question):

    # gets 
    response = st.session_state.conversation({'question': user_question})
    # Before i can use session state i must initialize it inside of our main function
    print(response['chat_histor'])
    st.session_state.chat_history = response['chat_history']


    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else: 
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


# test to see if application is working 
def main():
    # To load all API keys from .env file
    load_dotenv()


    # setting page titles and adding a book imoji
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    # how to make variables persistant
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    # setting header for gui 
    st.header("Chat with multiple PDFs :books:")
    # adding input field and and description of inptu field
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)
    # chat boxes for user and for bot
    # st.write(user_template.replace("{{MSG}}", "Hello Robot"), unsafe_allow_html=True)
    # st.write(bot_template.replace("{{MSG}}", "Hello Human"), unsafe_allow_html=True)

   
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Uplaod your PDFs here and click 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get the pdf text
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)

                # create vector store
                vectorstore =  get_vectorstore(text_chunks)
                st.write(vectorstore)

                # create conversation chain
                # returns history of conversation and the next element in the conversation
                st.session_state.conversation = get_conversation_chain(vectorstore)


  
if __name__ == '__main__':
    main()