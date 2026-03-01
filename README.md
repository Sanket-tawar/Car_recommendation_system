# Cars24 Car Recommendation System 🚗

This project builds a **used car recommendation system** using data scraped from Cars24.  
It recommends similar cars based on vehicle features such as name, variant, fuel type, and transmission.

The project demonstrates an **end-to-end data science workflow**, including web scraping, data preprocessing, recommendation modeling, and web app deployment.

## Project Pipeline

1. **Data Acquisition (Web Scraping)**
   - Scraped used car listings from Cars24 Pune pages.
   - Extracted fields such as car URL, image URL, name, variant, price, location, EMI, fuel type, transmission, and registration.

2. **Data Cleaning & Preprocessing**
   - Standardized column names.
   - Converted price values into numerical format.
   - Cleaned KM driven values.
   - Handled missing or inconsistent data.

3. **Recommendation System**
   - Created a **tags feature** combining important car attributes.
   - Used **CountVectorizer** to convert text features into vectors.
   - Applied **Cosine Similarity** to compute similarity between cars.
   - Generated top 5 similar car recommendations.

4. **Web Application (Streamlit)**
   - Built an interactive UI using Streamlit.
   - Features:
     - Car selection dropdown
     - Price range filter
     - Fuel type filter
     - Car images display
     - Direct link to view the car on Cars24

## Tech Stack

- Python
- Pandas
- BeautifulSoup
- Scikit-learn
- Streamlit
- Jupyter Notebook

## Project Structure
