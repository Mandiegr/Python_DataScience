library(tidyverse)
library(caret)
library(dslabs)
data(heights)

# definir o resultado e os preditores
y <- heights$sex
x <- heights$height

#gerar conjuntos de treinamento e teste
set.seed(2007)
test_index <- createDataPartition(y, times = 1, p = 0.5, list = FALSE)
test_set <- heights[test_index, ]
train_set <- heights[-test_index, ]

#adivinhe o resultado
y_hat <- sample(c("Male", "Female"), length(test_index), replace = TRUE) %>% 
  factor(levels = levels(test_set$sex))


# precisão computacional
mean(y_hat == test_set$sex)

# compare alturas de homens e mulheres em nosso conjunto de dados
heights %>% group_by(sex) %>% summarize(mean(height), sd(height))

# agora tente prever "masculino" se a altura estiver dentro de 2 DP da média masculina
y_hat <- ifelse(x > 62, "Male", "Female") %>% factor(levels = levels(test_set$sex))
mean(y == y_hat)

# examina a precisão de 10 pontos de corte
cutoff <- seq(61, 70)
accuracy <- map_dbl(cutoff, function(x){
  y_hat <- ifelse(train_set$height > x, "Male", "Female") %>% 
    factor(levels = levels(test_set$sex))
  mean(y_hat == train_set$sex)
})
data.frame(cutoff, accuracy) %>% 
  ggplot(aes(cutoff, accuracy)) + 
  geom_point() + 
  geom_line() 
max(accuracy)

best_cutoff <- cutoff[which.max(accuracy)]
best_cutoff

y_hat <- ifelse(test_set$height > best_cutoff, "Male", "Female") %>% 
  factor(levels = levels(test_set$sex))
y_hat <- factor(y_hat)
mean(y_hat == test_set$sex)