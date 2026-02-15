# 🐼 Pandas Data Cleaning Practice Project

**Dataset:** Best-Selling Video Games

## 📌 Project Overview

This project focuses on **cleaning and preparing a real-world dataset** containing information about the best-selling video games of all time.
The dataset contains multiple inconsistencies, missing values, and structural errors that required thoughtful data-cleaning strategies using **Pandas**.

The goal of this project is to practice **practical data wrangling**, not just basic transformations.

---

## 📊 Dataset Description

The dataset includes information such as:

* Game rank
* Title
* Platform(s)
* Release year
* Sales (in millions)
* Publisher(s)
* Series

Some columns were inconsistently formatted or contained misplaced values due to the dataset being sourced from a scraped table.

---

## 🧹 Data Cleaning Steps

### 1️⃣ Rank Column Cleaning

* The `Rank` column contained non-numeric values and references.
* Since the dataset was originally ordered from best to worst rank:

  * Valid numeric ranks were preserved
  * Invalid or missing ranks were replaced using the row position
* Any corrupted rank values were appended to the game title to avoid data loss

---

### 2️⃣ Dropping Irrelevant Columns

* `Ref.` and `Table_Number` were removed because:

  * They provided no analytical value
  * They contained mostly empty or metadata-only values

---

### 3️⃣ Release Year Correction

* The `Releaseyear` column contained:

  * Non-numeric characters
  * Misplaced values stored in the `Platform(s)` column
* Cleaning steps:

  * Removed non-numeric characters
  * Enforced a 4-digit year format (`YYYY`)
  * Detected invalid years (outside 1900–2099)
  * Swapped misplaced values between `Releaseyear` and `Platform(s)`
* Final output ensures consistent and valid year formatting

---

### 4️⃣ Sales Data Handling

* Converted `Sales(millions)` to numeric values
* Rows without valid sales data were removed
* Sales values were cast to integers for consistency

---

### 5️⃣ Missing Categorical Data

* Filled missing values with meaningful defaults:

  * `Publisher(s)` → **"Unknown"**
  * `Series` → **"Indie Game"**

This preserves dataset completeness without introducing misleading numeric assumptions.

---

## 🛠 Tools & Technologies

* **Python**
* **Pandas**
* **Regex**
* **CSV data processing**

---

## 🎯 Skills Demonstrated

* Data cleaning and validation
* Handling corrupted and misplaced values
* Regex-based text cleaning
* Conditional column swapping
* Type casting and missing data strategies
* Writing reproducible, well-documented code

     

