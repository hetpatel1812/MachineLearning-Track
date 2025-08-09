# 📊 Day 7 — Matplotlib Subplots & Multiple Visualizations

## 📌 Overview  
On **Day 7** of the Machine Learning Track, we expanded our Matplotlib skills by learning how to arrange **multiple plots** in a single figure.  
We explored both the `subplot()` and `subplots()` methods to create side-by-side or grid-based visualizations for better comparisons.  

---

## 📖 Key Learning Points  

### **1. Multiple Plots with `subplot()`**  
- `plt.subplot(nrows, ncols, index)` allows adding multiple plots to one figure.
- Each subplot is indexed starting from 1.
- Example: A **Line Plot** and **Bar Plot** displayed side by side in one figure.

**Benefits:**  
- Quick way to create simple multi-plot layouts.
- Easy for small comparisons.

---

### **2. Multiple Plots with `subplots()`**  
- `fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))` creates a figure and an array of axes.
- Each `ax[i]` can be customized independently.
- Example: Customizing colors, titles, and adding a shared main title with `fig.suptitle()`.
- Used `plt.tight_layout()` to avoid overlapping elements.

**Benefits:**  
- More flexible and powerful than `subplot()`.
- Better for complex visualizations and advanced styling.

---

## 🎯 Skills Gained  
- Creating side-by-side or grid-based plots.
- Customizing individual subplots independently.
- Adding shared titles and adjusting layout spacing.
- Comparing multiple data visualizations in one figure.

---

## 📌 Why This Matters for Machine Learning  
- Enables visual comparison of different datasets or models in a single view.
- Makes presentations and reports more compact and visually clear.
- Helps identify patterns and trends faster by juxtaposing plots.

