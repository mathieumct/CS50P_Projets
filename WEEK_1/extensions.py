filename = (input("File Name : "))

if filename.strip().lower().endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpg"):
        print("image/jpeg")
elif filename.strip().lower().endswith(".jpeg"):
        print("image/jpeg")
elif filename.strip().lower().endswith(".png"):
        print("image/png")
elif filename.strip().lower().endswith(".pdf"):
        print("application/pdf")
elif filename.strip().lower().endswith(".txt"):
        print("text/plain")
elif filename.strip().lower().endswith(".zip"):
        print("application/zip")
else :
       print("application/octet-stream")
