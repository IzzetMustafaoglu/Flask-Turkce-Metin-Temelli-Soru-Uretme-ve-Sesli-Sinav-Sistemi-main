import spacy
import clause
import nonClause
import identification
import questionValidation
from nlpNER import nerTagger



class AutomaticQuestionGenerator():
    # AQG Parsing & Generate a question
    def aqgParse(self, sentence):

        #nlp = spacy.load("en")
        nlp = spacy.load('en_core_web_sm')

        singleSentences = sentence.split(".")
        questionsList = []
        if len(singleSentences) != 0:
            for i in range(len(singleSentences)):
                segmentSets = singleSentences[i].split(",")

                ner = nerTagger(nlp, singleSentences[i])

                if (len(segmentSets)) != 0:
                    for j in range(len(segmentSets)):
                        previous = len(questionsList)
                        try:
                            questionsList += clause.howmuch_2(segmentSets, j, ner)
                        except Exception:
                            pass

                        if identification.clause_identify(segmentSets[j]) == 1:
                            try:
                                questionsList += clause.whom_1(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.whom_2(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.whom_3(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.whose(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.what_to_do(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.who(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.howmuch_1(segmentSets, j, ner)
                            except Exception:
                                pass
                            try:
                                questionsList += clause.howmuch_3(segmentSets, j, ner)
                            except Exception:
                                pass


                            else:
                                s = identification.subjectphrase_search(segmentSets, j)
                                try:
                                    s = identification.subjectphrase_search(segmentSets, j)
                                except Exception:
                                    pass

                                if len(s) != 0:
                                    segmentSets[j] = s + segmentSets[j]
                                    try:
                                        questionsList += clause.whom_1(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.whom_2(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.whom_3(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.whose(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.what_to_do(segmentSets, j, ner)
                                    except Exception:
                                        pass
                                    try:
                                        questionsList += clause.who(segmentSets, j, ner)
                                    except Exception:
                                        pass

                                    else:
                                        try:
                                            questionsList += nonClause.what_whom1(segmentSets, j, ner)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nonClause.what_whom2(segmentSets, j, ner)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nonClause.whose(segmentSets, j, ner)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nonClause.howmany(segmentSets, j, ner)
                                        except Exception:
                                            pass
                                        try:
                                            questionsList += nonClause.howmuch_1(segmentSets, j, ner)
                                        except Exception:
                                            pass
                        if previous < len(questionsList):
                            for q in range(previous, len(questionsList)):
                                questionsList[q] = [questionsList[q], segmentSets[j]]

                questionsList.append('\n')
                print(questionsList)
        return questionsList



    def DisNormal(self, str):
        print("\n")
        print("------X------")
        print("Start  output:\n")

        count = 0
        out = ""

        for i in range(len(str)):
            count = count + 1
            print("Q-0%d: %s" % (count, str[i]))

        print("")
        print("End  OutPut")
        print("-----X-----\n\n")


    # AQG Display the Generated Question
    def display(self, str):
        print("\n")
        print("------X------")
        print("Start  output:\n")

        count = 0
        out = ""
        for i in range(len(str)):
            if (len(str[i][0]) >= 3):
                if (questionValidation.hNvalidation(str[i][0]) == 1):
                    if ((str[i][0][0] == 'W' and str[i][0][1] == 'h') or (str[i][0][0] == 'H' and str[i][0][1] == 'o') or (
                            str[i][0][0] == 'H' and str[i][0][1] == 'a')):
                        WH = str[i][0].split(',')
                        if (len(WH) == 1):
                            str[i][0] = str[i][0][:-1]
                            str[i][0] = str[i][0][:-1]
                            str[i][0] = str[i][0][:-1]
                            str[i][0] = str[i][0] + "?"
                            count = count + 1

                            if (count < 10):
                                # print("Q-0%d: %s" % (count, str[i][0]))
                                # print("\nAnswer:",str[i][1].replace("\n"," "),"\n---------\n")
                                out += "Q-0" + count.__str__() + ": " + str[i][0] + "\n"
                                out += "Ans: " + str[i][1].replace("\n", " ") + "\n"
                                out += "----------\n"

                            else:
                                # print("Q-%d: %s" % (count, str[i][0]))
                                # print("\nAnswer:",str[i][1].replace("\n"," "),"\n---------\n")
                                out += "Q-" + count.__str__() + ": " + str[i][0] + "\n"
                                out += "Ans: " + str[i][1].replace("\n", " ") + "\n"
                                out += "----------\n"

        print("")
        print("End  OutPut")
        print("-----X-----\n\n")

        output = "C:/Users/izzet/OneDrive/Masaüstü/asdf/Metin-Temelli-Soru-Uretme-ve-Sesli-Sinav-Sistemi-master/DB/output.txt"

        w = open(output, 'w+', encoding="utf8")
        w.write(out)
        w.close()
        return 0

