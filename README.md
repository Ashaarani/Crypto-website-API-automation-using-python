# Crypto Website API Automation Using Python

This repository contains a Python script that automates the retrieval and analysis of cryptocurrency data. The script fetches the latest data, calculates volatility, and generates visualizations to compare the prices of various cryptocurrencies, specifically focusing on Bitcoin and Ethereum.

## Features

- Fetches cryptocurrency data from an API
- Filters data for the past year
- Calculates daily returns 
- Generates visualizations to compare the prices of Bitcoin and Ethereum

## Requirements

- Python 3.6+
- Pandas
- Seaborn
- Matplotlib
- Numpy

## Installation

1.Clone the repository:

git clone https://github.com/your-username/crypto-website-api-automation.git
cd crypto-website-api-automation

2.Install the required packages

3.Fetch the API key from a cryptocurrency site:

Sign up at a cryptocurrency data provider like CoinMarketCap or CryptoCompare.
Follow the instructions to get your API key.
Store your API key securely. You will need it to run the script.

## Script Overview
The script performs the following steps:

Load and filter data: Reads the cryptocurrency data file and filters the data for the past year.

Pivot data: Transforms the data to have timestamps as the index and cryptocurrency names as columns.

Calculate daily returns: Computes the daily percentage change in prices.

Uses Seaborn to create visualizations comparing the prices of Bitcoin and Ethereum.
