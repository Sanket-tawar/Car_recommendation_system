 📊 Cars24 Car Recommendation System | Streamlit

📌 Project Overview

This project features an interactive, web-based Car Recommendation System built using Streamlit. By processing comprehensive used car data, the application allows users to search for vehicles, apply custom filters, and receive intelligent recommendations based on similarity metrics.
The goal of this project is to bridge the gap between complex machine learning recommendation engines and an intuitive, user-friendly interface that assists buyers in making informed purchasing decisions.

🎯 Business Objective

The primary objective of this system is to streamline the used car discovery process by providing relevant alternatives to a user's vehicle of interest.
Key business questions addressed include:
How can content-based filtering effectively recommend similar vehicles?
How can dynamic, real-time sidebar filters restrict options based on budget and fuel preference?
How can a responsive frontend handle dataset updates seamlessly to present instantaneous recommendations?

🛠️ Tools & Technologies

Streamlit – Frontend application framework and UI deployment
Python – Core programming logic and application backend
Pandas & NumPy – Data manipulation, filtering, and pre-processing
Scikit-Learn – Similarity algorithms and feature vectorization

 
File Description

FileDescriptionapp.pyCore Python script containing the Streamlit UI and recommendation logic.dataset.csvPre-processed source dataset containing used car attributes.Screenshot 2026-06-13 144639.pngLanding page preview showing the primary layout and baseline features.Screenshot 2026-06-13 144723.pngLive application preview illustrating interactive filters and dropdown behavior.

📋 Dataset Overview

The dataset contains information related to:
Car Model / Variant
Manufacturing Year
Price Tiers
Fuel Type (Petrol, Diesel, CNG, Electric)
Kilometers Driven
Transmission Type
The data was cleaned, transformed, and modeled before creating visual reports.

🔄 Data Preparation

Data Cleaning

Removed inconsistencies and duplicate records
Handled missing values
Standardized category labels
Verified data types and formatting

Data Transformation

Created calculated measures
Structured data for reporting
Optimized fields for dashboard analysis

Data Modeling

Built relationships between relevant fields
Created DAX measures for KPI calculations
Optimized model performance

📈 Key Performance Indicators (KPIs)

KPIValueMinimum Price Boundary168,000Maximum Price Boundary2,800,000Default Selected Vehicle2012 Maruti Alto 800Active Fuel TypesPetrol, Diesel, CNG, Electric
These KPIs provide a quick overview of overall business performance and customer satisfaction.

📊 Dashboard Analysis

1. Price Range Analysis

The dashboard analyzes pricing filters across the dataset:
Minimum Threshold: 168,000
Maximum Cap: 2,800,000
Dynamic Slider Control

Key Findings

The slider dynamically scales down based on structural inputs.
Adjusting the cap instantly narrows down the target vehicle matrix.

2. Fuel Type Analysis

Products are categorized into:
Petrol
Diesel
CNG
Electric

Key Findings

Selecting specific fuel options recalculates matching models immediately.
Diesel engine queries display contextual results like the 2019 Renault Duster.

3. Selected Vehicle Baseline

Analysis performance tracks custom baseline models:
2012 Maruti Alto 800
2014 Honda City
2019 Renault Duster

Key Findings

The application maps contextual baseline choices to build similarity vectors.
Alternative variants populate instantly based on the root car chosen.

📷 Dashboard Preview

Main Interface
The user landing page initializes with a dark theme, a collapsible sidebar filter for budget/fuel configurations, and a primary selection module:
<img width="1919" height="1008" alt="Screenshot 2026-06-13 144639" src="https://github.com/user-attachments/assets/79a26d72-9c88-47c0-814a-e4e0cd4d6a4a" />

Filter Interaction
When a user updates criteria (such as setting the Fuel Type to Diesel and reducing the maximum price cap to 1,367,183), the application filters the target model matrix dynamically to display contextual matches like the 2019 Renault Duster and 2014 Honda City:
<img width="1919" height="1007" alt="Screenshot 2026-06-13 144723" src="https://github.com/user-attachments/assets/a8dbd727-3b7c-42fc-863c-37e7e427f650" />


📊 Skills Demonstrated

Streamlit

Dashboard Development
Data Modeling
Interactive Reporting
KPI Design

Data Analysis

Sales Analysis
Trend Analysis
Performance Evaluation
Business Intelligence Reporting

Python & Machine Learning

Calculated Measures
KPI Creation
Aggregation Functions

Data Pipeline Engineering

Data Management
Dataset Preparation

📚 Project Outcome

This project successfully demonstrates how Python and Streamlit can turn a static used-car dataset into an interactive digital product. By combining granular sidebar filtering with an algorithmic recommendation module, the tool provides a fluid, real-world e-commerce utility mimicking standard features utilized by global automotive platforms.
