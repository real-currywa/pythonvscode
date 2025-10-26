import streamlit as st

bill = 0

st.header("Kore FastFood Corp")

st.image('https://cdn.britannica.com/98/235798-050-3C3BA15D/Hamburger-and-french-fries-paper-box.jpg')

st.subheader('Food')

food1,food2,food3,food4 = st.columns(4)



with food1:
    if st.checkbox('Rice & Chicken $10'):
        bill += 10
        st.success('OK Done')
        

with food2:
    if st.checkbox('Pasta & Sauce: $7'):
        bill += 7
        st.success('OK Done')

with food3:
    if st.checkbox('Yam & Egg $4'):
        bill += 4
        st.success('OK Done')

with food4:
    if st.checkbox('Chicken & Chips $6'):
        bill += 6
        st.success('OK Done')

st.subheader('Drinks')

drink1,drink2,drink3,drink4 = st.columns(4)

with drink1:
    if st.checkbox('Fruit Cocktail $3'):
        bill += 3
        st.success('OK Done')

with drink2:
    if st.checkbox("Fanta $1"):
        bill += 1
        st.success('OK Done')

with drink3:
    if st.checkbox("Coke $1"):
        bill += 1
        st.success('OK Done')

with drink4:
    if st.checkbox("Sprite $1"):
        bill += 1
        st.success('OK Done')

st.subheader('Fruits')


fruit1,fruit2,fruit3,fruit4 = st.columns(4)

with fruit1:
    if st.checkbox("Apple $2"):
        bill += 2
        st.success('OK Done')

with fruit2:
    if st.checkbox("Orange $2"):
        bill += 2
        st.success('OK Done')

with fruit3:
    if st.checkbox("Banana $2"):
        bill += 2
        st.success('OK Done')

with fruit4:
    if st.checkbox("Mango $2"):
        bill += 2
        st.success('OK Done')

st.subheader('Snacks')

snack1,snack2,snack3,snack4 = st.columns(4)

with snack1:
    if st.checkbox("Pringles $2"):
        bill += 2
        st.success('OK Done')

with snack2:
    if st.checkbox("Biscuit $1"):
        bill += 1
        st.success('OK Done')

with snack3:
    if st.checkbox("Popcorn $2"):
        bill += 2
        st.success('OK Done')

with snack4:
    if st.checkbox("ChinChin $1"):
        bill += 1
        st.success('OK Done')

if st.button("Check my bill."):
   st.success(f"Your bill is ${bill}")






