from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# ChatPromptTemplate creates a structured sequence of messages for chat models.
# Why don't we need SystemMessage, HumanMessage, or AIMessage classes here?
# Because LangChain provides a convenient shortcut: using tuples like ('system', 'text') or ('human', 'text').
# LangChain automatically converts these shorthand tuples into the proper Message objects under the hood!
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    
    # MessagesPlaceholder acts as a designated injection spot for a LIST of messages (like our chat history).
    # What would happen without it? 
    # If we just tried to use a string variable like ('human', 'History: {chat_history}'),
    # the entire history list would be smashed into a single, ugly text block. 
    # MessagesPlaceholder safely drops an entire list of actual Message objects right into the middle of this sequence, preserving their original structure.
    MessagesPlaceholder(variable_name='chat_history'),
    
    ('human','{query}')
])

chat_history = []
# load chat history
with open('2_Prompts/3_message_placeholder/chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)