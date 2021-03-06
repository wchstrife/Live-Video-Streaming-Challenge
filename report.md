# 实验总结

王宸昊 2019214541

## 1. 实现思路

在阅读了一部分代码的框架，简单的分析预测的目标是码率和缓冲区大小。

其中码率有4个档，缓冲区大小有2个档。

由于对数据和基础方法并不是特别熟悉，所以预测采用的方法是简单的阈值划分。

主要的工作包括
1. 对不同的属性字段对于QoE的影响进行了分析
2. 对于阈值的选取进行了调试。

## 2. 实验结论

根据对观测量的实际分析，选取了如下观测量进行阈值划分：
- rebuf
- buffer_size
- end_delay
- buffer_flag

经过实验后，buffer_size对结果的影响最大，首先根据buffer_size作为主要特征进行划分.

其次只有少部分数据有rebuf时间，所以当出现该特征时，优先考虑降低码率.

end_delay 和 buffer_flag 作为次要的特征，在一定程度上可以提升QoE.

同时，还对cdn_flag、decision_flag等特征进行了分析，发现对结果的影响不大甚至有负面影响，也有可能是采用的线性划分模型过于简单，所以拟合的效果不好。

最终，在给定的测试集上，QoE均值为1128.764左右，相比于采用强化学习的冠军模型，还是有相当大的差距。