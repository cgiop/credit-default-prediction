import numpy as np

def add_features(df):

    # 1️⃣ Average repayment delay
    pay_cols = ['PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']
    df['avg_repayment_delay'] = df[pay_cols].mean(axis=1)

    # 2️⃣ Max repayment delay (worst case behavior)
    df['max_repayment_delay'] = df[pay_cols].max(axis=1)

    # 3️⃣ Average bill amount
    bill_cols = ['BILL_AMT1','BILL_AMT2','BILL_AMT3',
                 'BILL_AMT4','BILL_AMT5','BILL_AMT6']
    df['avg_bill_amt'] = df[bill_cols].mean(axis=1)

    # 4️⃣ Average payment made
    pay_amt_cols = ['PAY_AMT1','PAY_AMT2','PAY_AMT3',
                     'PAY_AMT4','PAY_AMT5','PAY_AMT6']
    df['avg_payment_amt'] = df[pay_amt_cols].mean(axis=1)

    # 5️⃣ Payment to bill ratio (repayment strength)
    df['payment_to_bill_ratio'] = df['avg_payment_amt'] / (df['avg_bill_amt'] + 1)

    # 6️⃣ Credit utilization
    df['credit_utilization'] = df['avg_bill_amt'] / df['LIMIT_BAL']

    return df
