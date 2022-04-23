import os
import glob


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


def main():

    input_change_current_directory("""Which directory?
Example: .
""")

    print(f"""Current directory: {os.getcwd()}""")

    # フィル名を一覧します
    files = list_files_flat()


main()
