import streamlit as st

# --- MENU DATA ---
menu = {
    'Pizza': 100,
    'Burger': 80,
    'Pasta': 60,
    'Salad': 50,
    'Coffee': 70
}

# --- APP TITLE ---
st.title("🥄The Python Restaurant")
st.write("Select your favorite dishes from the menu below 👇")

# --- MENU DISPLAY ---
st.subheader("Today's Menu")
for item, price in menu.items():
    st.write(f"**{item}** — ₹{price}")

# --- ORDER SECTION ---
st.subheader("Place Your Order")

# Allow multiple item selections
selected_items = st.multiselect(
    "Choose your items:",
    options=list(menu.keys()),
    help="You can select multiple dishes"
)

# --- ORDER CALCULATION ---
order_total = sum(menu[item] for item in selected_items)

if selected_items:
    st.success(f"✅ You’ve added: {', '.join(selected_items)}")
    st.info(f"💰 Total Amount: ₹{order_total}")
else:
    st.warning("Please select at least one item to see your total.")

# --- ORDER CONFIRMATION ---
if st.button("Place Order"):
    if selected_items:
        st.balloons()
        st.success(f"🎉 Order placed successfully! Total payable amount: ₹{order_total}")
    else:
        st.error("Please select an item before placing your order.")
