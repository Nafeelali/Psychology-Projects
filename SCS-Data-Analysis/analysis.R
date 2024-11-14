# Load necessary libraries
library(tidyverse)

# Load the data
data <- read.csv("SCS_data.csv")

# Data cleaning: Keep only valid gender responses 
data <- data %>%
  filter(gender %in% c(1, 2))  # Keep only Male (1) and Female (2)

# Perform a t-test to compare sexual compulsivity scores between males and females
t_test_result <- t.test(score ~ gender, data = data)

# Print the t-test results
print(t_test_result)

# Create a histogram of sexual compulsivity scores
ggplot(data, aes(x = score)) +
  geom_histogram(binwidth = 1, fill = "blue", color = "black", alpha = 0.7) +
  labs(title = "Distribution of Sexual Compulsivity Scores", x = "Score", y = "Frequency")

# Create a boxplot to visualize scores by gender
ggplot(data, aes(x = factor(gender), y = score)) +
  geom_boxplot() +
  labs(title = "Sexual Compulsivity Scores by Gender", x = "Gender", y = "Score")
