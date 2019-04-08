def designerPdfViewer(h, word):
    max_height = 0

    for letter in word:
        height = h[ord(letter) - ord("a")]
        if height > max_height:
            max_height = height

    return max_height * len(word)
