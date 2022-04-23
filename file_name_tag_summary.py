import os
import glob
import re


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
    pattern = re.compile("^.*__(.*)__.*$")

    for file in files:
        result = pattern.match(file)
        if result:
            # Matched
            tag_section = result.group(1)
            print(f"tag_section={tag_section}")

            tags = tag_section.split("_")
            for tag in tags:
                print(f"tag={tag}")

        else:
            pass

        pass


main()
