# Microsoft Q&A (MSQA)

Microsoft Q&A (MSQA) dataset is a question-answering dataset collected from the Microsoft Q&A forum (https://learn.microsoft.com/en-us/answers/). The dataset covers a wide range of Mi-crosoft technologies and products, including Azure,Office 365, Windows, and more. It contains 32k QA pairs, wher the answer is human-generated and selected as accepted answer.


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
| Start Date | 2019-10-29 |
| End Date | 2023-05-25 |
| Date range             | 1304 days|
| # data | 32765 |
| # tags | 377 | 
| Avg. # questions per tag | 111 |
| Avg. # tags per question | 1.28 |
| Avg. #tokens per question | 276.29 | 
| Avg. #tokens per answer | 278.78 |
| Avg. #upvotes per question | 0.04 |
| Avg. #upvotes per answer | 0.28 |
| Avg. #upvotes per sample | 0.32 |
### Data Filtering and Post-processing

Due to the data being collected from an online Q&A forum, the content is complex and includes a large number of decorative symbols and platform-generated content, which is hard to be used for research directly. To address this issue, we conducted a deep sampling of the collected data, summarized the existing problems, identified patterns, and designed the following data filtering pipeline:
- Remove user-id.
- Standardize all links using the Markdown link reference syntax to organize them into a unified format.
- Remove platform-generated content, such as messages asking for upvotes or email notifications.
- Remove irregular decorative symbols added by users, such as asterisks for separation.
- Match various line breaks and replace consecutive multiple line breaks with a single one.
- Detect image links in questions and remove samples with screenshots, as the dataset focuses solely on plain text.
- Detect the length of questions and specifically label samples with questions exceeding 8192 tokens, as these may require special handling or truncation for current models.

### Data example
Below is an actual example from the MSQA dataset:

| Attribut | Value |
| --- | --- |
| QuestionId | 247 |
 AnswerId | 345 |
 CreationDate | 2019-10-29T21:52:46.9Z |
 Score | 1 |
 QuestionScore | 0 |
 AnswerScore | 1 |
 Tags | ["Azure Web Apps"] |
 IsAzure | True |
 IsM365 | False |
 IsOther | False |
 QuestionText | Buy custom domain for Azure Web App<br>I want to purchase a new custom domain for my Azure Web App ?    <br>    <br>[Sourced from FAQ][1]    <br>    <br>  [1]: https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-buy-domain |
 AnswerText | App Service Free and Shared (preview) hosting plans are base tiers that run on the same Azure virtual machines as other App Service apps. Some apps might belong to other customers. These tiers are intended to be used only for development and testing purposes.    <br>    <br>To use custom domains in Azure App Service, your app's App Service plan must be a **paid tier** (Shared, Basic, Standard, or Premium). In this step, you make sure that the app is in the supported pricing tier.    <br>    <br>    <br>To learn how to purchase and set up a custom domain for your App Service web app, see [Buy and configure a custom domain name in App Service.][1]    <br>    <br>[Sourced from FAQ][1]    <br>    <br>  [1]: https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-buy-domain    <br> |
 Url | https://learn.microsoft.com/en-us/answers/questions/247/buy-custom-domain-for-azure-web-app.html |
 ProcessedAnswerText | App Service Free and Shared (preview) hosting plans are base tiers that run on the same Azure virtual machines as other App Service apps. Some apps might belong to other customers. These tiers are intended to be used only for development and testing purposes.    <br>To use custom domains in Azure App Service, your app's App Service plan must be a **paid tier** (Shared, Basic, Standard, or Premium). In this step, you make sure that the app is in the supported pricing tier.    <br>To learn how to purchase and set up a custom domain for your App Service web app, see [Buy and configure a custom domain name in App Service.](https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-buy-domain)    <br>[Sourced from FAQ](https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-buy-domain) |


To facilitate manual inspection of the effectiveness of data filtering, we developed a script, `viz.py`, that visualizes the differences before and after data filtering. Below is an example of the visualization,

![visualization-demo](https://github.com/keanudicap/MSQA/blob/wzz/pic/demo_pic.png)

The source files for this demo can be found at [viz_demo.html](https://github.com/keanudicap/MSQA/blob/wzz/viz_demo.html).


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