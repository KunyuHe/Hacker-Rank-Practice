def checkMagazine(magazine, note):
    if len(magazine) < len(note):
        print("No")
        # Program would not stop if not return
        return None

    note_dict = {}
    for word in note:
        if word not in note_dict:
            note_dict[word] = 1
        else:
            note_dict[word] += 1

    for word in magazine:
        if word in note_dict:
            note_dict[word] = max(0, note_dict[word]-1)

    print(["No", "Yes"][int(sum(note_dict.values())==0)])