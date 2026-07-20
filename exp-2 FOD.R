# 3 × 3 matrix
# Rows -> Products
# Columns -> Sales Prices

sales_data <- matrix(c(
  100, 120, 110,
  200, 210, 220,
  150, 160, 170
), nrow = 3, byrow = TRUE)

# Display sales data
print("Sales Data:")
print(sales_data)

# Calculate average price for each product (row-wise)
product_average <- rowMeans(sales_data)

# Calculate overall average price
overall_average <- mean(sales_data)

# Display results
cat("Average Price of Each Product:\n")
print(product_average)

cat("\nOverall Average Price of All Products Sold =", overall_average, "\n")

# Bar Graph
barplot(
  product_average,
  names.arg = c("Product 1", "Product 2", "Product 3"),
  col = c("skyblue", "orange", "lightgreen"),
  main = "Average Price of Each Product",
  xlab = "Products",
  ylab = "Average Price",
  ylim = c(0, max(product_average) + 50)
)

# Add overall average line
abline(h = overall_average, col = "red", lwd = 2, lty = 2)

# Add legend
legend("topright",
       legend = "Overall Average",
       col = "red",
       lty = 2,
       lwd = 2)