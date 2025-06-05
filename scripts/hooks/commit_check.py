import joblib
import sys

commit_msg_file = sys.argv[1]
with open(commit_msg_file, "r") as f:
    message = f.read().strip()

# Load and use
model = joblib.load('./scripts/models/commit_message_classifier.pkl')
result = model.predict([message])
print(result[0])

if result[0] != "yes":
    print(f"\n[X] Commit blocked: message classified as invalid. Please write a clearer or more meaningful commit message.", file=sys.stderr)
    sys.exit(1)

print("[OK] Commit message passed validation.")