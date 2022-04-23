import os
import glob
import re
import csv
from collections import OrderedDict


def input_change_current_directory(prompt_message):
    """カレント ディレクトリーを替えます"""
    path = input(prompt_message)

    # カレントディレクトリを移動
    os.chdir(path)


def list_files_flat():
    files = glob.glob("./**/*")

    print(f"""
Files
-----""")

    # 一覧します
    for file in files:
        print(file)

    return files


def input_y(prompt_message):
    """はい？"""
    print(prompt_message)

    answer = input()

    return answer.upper() == "Y"


def main():

    # ディレクトリーを選んでください
    while True:

        input_change_current_directory("""Which directory?
Example: .
""")

        print(f"""Current directory: {os.getcwd()}""")

        # フィル名を一覧します
        files = list_files_flat()

        is_y = input_y("""
Are you sure this is the right directory (y/n)?
""")

        if is_y:
            break
        else:
            print("Canceld")

    # 集計を始めます
    summary = OrderedDict()
    pattern = re.compile("^.*__(.*)__.*$")

    for file in files:
        result = pattern.match(file)
        if result:
            # Matched
            tag_section = result.group(1)
            # print(f"tag_section={tag_section}")

            # tags = tag_section.split("_")
            # for tag in tags:
            #     print(f"tag={tag}")

            while True:
                if tag_section in summary:
                    # print(f"+=1")
                    summary[tag_section] += 1
                else:
                    # print(f"=1")
                    summary[tag_section] = 1

                # _ が付いていれば、最後の１つを外したい
                if "_" in tag_section:
                    # print(f"before={tag_section}")
                    tag_section = tag_section.rsplit("_", 1)[0]
                    # print(f"after={tag_section}")

                else:
                    # print(f"break {tag_section}")
                    break

        else:
            pass

        pass

    # 並び替え
    summary = OrderedDict(
        sorted(summary.items(), key=lambda x: x[0])
    )

    # 集計表示
#    print("""
# Summary
# -------""")
#    for k, v in summary.items():
#        print(f"{k} = {v}")

    # CSVファイル出力
    with open('./summary.csv', 'w', encoding='utf-8', newline="") as f:
        writer = csv.DictWriter(f, ['tag', 'count'], extrasaction='ignore')
        writer.writeheader()

        rows = []
        for k, v in summary.items():
            rows.append({'tag': k, 'count': v})

        writer.writerows(rows)

    print("finished")


main()
