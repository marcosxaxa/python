def paper_doll(text):
    out = []
    for i in text:
        out.append(i*3)
    print(''.join(out))

paper_doll('mississippi')