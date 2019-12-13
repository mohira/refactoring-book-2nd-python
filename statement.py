import math


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = 0

        if play['type'] == 'tragedy':
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == 'comedy':
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']
        else:
            raise Exception(f'unknown type: {play["type"]}')

        # ボリューム特典のポイントを加算
        volume_credits += max(perf['audience'] - 30, 0)

        # 喜劇の時人は10人につき、さらにポイントを加算
        if 'comedy' == play['type']:
            volume_credits += math.floor(perf['audience'] / 5)

        # 注文の内訳を出力
        result += f'  {play["name"]}: ${this_amount / 100:.2f} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is ${total_amount / 100:.2f}\n'
    result += f'You earned {volume_credits} credits\n'

    return result
