from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from llm import llm

# --- Classification Chain ---
classify_prompt = ChatPromptTemplate.from_messages([
    (
        "system", 
        "You are a logistics assistant. Classify the given shipment report into exactly one of these four categories: "
        "delayed, damaged, lost, unknown. Output only the category name in lowercase with no extra text."
    ),
    ("human", "{report_text}")
])
classify_chain = classify_prompt | llm | StrOutputParser()


# --- Escalation Chain ---
escalate_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a senior logistics coordinator. Draft a concise, professional internal escalation note "
        "for a manager regarding an unresolved or unknown shipment exception. Include the shipment value, "
        "a brief summary of the issue, and a clear request for review."
    ),
    ("human", "Shipment Value: ${shipment_value}\nReport Details: {report_text}")
])
escalate_chain = escalate_prompt | llm | StrOutputParser()


# --- Customer Email Chain ---
draft_email_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a professional and empathetic customer service representative for a logistics and shipping company. "
        "Draft a polite, reassuring customer-facing email addressing their shipment issue, explaining the situation clearly, "
        "and outlining the next steps or resolution."
    ),
    ("human", "Customer Name: {customer_name}\nShipment Value: ${shipment_value}\nIssue Details: {report_text}")
])
draft_email_chain = draft_email_prompt | llm | StrOutputParser()