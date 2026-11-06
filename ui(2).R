library(shiny)

shinyUI(fluidPage(
  titlePanel("Car fuel economy estimate"),
  sidebarLayout(
    sidebarPanel(
      sliderInput("hp", "Engine horsepower", min = 50, max = 350,
                  value = 110, step = 10),
      radioButtons("am", "Transmission",
                   choices = c("Automatic" = 0, "Manual" = 1)),
      h4("How to use"),
      p("Choose a horsepower value and transmission. The estimated miles per gallon (MPG) updates automatically."),
      p("The chart shows the 32 cars in R's mtcars dataset. The red point is your estimate. This is a simple statistical estimate, not a guarantee for a real car.")
    ),
    mainPanel(
      h3(textOutput("estimate")),
      plotOutput("comparison")
    )
  )
))
