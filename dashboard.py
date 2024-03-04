import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def create_avg_season_df(df):
    avg_season_df = df.groupby('season')['count'].mean()
    return avg_season_df

def create_avg_registered_df(df):
    avg_registered_df = df.groupby('year')['registered'].mean()
    return avg_registered_df

def create_avg_unregistered_df(df):
    avg_unregistered_df = df.groupby('year')['unregistered'].mean()
    return avg_unregistered_df

with st.sidebar:
    st.text('SELAMAT DATANG DI DASHBOARD')

# Load data
bike_df = pd.read_csv("bike.csv")


# Streamlit app
st.header('Bike Sharing Dashboard :bike:')

# Create dataframe
avg_season_df = create_avg_season_df(bike_df)
avg_registered_df = create_avg_registered_df(bike_df)
avg_unregistered_df = create_avg_unregistered_df(bike_df)

st.subheader("Bagaimana rata-rata peminjaman pada setiap musim?")

# Plot
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 6))
ax.bar(avg_season_df.index, avg_season_df.values, color='#FFA500')
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['Springer', 'Summer', 'Fall', 'Winter'])
ax.set_title('Mean Bike Rental Count by Season')
ax.set_xlabel('Season')
ax.set_ylabel('Average Rental Count')

# Display plot in Streamlit app
st.pyplot(fig)

with st.expander("See explanation"):
    st.write(
        """ Data menunjukan bahwa rata-rata permintaan peminjaman sepeda tertinggi terjadi di musim gugur dan permintaan terendah terjadi di musim semi. Ketiga musim lainnya terlihat berada di antara angka 200, sedangkan musim semi tidak sampai rata-rata 150 permintaan.

"""
    )

st.subheader("Bagaimana rata-rata peminjaman sepeda pada hari kerja dan hari libur?")
# Plot for registered users
tabs = st.tabs(["Registered Users", "Unregistered Users"])

with tabs[0]:
    st.header("Registered Users per Year")
    fig_registered, ax_registered = plt.subplots(figsize=(8, 6))
    ax_registered.bar(avg_registered_df.index, avg_registered_df.values, color='#2AAA8A')
    ax_registered.set_title('Mean Bike Rental Count by Registered Users')
    ax_registered.set_xlabel('Year')
    ax_registered.set_ylabel('Average Registered')
    ax_registered.set_xticks([0, 1])
    ax_registered.set_xticklabels(['2020', '2021'])
    st.pyplot(fig_registered)

with tabs[1]:
    st.header("Unregistered Users per Year")
    fig_unregistered, ax_unregistered = plt.subplots(figsize=(8, 6))
    ax_unregistered.bar(avg_unregistered_df.index, avg_unregistered_df.values, color='#2AAA8A')
    ax_unregistered.set_title('Mean Bike Rental Count by Unregistered Users')
    ax_unregistered.set_xlabel('Year')
    ax_unregistered.set_ylabel('Average Unregistered')
    ax_unregistered.set_xticks([0, 1])
    ax_unregistered.set_xticklabels(['2020', '2021'])
    st.pyplot(fig_unregistered)
with st.expander("See explanation"):
    st.write(
        """ Total rata-rata permintaan peminjaman pada tahun 2021 lebih tinggi. Hal ini juga sebanding lurus dengan naiknya jumlah permintaan dari pengguna unregistered sebesar 48.28%. Walaupun begitu, gap nilai registered dan unregistered sangatlah jauh. Angka unregistered tidak menyentuh angka 100 pada tahun 2020 dan 2021.
"""
    )



# Define weekday names
weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Filter DataFrame for holiday = 0 and 1
holiday_0 = bike_df[bike_df['holiday'] == 0]
holiday_1 = bike_df[bike_df['holiday'] == 1]

# Group by weekday and count occurrences
weekday_counts_0 = holiday_0.groupby('weekday').size()
weekday_counts_1 = holiday_1.groupby('weekday').size()

st.subheader("Bagaimana distribusi permintaan peminjaman sepeda pada hari kerja dan hari libur?")

tabs = st.tabs(["Working day", "Holiday"])

with tabs[0]:
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.pie(weekday_counts_0, labels=[weekday_names[idx] for idx in weekday_counts_0.index], autopct='%1.1f%%')
    ax1.set_title('Weekday Distribution for Working Days')
    st.pyplot(fig1)

with tabs[1]:
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    ax2.pie(weekday_counts_1, labels=[weekday_names[idx] for idx in weekday_counts_1.index], autopct='%1.1f%%')
    ax2.set_title('Weekday Distribution for Holidays')
    st.pyplot(fig2)

with st.expander("See explanation"):
    st.write(
        """Permintaan cenderung merata pada hari kerja, tetapi meningkat secara signifikan pada hari libur, terutama pada hari Selasa. 
        """
    )
