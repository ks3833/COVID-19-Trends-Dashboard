import kagglehub

path = kagglehub.dataset_download("bolkonsky/covid19")

print("Path to dataset files:", path)

import os

print("Dataset folder:", path)
print(os.listdir(path))


import pandas as pd

file_path = r"C:\Users\USER\.cache\kagglehub\datasets\bolkonsky\covid19\versions\1\owid-covid-data.csv"

df = pd.read_csv(file_path)

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

countries = [
    "India",
    "United States",
    "Brazil",
    "United Kingdom"
]

df = df[df["location"].isin(countries)]
df["date"] = pd.to_datetime(df["date"])

import matplotlib.pyplot as plt

latest_cases = df.groupby("location")["total_cases"].max()

plt.figure(figsize=(8,5))
latest_cases.plot(kind="bar")
plt.title("Total COVID Cases by Country")
plt.ylabel("Cases")
plt.show()

india = df[df["location"] == "India"]

plt.figure(figsize=(12,6))
plt.plot(india["date"], india["new_cases"])
plt.title("Daily COVID Cases in India")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.grid(True)
plt.show()

peak = india.loc[india["new_cases"].idxmax()]
import os
import pandas as pd
import matplotlib.pyplot as plt

# Download dataset
path = kagglehub.dataset_download("bolkonsky/covid19")

print("Path to dataset files:", path)
print("Dataset folder:", path)
print(os.listdir(path))

# Load dataset
file_path = os.path.join(path, "owid-covid-data.csv")

df = pd.read_csv(file_path)

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# Select countries
countries = [
    "India",
    "United States",
    "Brazil",
    "United Kingdom"
]

df = df[df["location"].isin(countries)]

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# ---------------------------
# Total Cases by Country
# ---------------------------
latest_cases = df.groupby("location")["total_cases"].max()

plt.figure(figsize=(8, 5))
latest_cases.plot(kind="bar")
plt.title("Total COVID Cases by Country")
plt.ylabel("Cases")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

# ---------------------------
# India COVID Waves
# ---------------------------
india = df[df["location"] == "India"]

plt.figure(figsize=(12, 6))
plt.plot(india["date"], india["new_cases"])
plt.title("Daily COVID Cases in India")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------
# Peak COVID Day in India
# ---------------------------
peak = india.loc[india["new_cases"].idxmax()]

print("\nPeak COVID Day in India")
print("Date:", peak["date"])
print("New Cases:", int(peak["new_cases"]))

# ---------------------------
# Total Deaths by Country
# ---------------------------
deaths = df.groupby("location")["total_deaths"].max()

plt.figure(figsize=(8, 5))
deaths.plot(kind="bar")
plt.title("Total COVID Deaths by Country")
plt.ylabel("Deaths")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

# ---------------------------
# Death Rate Analysis
# ---------------------------
latest = df.groupby("location").last()

latest["death_rate"] = (
    latest["total_deaths"] / latest["total_cases"]
) * 100

print("\nDeath Rate (%)")
print(latest["death_rate"])

plt.figure(figsize=(8, 5))
latest["death_rate"].plot(kind="bar")
plt.title("COVID Death Rate by Country")
plt.ylabel("Death Rate (%)")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

# ---------------------------
# Export Cleaned Data
# ---------------------------
df.to_csv("cleaned_covid_data.csv", index=False)

print("\nCleaned dataset exported successfully!")
print("File saved as: cleaned_covid_data.csv")

print("\nPeak COVID Day in India")
print("Date:", peak["date"])
print("New Cases:", int(peak["new_cases"]))

print(df.columns.tolist())
deaths = df.groupby("location")["total_deaths"].max()

plt.figure(figsize=(8,5))
deaths.plot(kind="bar")
plt.title("Total COVID Deaths by Country")
plt.ylabel("Deaths")
plt.show()


plt.figure(figsize=(12,6))

for country in countries:
    country_df = df[df["location"] == country]
    plt.plot(
        country_df["date"],
        country_df["new_cases"],
        label=country
    )

plt.title("COVID Cases Comparison Across Countries")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.grid(True)
plt.show()

df.to_csv("cleaned_covid_data.csv", index=False)