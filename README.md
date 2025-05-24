# A Regime Switching Framework to Debunk Market Myths

Welcome to the repository for the MScFE 690 Capstone project:  
**A Regime Switching Framework to Debunk Market Myths**

This project implements a robust quantitative framework using regime-switching models to analyze, test, and debunk commonly held myths in financial markets. The approach leverages advanced statistical techniques to identify different "regimes" or market states, allowing users to rigorously challenge market adages and investment rules-of-thumb with empirical evidence.

---

## Table of Contents

- [Overview](#overview)
- [Motivation](#motivation)
- [Key Features](#key-features)
- [Methodology](#methodology)
- [How to Use](#how-to-use)
- [Results & Insights](#results--insights)
- [Project Structure](#project-structure)
- [References](#references)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Financial markets are rife with widely accepted “truths” and myths (e.g., "Sell in May and go away", "Value stocks always outperform growth stocks"). This project provides a systematic, data-driven approach to investigate the validity of such statements using regime-switching models. By segmenting market data into statistically distinct regimes, we can assess whether these myths hold under varying market conditions.

---

## Motivation

- **Critical Thinking:** Challenge and rigorously test financial clichés that often shape investment decisions.
- **Quantitative Rigor:** Move beyond anecdotal evidence to robust, reproducible statistical testing.
- **Market Understanding:** Uncover hidden dynamics and regime-dependent behaviors in financial time series.

---

## Key Features

- **Regime-Switching Models:** Employs Markov-Switching and related models to detect market regimes.
- **Myth Testing:** Framework to encode and empirically test popular market myths.
- **Visualization:** Clear, publication-quality plots to illustrate regime changes and myth validity.
- **Extensible:** Easily adapt the framework to new myths, time periods, asset classes, or geographies.

---

## Methodology

1. **Data Collection & Preparation:** 
   - Historical market data is sourced and cleaned.
2. **Modeling Regimes:** 
   - Statistical models (e.g., Markov-Switching) are fitted to the time series to identify distinct market regimes (e.g., bull vs. bear, high vs. low volatility).
3. **Encoding Myths:** 
   - Each market myth is formulated as a testable hypothesis.
4. **Empirical Testing:** 
   - Myths are tested within and across identified regimes to assess their validity.
5. **Analysis & Visualization:** 
   - Results are visualized and interpreted, highlighting when, if ever, the myths hold true.

---

## How to Use

> **Note:** This repository contains the main report (`MScFE_690_Capstone.pdf`). Source code and data (if provided) would be found in the respective directories.

1. **Clone the Repo:**
    ```bash
    git clone https://github.com/edithluv/A_Regime_Switching_Framework_to_Debunk_Market_Myths_-1-.git
    ```
2. **Read the Report:**
   - Open `MScFE_690_Capstone.pdf` for a comprehensive explanation of the framework, methods, case studies, and results.

3. **(If Code Provided) Run the Analysis:**
   - Follow instructions in `src/` or `notebooks/` (if available).
   - Install required dependencies (typically via `requirements.txt` or `environment.yml`).

---

## Results & Insights

- The regime-switching framework reveals that many market myths are **regime-dependent**: they may hold in some market states, but not others.
- Relying on myths without accounting for shifting regimes can lead to suboptimal investment decisions.
- The report contains detailed empirical results, including:
  - Regime classification plots
  - Myth validity tables across regimes
  - Case studies on well-known market adages

---

## Project Structure

```
.
├── MScFE_690_Capstone.pdf    # Main report (full methodology, results, and discussion)
├── data/                     # (If present) Raw and processed datasets
├── src/                      # (If present) Source code for modeling and analysis
├── notebooks/                # (If present) Jupyter notebooks for exploration and visualization
└── README.md                 # This file
```

---

## References

- Hamilton, J.D. (1989). "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle." *Econometrica*.
- Ang, A., & Timmermann, A. (2012). "Regime Changes and Financial Markets." *Annual Review of Financial Economics*.
- [Additional references in the report]

---

## Contributing

Contributions, suggestions, and myth ideas are welcome!  
Please open an issue or submit a pull request.

---

## License

This project is for academic and research use.  
See `LICENSE` (if provided) for details.
