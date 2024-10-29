import pandas as pd
import numpy as np

def expand_survey(survey_df, target_size=300):
    # 获取原始数据中的总数
    original_size = len(survey_df)
    
    # 查看并打印扩充前的比例
    original_ratios = survey_df.apply(lambda x: x.value_counts(normalize=True)).fillna(0)
    print("扩充前的比例：")
    print(original_ratios)
    
    # 计算每列选项的比例并生成扩充后的数据
    expanded_data = []
    for column in survey_df.columns:
        counts = survey_df[column].value_counts()
        proportions = counts / original_size
        num_samples = (proportions * target_size).round().astype(int)
        
        column_data = np.concatenate([
            [option] * num_samples[option] for option in num_samples.index
        ])
        np.random.shuffle(column_data)
        expanded_data.append(column_data)
    
    # 将扩充后的数据合并为DataFrame
    expanded_df = pd.DataFrame({col: data for col, data in zip(survey_df.columns, expanded_data)})
    
    # 查看并打印扩充后的比例
    expanded_ratios = expanded_df.apply(lambda x: x.value_counts(normalize=True)).fillna(0)
    print("\n扩充后的比例：")
    print(expanded_ratios)
    
    return expanded_df

# 示例用法
survey_df = pd.read_csv("survey_results.csv")
expanded_df = expand_survey(survey_df, target_size=300)

# 将扩充后的数据保存到新的CSV文件
expanded_df.to_csv("expanded_survey_results.csv", index=False)
