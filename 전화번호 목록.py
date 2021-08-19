def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    d = {}
    for phone in phone_book:
        for i in range(len(phone)):
            if phone[:i] in d.keys():
                return False
        d[phone] = [phone]           
    return True