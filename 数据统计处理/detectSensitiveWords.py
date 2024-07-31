# 识别敏感词语

def check_word_in_file(file):
    filtered_words_list = []
    with open(file, 'r', encoding='utf-8') as filtered_words:
        for line in filtered_words:
            line = line.strip()
            if line != '':
                filtered_words_list.append(line)

    input_word = input('请输入：')
    if input_word in filtered_words_list:
        print('freedom')
    else:
        print('Human Rights')


# 调用函数并传入文件路径
check_word_in_file('files/filtered_word.text')
