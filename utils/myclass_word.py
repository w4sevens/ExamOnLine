# encoding: utf-8
# @author: w4dll
# @file: myclass_word.py
# @time: 2021/2/12 13:05
from docx import Document
import copy

class QuestionBankClass:
    def __init__(self, filepath):
        self.data = []  # 题库数据

        # docx文档初始化
        self.d = Document(filepath)

    def get_questionbank(self):
        self.run()
        return self.data

    def get_contents(self, p, s1, ):
        single = p.text.find(s1 + ':')
        if single < 0:
            return ""
        single_end = p.text.find(']', single)
        res = p.text[single + 3:single_end]
        return res

    def run(self):
        ls = []
        dt = {}
        for p in self.d.paragraphs:
            if p.text.startswith('['):
                dt["question_type"] = self.get_contents(p, '题型')
                dt["answer"] = self.get_contents(p, '答案')
                dt["score"] = self.get_contents(p, '分数')
                dt["difficulty"] = self.get_contents(p, '难度')
            else:
                if p.text == "" and ls:
                    if ls[0] == "":  # 最后一行为空不保存
                        continue
                    dt['title'] = '\n'.join(ls)
                    a = copy.deepcopy(dt)
                    self.data.append(a)
                    dt.clear()
                    ls = []
                else:
                    ls.append(p.text)
        if dt and ls:
            dt['title'] = '\n'.join(ls)
            self.data.append(dt)