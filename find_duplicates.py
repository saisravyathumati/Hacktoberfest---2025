import os, hashlib

def hash_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def find_duplicates(folder):
    hashes = {}
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            file_hash = hash_file(path)
            if file_hash in hashes:
                print(f"Duplicate found:\n{path}\n{hashes[file_hash]}\n")
            else:
                hashes[file_hash] = path

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    find_duplicates(folder)
