from database import Word


class IremnaWord(Word):
    def __init__(self, word: str, pronunciation: str, pos: str, meaning: str,
                 word2: str, pronunciation2: str, pos2: str, meaning2: str, 
                 word3: str, pronunciation3: str, pos3: str, meaning3: str, 
                 word4: str, *notes: str):
        super().__init__(word)
        self.pronunciation = pronunciation
        self.pos = pos
        self.meaning = meaning
        
        self.word2 = word2
        self.pronounciation2 = pronounciation2
        self.pos2 = pos2
        self.meaning2 = meaning2
        
        self.word3 = word3
        self.pronounciation3 = pronounciation3
        self.pos3 = pos3
        self.meaning3 = meaning3
        
        self.word4 = word4
        self.notes = notes

    def get_field_name(self, special: bool) -> str:
        return f'**{self.word}**' + (f' [{self.pronounciation}]' if self.pronounciation else '') if not special \
            else f'__**{self.word}**' + (f' [{self.pronounciation}]' if self.pronounciation else '') + ' (일치)__'

    def get_field_value(self) -> str:
        definitions = list()
        if self.meaning:
            line = ''
            if self.pos:
                line += '<' + self.pos + '> '
            line += meaning
            definitions.append(line)
        if self.word2:
            line = '→ '
            if self.pos2:
                line += '<' + self.pos2 + '> '
            line += '**' + self.word2 + '**'
            if self.pronounciation2:
                line += ' [' + self.pronounciation2 + ']'
            if self.meaning2:
                line += ' ― ' + self.meaning2
            definitions.append(line)
        if self.word3:
            line = '→ '
            if self.pos3:
                line += '<' + self.pos3 + '> '
            line += '**' + self.word3 + '**'
            if self.pronounciation3:
                line += ' [' + self.pronounciation3 + ']'
            if self.meaning3:
                line += ' ― ' + self.meaning3
            definitions.append(line)
        return '\n'.join(definitions)