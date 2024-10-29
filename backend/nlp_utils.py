from llama_index import LlamaIndex

# Load pre-trained LlamaIndex model or another NLP model as needed
llama_index = LlamaIndex()

def get_answer(document_content, question):
    context = document_content
    return llama_index.ask(question, context)
