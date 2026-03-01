import streamlit as st
import pandas as pd
import pickle
df = pickle.load(open("C:\\Users\Admin\\Car_recommendation_system\\car_data.pkl","rb"))
similarity = pickle.load(open("C:\\Users\Admin\\Car_recommendation_system\\similarity.pkl","rb"))


# UI
def recommend(car_name):

    car_index = df[df['name'] == car_name].index[0]

    distances = similarity[car_index]

    car_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    cars = []

    for i in car_list:
        cars.append(df.iloc[i[0]])

    return cars


def format_price(price):
    return f"₹{price/100000:.2f} Lakh"


st.title("🚗 Cars24 Car Recommendation System")

st.sidebar.header("Filters")

min_price = int(df['price'].min())
max_price = int(df['price'].max())

price_range = st.sidebar.slider(
    "Price Range",
    min_price,
    max_price,
    (min_price, max_price)
)

fuel_option = st.sidebar.selectbox(
    "Fuel Type",
    ["All"] + list(df['fuel type'].unique())
)

filtered_df = df[
    (df['price'] >= price_range[0]) &
    (df['price'] <= price_range[1])
]

if fuel_option != "All":
    filtered_df = filtered_df[
        filtered_df['fuel type'] == fuel_option
    ]

selected_car = st.selectbox(
    "Select a Car",
    filtered_df['name'].values
)

if st.button("Recommend Cars"):

    recommendations = recommend(selected_car)

    cols = st.columns(5)

    for idx, car in enumerate(recommendations):

        with cols[idx]:

            st.image(car['image url'])

            st.markdown(f"**{car['name']}**")

            st.write(car['variant'])

            st.write(format_price(car['price']))

            st.write(
                f"{car['fuel type']} | {car['transmission']}"
            )

            st.markdown(
                f"[View Car]({car['car url']})"
            )
