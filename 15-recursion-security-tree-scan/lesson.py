"""
Lesson 15 — Recursion for Nested Security Scanning

This lesson demonstrates how a recursive function can
scan folders inside other folders and identify
suspicious files.
"""


file_system = {
    "name": "root",
    "files": [
        "notes.txt",
        "report.pdf"
    ],
    "folders": [
        {
            "name": "downloads",
            "files": [
                "invoice.pdf",
                "payload.exe"
            ],
            "folders": []
        },
        {
            "name": "documents",
            "files": [
                "resume.docx"
            ],
            "folders": [
                {
                    "name": "archive",
                    "files": [
                        "old_logs.txt",
                        "backdoor.exe"
                    ],
                    "folders": []
                }
            ]
        }
    ]
}


suspicious_extensions = (
    ".exe",
    ".bat",
    ".ps1"
)


def scan_folder(folder):
    suspicious_count = 0

    print(f"Scanning folder: {folder['name']}")

    for filename in folder["files"]:

        if filename.endswith(suspicious_extensions):
            print(f"  ALERT: Suspicious file found: {filename}")
            suspicious_count += 1

    for subfolder in folder["folders"]:
        suspicious_count += scan_folder(subfolder)

    return suspicious_count


print("=== RECURSIVE SECURITY SCAN ===")
print()

total_suspicious = scan_folder(file_system)

print()
print(f"Total suspicious files: {total_suspicious}")
