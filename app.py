"""main streamlit app"""
from numpy import float16
import streamlit as st
from PIL import Image
import pandas as pd
import json
import datetime

with open("./static/costs.json", "rb") as f:
    costs = json.load(f)

image = Image.open("./static/tampa.jpg")
st.title("Brians Bachelor Party Hub")

st.header("The Gang Goes to Tampa")
st.markdown(
    """
```
08/25/2022 - 08/28/2022
```
"""
)
st.image(image)


days = (datetime.datetime(2022, 8, 24) - datetime.datetime.now()).days

col1, col2, col3 = st.columns(3)
col1.metric(label="Days Remaining", value=days, delta="-1")
col2.metric("Beers to Delete", "699", "+69%")
col3.metric("Strippers to Hug", "1", "+1")


with st.expander("Activites", expanded=False):
    st.markdown("Golf ⛳ http://www.dunedingolfclub.com/")
    st.markdown("Party Boat ⛵ https://www.krakencycleboats.com/")
    st.markdown("Beach 🌊 https://www.clearwaterbeach.com/")
    st.markdown("Beer 🍻 https://beer.com/")

with st.expander("House", expanded=False):
    st.text("971 Eldorado Ave Clearwater Beach, Florida United States")
    st.markdown(
        "[Airbnb](https://www.airbnb.com/rooms/16474656?source_impression_id=p3_1655728923_8XATaewQrPn3zLq8)"
    )
    map_df = pd.DataFrame({"lat": 28.000730, "lon": -82.826840}, index=[0])
    st.map(map_df)

with st.expander("Cost Breakdown", expanded=False):
    cost_df = pd.DataFrame(costs)
    st.table(cost_df)
    total = cost_df["Per Person"].astype(float).sum()

    st.markdown(f"**Total:** {total}")
    st.markdown("**Not including food/drink")

with st.expander("Flights"):
    st.markdown("**PHL ✈️ Tampa**: 8/25")
    st.text("Look for an arrival around 2ish")
    st.markdown("**Tampa ✈️ PHL**: 8/28")
    st.text("Look for a departure around 11ish")
