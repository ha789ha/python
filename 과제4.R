install.packages("dplyr")
library("dplyr")

data("airquality")
airquality
airquality$windcill <- 35.74 + 0.6215*airquality$Temp - 35.75*airquality$Wind
                       + 0.4275*airquality$Temp*airquality$Wind
airquality %>%
   group_by(Month) %>%
   summarise(mean(Temp, na.rm = TRUE),
             mean(Ozone, na.rm = TRUE),
             mean(Wind, na.rm = TRUE),
             mean(windcill, na.rm = TRUE),
             mean(Solar.R, na.rm = TRUE))

## 결측치를 제외하기 위해  na.rm = TRUE 옵션 사용