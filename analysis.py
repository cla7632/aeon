import pdfplumber
import streamlit as st

# Function to extract text sections containing "customer" from the PDF
def extract_customer_mentions(file_path):
    customer_mentions = []

    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            # Check for "customer" in text (case insensitive)
            if text:
                lines = text.split('\n')
                for line in lines:
                    if "customer" in line.lower():  # case-insensitive search for "customer"
                        customer_mentions.append((page_num, line.strip()))
    
    return customer_mentions

# Path to the PDF financial report
file_path = 'AEON-CreditQ2FYE2025-1.pdf'  # Replace with the actual file path

# Extract customer-related mentions from the PDF
customer_mentions = extract_customer_mentions(file_path)

# Streamlit Interface
st.title("AEON Credit Service: Customer Insights & Strategic Recommendations")

# --- Main Card: Total Mentions ---
st.markdown("""
<div style="background-color: #3498db; border-radius: 10px; padding: 20px; color: white; text-align: center; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
    <h2>Strategic Focus on Customer Experience & Retention in AEON’s Latest Financial Report</h2>
   
</div>
""".format(len(customer_mentions)), unsafe_allow_html=True)

# --- Breakdown Section: Categories ---
st.header("Breakdown of Mentions by Category")

# Categories for breakdown (you can customize based on keywords found)
categories = {
    "Customer Experience": [],
    "Customer Retention": [],
    "Cross-Selling": [],
    "Customer Segmentation": [],
    "Others": []
}

# Categorize mentions based on keywords or context
for page_num, mention in customer_mentions:
    mention_lower = mention.lower()
    
    if "experience" in mention_lower:
        categories["Customer Experience"].append((page_num, mention))
    elif "retention" in mention_lower:
        categories["Customer Retention"].append((page_num, mention))
    elif "cross sell" in mention_lower:
        categories["Cross-Selling"].append((page_num, mention))
    elif "segmentation" in mention_lower:
        categories["Customer Segmentation"].append((page_num, mention))
    else:
        categories["Others"].append((page_num, mention))

# Function to display mentions in cards under each category (2x2 grid)
def display_category_cards(category, mentions):
    # st.markdown(f"<h3>{category}</h3>", unsafe_allow_html=True)
    
    # Create a card for the category (1x1)
    st.markdown(f"""
  <div style="background: linear-gradient(to right, #cf2182, #484886); border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
    <h4>{category}</h4>
    <p>{len(mentions)} mentions found under this category</p>
</div>
    """, unsafe_allow_html=True)
    
    # Arrange mentions in 2x2 grid (2 cards per row)
    if mentions:
        num_cards = len(mentions)
        for i in range(0, num_cards, 2):
            # Create two columns per row for displaying cards
            col1, col2 = st.columns(2)
            with col1:
                if i < num_cards:
                    page_num, mention = mentions[i]
                    col1.markdown(f"""
                    <div style="background-color: #002060; border-radius: 10px; padding: 15px; margin-bottom: 15px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                        <h4 style="color: #fff; margin: 0;">Page {page_num}</h4>
                        <p style="color: #fff; font-size: 14px; margin-top: 10px;">{mention}</p>
                    </div>
                    """, unsafe_allow_html=True)
            with col2:
                if i + 1 < num_cards:
                    page_num, mention = mentions[i + 1]
                    col2.markdown(f"""
                    <div style="background-color: #002060; border-radius: 10px; padding: 15px; margin-bottom: 15px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                        <h4 style="color: #fff; margin: 0;">Page {page_num}</h4>
                        <p style="color: #fff; font-size: 14px; margin-top: 10px;">{mention}</p>
                    </div>
                    """, unsafe_allow_html=True)

# Display categories with their respective mentions (2x2 grid)
for category, mentions in categories.items():
    display_category_cards(category, mentions)

# --- Recommendations Based on Insights ---
st.header("Strategic Recommendations")

# Insights and action points
st.markdown("""
Based on AEON's focus, the following recommendations aim to further enhance the customer experience and optimize customer retention:

1. **Enhance Digital Experience**: 
   Continuously refine its digital platforms, ensuring a seamless, user-friendly experience across all channels. Integrating AI chatbots for real-time assistance could improve customer satisfaction.
   
2. **Focus on High-Risk Customers**: 
   By identifying early signs of churn, AEON can proactively reach out to at-risk customers with personalized offers or solutions. Predictive analytics can be used to forecast customer behaviors and target retention efforts.

3. **Cross-Sell Strategies**: 
   By leveraging segmentation, AEON can target the right customers with cross-sell opportunities. Analyzing customer behavior and preferences could lead to higher conversion rates.

4. **Loyalty Programs**:
   AEON could integrate a loyalty program that rewards frequent usage or purchases. Offering exclusive benefits to high-value customers could increase customer lifetime value (CLV).

5. **Use Predictive Analytics**: 
   Develop and deploy machine learning models to predict customer churn, segment customers more effectively, and tailor marketing strategies based on customer behavior patterns.
""")

# --- End of Application ---
st.markdown("""
    Thank you for exploring this customer insights and recommendations! Please feel free to get in touch for further discussions.
    
    <br>
    
    <strong>Contact Information:</strong><br>
    - WhatsApp: <a href="https://api.whatsapp.com/send/?phone=60122260821&text=YO" target="_blank">Click here to message me on WhatsApp</a><br>
    - Email: <a href="mailto:youremail@example.com">cla7632@gmail.com</a><br>
    - Personal Website: <a href="https://lachieng.xyz/" target="_blank">Visit my website</a>
""", unsafe_allow_html=True)
