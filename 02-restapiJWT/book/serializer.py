def BookSerializer(books):
    res = []
    for indx in range(0, len(books)):
        book = books[indx]

        data = {
            "id": book.id,
            "title": book.title,
            "writer": book.writer
        }
        res.append(data)
    return res
