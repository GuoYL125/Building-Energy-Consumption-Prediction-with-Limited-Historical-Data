# LSTNet

## Usage
### Training
```shell
python main.py --data="data/need_new_data_Akima-5.txt" --save="save/need_new_data_Akima-5_Akima_1_1" --test --savehistory --logfilename="log/lstnet" --horizon 1 --normalize=1 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --save="save/need_new_data_Akima-5_Akima_2_1" --test --savehistory --logfilename="log/lstnet" --horizon 2 --normalize=1 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --save="save/need_new_data_Akima-5_Akima_3_1" --test --savehistory --logfilename="log/lstnet" --horizon 3 --normalize=1 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --save="save/need_new_data_Akima-5_Akima_4_1" --test --savehistory --logfilename="log/lstnet" --horizon 4 --normalize=1 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --save="save/need_new_data_Akima-5_Akima_5_1" --test --savehistory --logfilename="log/lstnet" --horizon 5 --normalize=1 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --save="save/need_new_data_Akima-5_Akima_6_1" --test --savehistory --logfilename="log/lstnet" --horizon 6 --normalize=1 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --save="save/need_new_data_Akima-5_Akima_7_1" --test --savehistory --logfilename="log/lstnet" --horizon 7 --normalize=1 --window=35 --skip=5 --highway=5 --batchsize=128
```
### Predict

The main.py file will need to be modified to focus on saving names when predicting.

```shell
python main.py --data="data/need_new_data_Akima-5.txt" --no-train --load="save/need_new_data_Akima-5_Akima_1_1" --predict=testingdata --plot --series-to-plot=0 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --no-train --load="save/need_new_data_Akima-5_Akima_2_1" --predict=testingdata --plot --series-to-plot=0 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --no-train --load="save/need_new_data_Akima-5_Akima_3_1" --predict=testingdata --plot --series-to-plot=0 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --no-train --load="save/need_new_data_Akima-5_Akima_4_1" --predict=testingdata --plot --series-to-plot=0 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --no-train --load="save/need_new_data_Akima-5_Akima_5_1" --predict=testingdata --plot --series-to-plot=0 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --no-train --load="save/need_new_data_Akima-5_Akima_6_1" --predict=testingdata --plot --series-to-plot=0 --window=35 --skip=5 --highway=5 --batchsize=128
python main.py --data="data/need_new_data_Akima-5.txt" --no-train --load="save/need_new_data_Akima-5_Akima_7_1" --predict=testingdata --plot --series-to-plot=0 --window=35 --skip=5 --highway=5 --batchsize=128
```

## Results

Predict the results from April 18 to 24 based on the model. The data is processed through the data_process/result_switch_value.py file, and the 7-day results are summarized in the submission form.

## Dataset

Data conversion of the meter data into submission data format using per-process/625_row_78.py. Expand the data volume using the interpolation method of sequential_data_interpolation.py to get the dataset.

