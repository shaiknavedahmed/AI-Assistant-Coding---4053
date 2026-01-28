#problem statement-1
'''Billing:“I was charged twice for my subscription this month. Please resolve this issue.”
Technical Support:“The mobile app crashes every time I try to log in.”
Feedback:“I really like the new dashboard design. Its much easier to use.”
Others:“I want to know your office working hours during holidays.”
Billing:“Can you send me a copy of last months invoice?”

Classify the following customer email into one of these categories: Billing, Technical Support, Feedback, Others.
Return only the category name.'''
def classify_email(email):
    billing_keywords = ["charged", "subscription", "invoice", "payment", "billing"]
    technical_support_keywords = ["crashes", "log in", "error", "bug", "technical issue"]
    feedback_keywords = ["like", "dislike", "suggestion", "feedback", "improvement"]
    
    email_lower = email.lower()
    
    if any(keyword in email_lower for keyword in billing_keywords):
        return "Billing"
    elif any(keyword in email_lower for keyword in technical_support_keywords):
        return "Technical Support"
    elif any(keyword in email_lower for keyword in feedback_keywords):
        return "Feedback"
    else:
        return "Others"
# Example usage
email = "I was charged twice for my subscription this month. Please resolve this issue."
category = classify_email(email)
print(category)  # Output: Billing

'''Classify the customer email into one of these categories:
Billing, Technical Support, Feedback, Others.

Example:
Email: I was charged twice for my subscription.
Category: Billing'''
def classify_email(email):
    billing_keywords = ["charged", "subscription", "invoice", "payment", "billing"]
    technical_support_keywords = ["crashes", "log in", "error", "bug", "technical issue"]
    feedback_keywords = ["like", "dislike", "suggestion", "feedback", "improvement"]
    
    email_lower = email.lower()
    
    if any(keyword in email_lower for keyword in billing_keywords):
        return "Billing"
    elif any(keyword in email_lower for keyword in technical_support_keywords):
        return "Technical Support"
    elif any(keyword in email_lower for keyword in feedback_keywords):
        return "Feedback"
    else:
        return "Others"
# Example usage
email = "The mobile app crashes every time I try to log in."
category = classify_email(email)
print(category)  # Output: Technical Support
''''''

'''Classify the customer email into one of these categories: Billing, Technical Support, Feedback, Others.
Examples: Email: My card was charged extra this month. Category: Billing
Email: The app crashes whenever I open it. Category: Technical Support
Email: I really like the new app design. Category: Feedback'''
def classify_email(email):
    billing_keywords = ["charged", "subscription", "invoice", "payment", "billing"]
    technical_support_keywords = ["crashes", "log in", "error", "bug", "technical issue"]
    feedback_keywords = ["like", "dislike", "suggestion", "feedback", "improvement"]
    
    email_lower = email.lower()
    
    if any(keyword in email_lower for keyword in billing_keywords):
        return "Billing"
    elif any(keyword in email_lower for keyword in technical_support_keywords):
        return "Technical Support"
    elif any(keyword in email_lower for keyword in feedback_keywords):
        return "Feedback"
    else:
        return "Others"
# Example usage
email = "I really like the new dashboard design. Its much easier to use."
category = classify_email(email)
print(category)  # Output: Feedback








#problem statement-2 
'''| Query No. | User Query                                                      | Intent           |
| --------- | --------------------------------------------------------------- | ---------------- |
| 1         | “I can’t log into my account even after resetting my password.” | Account Issue    |
| 2         | “Where is my order? It was supposed to arrive yesterday.”       | Order Status     |
| 3         | “Does this phone support 5G and wireless charging?”             | Product Inquiry  |
| 4         | “What are your customer support working hours?”                 | General Question |
| 5         | “My account was locked after multiple failed login attempts.”   | Account Issue    |
| 6         | “Can I track my order using my mobile number?”                  | Order Status     |
'''

'''Classify the following user query into one of these intents:
Account Issue, Order Status, Product Inquiry, General Question.
Return only the intent name.'''
def classify_query(query):
    account_issue_keywords = ["log into my account", "password", "account locked", "failed login"]
    order_status_keywords = ["where is my order", "track my order", "order status", "arrive"]
    product_inquiry_keywords = ["support 5g", "wireless charging", "product inquiry", "features"]
    
    query_lower = query.lower()
    
    if any(keyword in query_lower for keyword in account_issue_keywords):
        return "Account Issue"
    elif any(keyword in query_lower for keyword in order_status_keywords):
        return "Order Status"
    elif any(keyword in query_lower for keyword in product_inquiry_keywords):
        return "Product Inquiry"
    else:
        return "General Question"
# Example usage
query = "I can’t log into my account even after resetting my password."
intent = classify_query(query)
print(intent)  # Output: Account Issue


'''Classify the following user query into one of these intents: Account Issue, Order Status, Product Inquiry, General Question.
Example: User Query: I forgot my password and cannot access my account. Intent: Account Issue'''
def classify_query(query):
    account_issue_keywords = ["log into my account", "password", "account locked", "failed login"]
    order_status_keywords = ["where is my order", "track my order", "order status", "arrive"]
    product_inquiry_keywords = ["support 5g", "wireless charging", "product inquiry", "features"]
    
    query_lower = query.lower()
    
    if any(keyword in query_lower for keyword in account_issue_keywords):
        return "Account Issue"
    elif any(keyword in query_lower for keyword in order_status_keywords):
        return "Order Status"
    elif any(keyword in query_lower for keyword in product_inquiry_keywords):
        return "Product Inquiry"
    else:
        return "General Question"
# Example usage
query = "Where is my order? It was supposed to arrive yesterday."
intent = classify_query(query)
print(intent)  # Output: Order Status





'''Classify the following user query into one of these intents:
Account Issue, Order Status, Product Inquiry, General Question.

Examples:
User Query: My account got locked after too many login attempts.
Intent: Account Issue

User Query: When will my order be delivered?
Intent: Order Status

User Query: Does this laptop come with a warranty?
Intent: Product Inquiry

User Query: What payment methods do you accept?
Intent: General Question'''
def classify_query(query):
    account_issue_keywords = ["log into my account", "password", "account locked", "failed login"]
    order_status_keywords = ["where is my order", "track my order", "order status", "arrive"]
    product_inquiry_keywords = ["support 5g", "wireless charging", "product inquiry", "features"]
    
    query_lower = query.lower()
    
    if any(keyword in query_lower for keyword in account_issue_keywords):
        return "Account Issue"
    elif any(keyword in query_lower for keyword in order_status_keywords):
        return "Order Status"
    elif any(keyword in query_lower for keyword in product_inquiry_keywords):
        return "Product Inquiry"
    else:
        return "General Question"
# Example usage
query = "Does this phone support 5G and wireless charging?"
intent = classify_query(query)
print(intent)  # Output: Product Inquiry
