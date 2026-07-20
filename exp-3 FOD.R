# Create a sample house dataset
house_data <- matrix(c(
  3, 1500, 250000,
  5, 2200, 450000,
  4, 1800, 320000,
  6, 2800, 550000,
  5, 2400, 480000
), nrow = 5, byrow = TRUE)

colnames(house_data) <- c("Bedrooms", "Square_Footage", "Sale_Price")

# Select houses with more than 4 bedrooms
houses_gt4 <- house_data[house_data[, "Bedrooms"] > 4, ]

# Calculate average sale price
average_price <- mean(houses_gt4[, "Sale_Price"])

cat("Average Sale Price =", average_price, "\n")

# Pie Chart
pie(
  houses_gt4[, "Sale_Price"],
  labels = paste("House", 1:nrow(houses_gt4)),
  col = c("skyblue", "orange", "lightgreen"),
  main = "Sale Price Distribution of Houses\nwith More Than 4 Bedrooms"
)

# Add Legend
legend(
  "topright",
  legend = paste("House", 1:nrow(houses_gt4)),
  fill = c("skyblue", "orange", "lightgreen")
)