
student_scores <- matrix(c(
  85, 78, 90, 88,
  92, 81, 85, 87,
  76, 89, 84, 91,
  88, 90, 86, 85
), nrow = 4, byrow = TRUE)

# Subject names
subjects <- c("Math", "Science", "English", "History")

# Average marks of each subject
average_scores <- colMeans(student_scores)

# Display averages
print(average_scores)

# Bar Graph
barplot(
  average_scores,
  names.arg = subjects,
  col = c("red", "blue", "green", "orange"),
  main = "Average Score of Each Subject",
  xlab = "Subjects",
  ylab = "Average Marks",
  ylim = c(0, 100)
)