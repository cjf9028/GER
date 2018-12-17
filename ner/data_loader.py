# -*- coding: utf-8 -*-

import os
from konlpy.tag import Komoran
def _read_data_file(file_path, train=True):
    sentences = []
    sentence = [[], [], [],[]]
    komoran = Komoran()
    for line in open(file_path, encoding="utf-8"):
        line = line.strip()
		if max < index:
			max = index
		if line == "":
			sentences.append(sentence)
			sentence = [[], [], []]
		else:
			idx, ejeol, ner_tag = line.split("\t")
			# idx는 0부터 시작하도록
			if int(idx) == 1:
				index = 1
			for x in range(0, len(ejeol)):
				sentence[0].append(int(index))
				index += 1
				sentence[1].append(ejeol[x])
				if x == 0 and ner_tag != "-":
					if ner_tag[-1:] == "I":
						ner_tag = ner_tag[:-1] + "l"
					else:
						ner_tag = ner_tag[:-1] + "B"
				elif ner_tag != "-":
					ner_tag = ner_tag[:-1] + "l"
				sentence[2].append(ner_tag)
			sentence[0].append(int(index))
			index += 1
			sentence[1].append("SP_B")
			sentence[2].append("SP_B")

    return sentences

def test_data_loader(root_path):
    # [ idx, ejeols, nemed_entitis ] each sentence
    file_path = os.path.join(root_path, 'test', 'test_data')

    return _read_data_file(file_path, False)


def data_loader(root_path):
    # [ idx, ejeols, nemed_entitis ] each sentence
    file_path = os.path.join(root_path, 'train', 'train_data')

    return _read_data_file(file_path)

if __name__ == "__main__":
    sentences = data_loader("data")
    print(sentences[0])
