# Microsoft Q&A (MSQA)

Microsoft Q&A (MSQA) dataset is a question-answering dataset collected from the Microsoft Q&A forum (https://learn.microsoft.com/en-us/answers/). The dataset covers a wide range of Mi-crosoft technologies and products, including Azure,Office 365, Windows, and more. It contains 62k QA pairs, wher the answer is human-generated and selected as accepted answer.


## News
- **We arxiv our paper (https://arxiv.org/abs/2305.11541).**


## Introduction
Recent advancements in large language models(LLMs) have demonstrated
their impressive performance across various natural language processing (NLP)
tasks. However, when it comes to domain-specfic problems, LLMs exhibit limited
performance due to their insufficient pretraining on domain knowledge. Fine-tuning
and maintaining LLMs to incorparte domain-specific knowledge could be expensive
for researchers. In addition, the availability of domain-specific data is often restricted
and confidential, introducing risks of data leakage when using them for fine-tuning LLMs.

Existing works leverage retrieval-based methods or external modules to extract domain-specific knowledge.
However, these approaches suffer from limitations such as not retrieving all the necessary context when
facing complex questions. We introduce a novel model interaction paradigm taht bridges domain-general and
domain-specific knowledge. Our approach involves fine-tuning a small language model, e.g., LLaMA using
domain documentation to align it with domain-specific knowledge. Then we instruction-tune with MSQA scenario.
This paradigm replaces traditional retrieval modules with the generation of domain-specific knowledge,
enabling easy maintenance and privacy protection within the specific domain.

We release MSQA data and believe that this benchmarking dataset will assist the research community in
evaluating their model interaction strategies in domain-specific scenarios.

### Statistics of MSQA

| Statistic                        | Value |
|-----------------------------|---------|
| Date range             | 1304 days|
| # data | 32765|
| # tags | 377| 
| Avg. # questions per tag | 111 |
| Avg. # tags per question | 1.28 |
| Avg. #tokens per question | 276.29 | 
| Avg. #tokens per answer | 278.78 |
| Avg. #upvotes per question | 0.04 |
| Avg. #upvotes per answer | 0.28 |
| Avg. #upvotes per sample | 0.32 |
### Data Filtering and Post-processing

### Data example

<!-- the table of one data example -->

<!-- your data visualization of before and after post-processing -->

## License
This dataset is released under open data license, CDLA-Permissive-2 (https://cdla.dev/permissive-2-0/)

## Get Data

**\*\*Please DO NOT re-distribute our data.\*\***

If you think the release of this dataset might infringe your copyright, please inform us via the email fangkaiyang@microsoft.com for taking down the dataset.



## Paper and Citation
https://arxiv.org/abs/2305.11541
```
@misc{wang2023empower,
      title={Empower Large Language Model to Perform Better on Industrial Domain-Specific Question Answering}, 
      author={Zezhong Wang and Fangkai Yang and Pu Zhao and Lu Wang and Jue Zhang and Mohit Garg and Qingwei Lin and Dongmei Zhang},
      year={2023},
      eprint={2305.11541},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

<!-- ## References

- [Ren et al., 2015] Shaoqing Ren, Kaiming He, Ross B. Girshick,
    and Jian Sun. Faster R-CNN: towards real-time
    object detection with region proposal networks. CoRR,
    abs/1506.01497, 2015.
- [Gilani et al., 2017] A. Gilani, S. R. Qasim, I. Malik, and
    F. Shafait. Table detection using deep learning. In Proc. of
    ICDAR 2017, volume 01, pages 771–776, Nov 2017.
- [Wu et al., 2019] Y Wu, A Kirillov, F Massa, WY Lo, R Girshick. [Detectron2](https://github.com/facebookresearch/detectron2)[J]. 2019.
- [Xie et al., 2016] Saining Xie, Ross B. Girshick, Piotr
    Doll´ar, Zhuowen Tu, and Kaiming He. Aggregated residual
    transformations for deep neural networks. CoRR,
    abs/1611.05431, 2016.
- [Klein et al., 2017] Guillaume Klein, Yoon Kim, Yuntian
    Deng, Jean Senellart, and Alexander M. Rush. Open-NMT:
    Open-source toolkit for neural machine translation.
    In Proc. of ACL, 2017.] -->