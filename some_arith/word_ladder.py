# -*- coding: utf-8 -*-
beginWord = "hot"
endWord = "dog"
wordList = ["hot", "dog", "cog", "pot", "dot"]
# beginWord = "lost"
# endWord = "miss"
# wordList = ["most","mist","miss","lost","fist","fish"]
# beginWord = "leet"
# endWord = "code"
# wordList = ["lest","leet","lose","code","lode","robe","lost"]
beginWord = "kiss"
endWord = "tusk"
wordList = ["dusk", "kiss", "miss", "musk", "tusk", "diss", "disk", "sang", "ties", "muss"]

# beginWord ="hot"
# endWord = "dog"
# wordList = ["hot","dog"]

beginWord = "cet"
endWord = "ism"
wordList = ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val", "mes", "ohs", "now", "boa", "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob", "rue", "fry", "lit", "rex", "jan", "cot", "bid", "ali", "pay", "col", "gum", "ger", "row", "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui", "ark", "has", "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu", "ana", "gap", "cry", "led", "abe", "box", "ore", "pig", "fie", "toy", "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply", "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan", "map", "ski", "ova", "wed", "non", "wac", "nut", "why", "bye", "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot", "bow", "fob", "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib", "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag", "jar", "arm", "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk", "far", "mew", "wit", "doe", "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic", "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen", "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod", "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere", "dig", "era", "cat", "fox", "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani", "and", "ibm", "yap", "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan", "fey", "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao", "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may", "shy", "rid", "bat", "sum", "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo", "hey", "saw", "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva", "tog", "ram", "let", "see", "zit", "maw", "nix", "ate", "gig", "rep", "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod",
            "bed", "vet", "ham", "sis", "hex", "via", "fir", "nod", "mao", "aug", "mum", "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem", "who", "bet", "gos", "son", "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin", "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken", "wad", "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin", "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug", "asp", "hui", "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm", "nat", "wyo", "gym", "dug", "toe", "dee", "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd", "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio", "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc", "moe", "caw", "eel", "dix", "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton", "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did", "tin", "get", "gte", "sox", "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty", "lap", "two", "ins", "con", "ant", "net", "tux", "ode", "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot", "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism", "err", "him", "all", "pad", "hah", "hie", "aim", "ike", "jed", "ego", "mac", "baa", "min", "com", "ill", "was", "cab", "ago", "ina", "big", "ilk", "gal", "tap", "duh", "ola", "ran", "lab", "top", "gob", "hot", "ora", "tia", "kip", "han", "met", "hut", "she", "sac", "fed", "goo", "tee", "ell", "not", "act", "gil", "rut", "ala", "ape", "rig", "cid", "god", "duo", "lin", "aid", "gel", "awl", "lag", "elf", "liz", "ref", "aha", "fib", "oho", "tho", "her", "nor", "ace", "adz", "fun", "ned", "coo", "win", "tao", "coy", "van", "man", "pit", "guy", "foe", "hid", "mai", "sup", "jay", "hob", "mow", "jot", "are", "pol", "arc", "lax", "aft", "alb", "len", "air", "pug", "pox", "vow", "got", "meg", "zoe", "amp", "ale", "bud", "gee", "pin", "dun", "pat", "ten", "mob"]


def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    if endWord not in wordList:
        return 0
    if cmp_word(beginWord, endWord):
        return 2
    if beginWord in wordList:
        wordList.remove(beginWord)

    path = build_tree(beginWord, endWord, wordList, [])
    for item in path:
        if endWord in item:
            return len(item)

    return 0


def cmp_word(w1, w2):
    _w1 = list(w1)
    _w2 = list(w2)
#     print w1, w2
    for item in range(len(w1)):
        tmp1 = _w1[item]
        tmp2 = _w2[item]
        _w1[item] = '_'
        _w2[item] = '_'

        if ''.join(_w1) == ''.join(_w2):
            return True
        _w1[item] = tmp1
        _w2[item] = tmp2
    return False


def cmp_path(path_1, path_2):
    for idx, item_1 in enumerate(path_1):
        if path_2[idx] != item_1:
            return False
    return True


def pre_word_map(wordList):
    _map = dict()
    for item in wordList:
        #         print item
        _word = list(item)
        for idx in range(len(item)):
            tmp = _word[idx]
            _word[idx] = '_'
            word = ''.join(_word)
            if word not in _map:
                _map[word] = set()
                _map[word].add(item)
            else:
                _map[word].add(item)
            _word[idx] = tmp
    return _map


def visit(wordList, word):
    _pre_word_map = pre_word_map(wordList)
    _set = set()
    _word = list(word)
    for idx in range(len(word)):
        tmp = _word[idx]
        _word[idx] = '_'
        key = ''.join(_word)
        _set = _set | _pre_word_map.get(key, set())
        _word[idx] = tmp
    return _set - set([word])


def build_tree(beginWord, endWord, wordList, path_set):
    if not path_set:
        path_set.append([beginWord])
    nw_path = list()
    for pathed in path_set:
        current = pathed[-1]
#         遍历
        result = list(visit(wordList, current))
#         return
        if not result:
            return path_set
#         存在
        recoard = list(pathed)
        for nxt in result:
            _pathed = list(recoard)
            if nxt not in _pathed:
                _pathed.append(nxt)
                nw_path.append(list(_pathed))
            if nxt == endWord:
                return nw_path
    return build_tree(beginWord, endWord, wordList, nw_path)

# other solution
# class Solution(object):
#     def ladderLength(self, beginWord, endWord, wordList):
#         from collections import deque
#         if endWord not in wordList:
#             return 0
#         wordList = set(wordList)  # 必备优化，不然超时

#         res, forward, backward = 2, {beginWord}, {endWord}
#         while forward:
#             if len(forward) > len(backward):
#                 forward, backward = backward, forward

#             next_level = set()
#             for word in forward:
#                 for i in range(len(word)):
#                     for k in range(26):
#                         tmp = word[:i] + chr(ord("a") + k) + word[i + 1:]

#                         if tmp in backward:  # 找到了
#                             return res
#                         if tmp in wordList:
#                             next_level.add(tmp)
#                             wordList.remove(tmp)
#             res += 1
#             forward = next_level
#         return 0


if __name__ == "__main__":
    # sl = Solution()
    # print sl.ladderLength(endWord, beginWord,  wordList)
    print ladderLength(endWord, beginWord,  wordList)
