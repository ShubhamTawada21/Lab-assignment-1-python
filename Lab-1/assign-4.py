# Data Analysis and Visualization with Real-World Weather Data
# Author: Shubham
# Roll no. : 2501730210
# Date: 24 November 2025
# Course: Programming for Problem Solving using Python
import pandas as pd
import matplotlib.pyplot as plt
import os
def task1_load_and_inspect_data():
    file_path = "weather_data.csv"

    
    if not os.path.exists(file_path):
        print("\n❌ ERROR: 'weather_data.csv' is missing!")
        print("👉 Place 'weather_data.csv' in the SAME folder as lab4.py\n")
        return None

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        print("\n❌ ERROR: weather_data.csv is empty!")
        return None

    print("\n===================")
    print(" TASK 1: WEATHER DATA LOADED")
    print("===================\n")

    print("🔹 First 5 rows:")
    print(df.head(), "\n")

    print("🔹 Basic Info:")
    print(df.info(), "\n")

    print("🔹 Statistical Summary:")
    print(df.describe(), "\n")

    return df



def task2_missing_values(df):
    print("\n===================")
    print(" TASK 2: MISSING VALUE HANDLING")
    print("===================\n")

    print("🔹 Missing values per column:")
    print(df.isnull().sum(), "\n")

    # Fill numeric missing values with mean
    df_filled = df.fillna(df.mean(numeric_only=True))

    print("✅ Missing values handled successfully using column-wise mean.\n")
    return df_filled



def task3_filter_temperature(df):
    print("\n===================")
    print(" TASK 3: DATA FILTERING")
    print("===================\n")

    if "Temperature" not in df.columns:
        print("❌ ERROR: 'Temperature' column not found in weather_data.csv")
        return df

    avg_temp = df["Temperature"].mean()

    print(f"🔹 Average Temperature = {avg_temp:.2f}")

    filtered_df = df[df["Temperature"] > avg_temp]

    print("\n🔹 Days with ABOVE AVERAGE temperature:")
    print(filtered_df.head(), "\n")

    return filtered_df



def task4_visualizations(df):
    print("\n===================")
    print(" TASK 4: PLOTTING & VISUALIZATION")
    print("===================\n")

   
    if "Temperature" in df.columns:
        plt.figure(figsize=(8, 4))
        plt.plot(df["Temperature"])
        plt.title("Temperature Trend Over Time")
        plt.xlabel("Day Index")
        plt.ylabel("Temperature (°C)")
        plt.grid(True)
        plt.show()
        print("📈 Temperature line plot displayed.\n")
    else:
        print("❌ 'Temperature' column missing – skipping temperature plot.\n")

    
    if "Rainfall" in df.columns:
        plt.figure(figsize=(8, 4))
        plt.bar(df.index, df["Rainfall"])
        plt.title("Rainfall Distribution")
        plt.xlabel("Day Index")
        plt.ylabel("Rainfall (mm)")
        plt.grid(True)
        plt.show()
        print("🌧 Rainfall bar chart displayed.\n")
    else:
        print("❌ 'Rainfall' column missing – skipping rainfall plot.\n")



if _name_ == "_main_":
    df = task1_load_and_inspect_data()

    if df is not None:
        df = task2_missing_values(df)
        filtered_df = task3_filter_temperature(df)
        task4_visualizations(df)

    print("\n🎯 WEATHER DATA ANALYSIS COMPLETED SUCCESSFULLY!\n")