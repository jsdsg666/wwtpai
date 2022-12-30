# wwtpai
 
One Paragraph of project description goes here
 
## Getting Started
 
This project is used for modeling and machine learning applications in the waste water treatment process(WWTP). Applicable disciplines of the project:Environmental Science and Engineering, Water Supply and Drainage Science and Engineering, Civil Engineering, Municipal Engineering, Resources and Environment, Environmental Informatics, Machine Learning, Deep Learning
 
### Prerequisites
You need the environment of python3,third party library of pandas,openpyxl


### Installing
You can get it by pip install wwtpai
```
pip install wwtpai
```

 
## Example
```
import pandas as pd
import wwtpai

train=pd.read_excel(../dataset/pre_train.xlsx)
test=pd.read_excel(../dataset/pre_test.xlsx)
'''
difference_sequence is the environmental indicator to be constructed. The second column is the initial value, the third column is the end value, and the first column is the difference value.The second and third columns are names of columns about the environmental data set what you need to optimize,  the first column is that you need to name it yourself
'''
difference_sequence=[('COD','WI_COD','WO_COD'),
('AN','WI_AN','WO_AN'),
('TN','WI_TN','WO_TN'),
('AR_DO','AR_WODO','AR_WIDO'),
('AR_AN','WI_AN','AR_AN')]
print(train.describe(),test.describe())


after_train_excel,after_test_excel=wwtp_data_opt(train, test, difference_sequence)
after_train=pd.read_excel(after_train_excel)
after_test=pd.read_excel(after_test_excel)
print(after_train.describe(),after_test.describe())
```
## Versioning
 0.1.1

 
## Authors
 
* **Wang YuQi** -*Harbin Institute of Technology,shenzhen*- *Main work* 
* **Wang HongCheng** -*Harbin Institute of Technology,shenzhen*- *tutor* 
* **Wang AiJie** -*Harbin Institute of Technology,shenzhen*- *tutor* 
* **Zhou HanBo** -*Harbin Institute of Technology,shenzhen*- *team members* 
* **Wang WenZhe** -*Harbin Institute of Technology,shenzhen*- *team members* 
* **Lv JiaQiang** -*Harbin Institute of Technology*- *team members* 
 
 
## License
 
GPL
 
## Acknowledgments
*Harbin Institute of Technology,shenzhen*

