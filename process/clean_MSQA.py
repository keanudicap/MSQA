import re
from tool import *
import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == "__main__":

    
    ans_functions = [
        remove_user_mentions, 
        replace_reference_with_link,
        remove_accept_answer_line,
        remove_ref_line,
        remove_email_notification_line, 
        remove_slash_and_dash_line, 
        remove_star_symbol_line,
        detect_and_remove_pic_case, 
        detect_and_remove_thank,
        detect_and_remove_welcome,
        detect_and_remove_hello,
        detect_and_remove_hope,
        detect_and_remove_know,
        detect_and_remove_regards,
        remove_symbols_only_line,
        remove_multiple_n,
        remove_space,
    ]

    ques_functions = [
        detect_and_remove_pic_case,
    ]

    data = pd.read_csv("./msqa-p-45k.csv")
    
    results = []
    for idx, row in data.iterrows():
        ques = row['QuestionText']
        ans = row['AnswerText']
        qid = row['QuestionId']

        processed_ques = pipeline(ques, ques_functions) # 30
        processed_ans = pipeline(ans, ans_functions)

        if processed_ques != '1155121439' and processed_ans != '1155121439':
            res_dict = row.to_dict()
            res_dict['ProcessedAnswerText'] = processed_ans
            results.append(res_dict)

    df = pd.DataFrame(results)
    print(f'{df.shape[0]} samples are saved.')
    print(df.columns)
    

    df.to_csv("msqa-p-45k.csv", index=False)
