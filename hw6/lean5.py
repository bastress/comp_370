"""
ORIGINAL CODE:

# get all the sales data by product type
book_sales_2022 = load("data/book_sales_2022.csv")
book_sales_2023 = load("data/book_sales_2023.csv")
book_sales_2024 = load("data/book_sales_2024.csv")

game_sales_2022 = load("data/game_sales_2022.csv")
game_sales_2023 = load("data/game_sales_2023.csv")
game_sales_2024 = load("data/game_sales_2024.csv")

# calculate the total sales for each year
total_sales_2022 = sum_sales(book_sales_2022, game_sales_2022)
total_sales_2023 = sum_sales(book_sales_2023, game_sales_2023)
total_sales_2024 = sum_sales(book_sales_2024, game_sales_2024)
"""

# REWRITTEN CODE:

sale_years = [2022, 2023, 2024]
total_sales = {}

for year in sale_years:
    game_sales = load("data/game_sales_" + str(year) + ".csv")
    book_sales = load("data/book_sales_" + str(year) + ".csv")
    total_sales[year] = sum_sales(book_sales, game_sales)