# main
import pandas as pd
import re

def main(row):
    row = row["Column45"]
    
    # flags
    iList = {
        '友達と応募歓迎': '0', '履歴書不要': '0', '高収入': '0', '日払い': '0', '扶養控除内勤務可': '0', 'シルバー歓迎': '0', 
        'フリーター歓迎': '0', '留学生歓迎': '0', '大学生歓迎': '0', '学歴不問': '0', '経験者優遇': '0', '高校生歓迎': '0', 
        '主婦(夫)歓迎': '0', '未経験者歓迎': '0', 'ヒゲ可': '0', 'ピアスOK': '0', '髪色自由': '0', 'ネイル可': '0', '髪型自由': '0', '服装自由': '0', 
        'オープニングスタッフ': '0', '駅から5分以内': '0', '産休・育休取得実績あり': '0', '車通勤OK': '0', '1日4h以内可': '0', 
        'シフト自由・自己申告': '0', '春夏冬休み期間限定': '0', '在宅ワーク・内職': '0', '土日祝勤務': '0', '副業・Ｗワーク歓迎': '0', 
        '研修制度あり': '0', '交通費支給': '0', '寮・社宅あり': '0', 'まかない(食事)あり': '0', '託児所あり': '0'
    }
    
    # Check each pattern individually against the input string
    [iList.update({pattern: '1'}) for pattern in iList.keys() if pattern in row]
    
    # inserting the formation of bits from the flags
    bits = ""
    for i in iList.values():
        bits += str(i)
    df.at[count[0], "index"] = bits
    count[0]+=1

# read the main file
tgt="target_data/tgtData.csv"
df=pd.read_csv(tgt, encoding='shift_jis')

#row to be assigned
count=[0]

#column to be assigned
df['index'] = None

# excute the program
df.apply(main, axis=1)

# save output
df.to_csv("output.csv")