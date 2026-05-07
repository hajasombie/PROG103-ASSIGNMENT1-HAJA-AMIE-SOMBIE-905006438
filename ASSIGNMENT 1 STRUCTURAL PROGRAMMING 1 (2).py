from pathlib import Path
import json
from datetime import datetime
import sys

DATA_DIR = Path(__file__).parent
STUDENTS_FILE = DATA_DIR / "students.json"
ATTENDANCE_FILE = DATA_DIR / "attendance_records.json"

def ensure_files():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not STUDENTS_FILE.exists():
        STUDENTS_FILE.write_text("{}", encoding="utf-8")
    if not ATTENDANCE_FILE.exists():
        ATTENDANCE_FILE.write_text("{}", encoding="utf-8")

def load_json(path):
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
    except Exception:
        pass
    return {}

def save_json(path, data):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_students():
    data = load_json(STUDENTS_FILE)
    # convert keys to ints for internal use
    students = {}
    for k, v in data.items():
        try:
            students[int(k)] = v
        except Exception:
            continue
    return students

def save_students(students):
    # convert keys to str for json
    data = {str(k): v for k, v in students.items()}
    save_json(STUDENTS_FILE, data)

def load_attendance():
    return load_json(ATTENDANCE_FILE)

def save_attendance(att):
    save_json(ATTENDANCE_FILE, att)

def input_int(prompt, allow_blank=False):
    while True:
        v = input(prompt).strip()
        if v == "" and allow_blank:
            return None
        try:
            return int(v)
        except ValueError:
            print("Enter a numeric id.")

def input_nonempty(prompt, allow_blank=False):
    while True:
        s = input(prompt).strip()
        if s == "" and allow_blank:
            return None
        if s == "":
            print("Cannot be empty.")
            continue
        return s

def format_student_record(raw):
    return {
        "student_name": raw.get("student_name", "").strip().title(),
        "email": raw.get("email", "").strip(),
        "parent_phonenumber": raw.get("parent_phonenumber", "").strip(),
        "phone_number": raw.get("phone_number", "").strip(),
        "faculty": raw.get("faculty", "").strip().upper(),
        "program": raw.get("program", "").strip().upper(),
        "class": raw.get("class", "").strip()
    }

def add_student(students):
    print("\nAdd New Student")
    sid = input_int("Student ID (numeric): ")
    if sid in students:
        print("ID already exists. Use edit if you need to change.")
        return
    name = input_nonempty("Full name: ")
    email = input_nonempty("Email: ")
    parent = input_nonempty("Parent phone number: ")
    phone = input_nonempty("Phone number: ")
    faculty = input_nonempty("Faculty: ")
    program = input_nonempty("Program: ")
    class_name = input_nonempty("Class: ")
    students[sid] = format_student_record({
        "student_name": name,
        "email": email,
        "parent_phonenumber": parent,
        "phone_number": phone,
        "faculty": faculty,
        "program": program,
        "class": class_name
    })
    save_students(students)
    print("Student added.")

def view_students(students):
    if not students:
        print("\nNo students available.")
        return
    print("\nStudents (sorted by ID):")
    for sid in sorted(students):
        s = students[sid]
        print(f"{sid} | {s['student_name']} | {s.get('faculty','')}/{s.get('program','')} | Class: {s.get('class','')}")
    print(f"\nTotal students: {len(students)}")

def view_student_detail(students):
    sid = input_int("Enter student ID to view: ")
    s = students.get(sid)
    if not s:
        print("Student not found.")
        return
    print(f"\nDetail for {sid}:")
    for k, v in s.items():
        print(f"  {k}: {v}")

def edit_student(students):
    sid = input_int("Enter student ID to edit: ")
    s = students.get(sid)
    if not s:
        print("Student not found.")
        return
    print("Press enter to keep existing value.")
    name = input_nonempty(f"Full name [{s['student_name']}]: ", allow_blank=True)
    email = input_nonempty(f"Email [{s['email']}]: ", allow_blank=True)
    parent = input_nonempty(f"Parent phone number [{s['parent_phonenumber']}]: ", allow_blank=True)
    phone = input_nonempty(f"Phone number [{s['phone_number']}]: ", allow_blank=True)
    faculty = input_nonempty(f"Faculty [{s['faculty']}]: ", allow_blank=True)
    program = input_nonempty(f"Program [{s['program']}]: ", allow_blank=True)
    class_name = input_nonempty(f"Class [{s['class']}]: ", allow_blank=True)

    updated = {
        "student_name": s["student_name"] if name is None else name.title(),
        "email": s["email"] if email is None else email,
        "parent_phonenumber": s["parent_phonenumber"] if parent is None else parent,
        "phone_number": s["phone_number"] if phone is None else phone,
        "faculty": s["faculty"] if faculty is None else faculty.upper(),
        "program": s["program"] if program is None else program.upper(),
        "class": s["class"] if class_name is None else class_name
    }
    students[sid] = updated
    save_students(students)
    print("Student updated.")

def delete_student(students, attendance):
    sid = input_int("Enter student ID to delete: ")
    if sid not in students:
        print("Student not found.")
        return
    confirm = input(f"Delete student {sid} {students[sid]['student_name']}? (yes/no): ").strip().lower()
    if confirm in ("y", "yes"):
        students.pop(sid)
        # remove from attendance records
        for date, day in attendance.items():
            if str(sid) in day:
                day.pop(str(sid))
        save_students(students)
        save_attendance(attendance)
        print("Deleted.")
    else:
        print("Cancelled.")

def search_students(students):
    q = input_nonempty("Enter full or partial name or ID: ")
    results = []
    try:
        qid = int(q)
    except Exception:
        qid = None
    for sid, s in students.items():
        if qid is not None and sid == qid:
            results.append((sid, s))
        elif q.lower() in s['student_name'].lower():
            results.append((sid, s))
    if not results:
        print("No matches.")
        return
    print("Matches:")
    for sid, s in results:
        print(f"{sid} | {s['student_name']} | {s.get('email','')}")

def mark_attendance(students, attendance):
    if not students:
        print("No students to mark.")
        return
    date_str = input("Enter date YYYY-MM-DD (empty = today): ").strip()
    if date_str == "":
        date_str = datetime.now().date().isoformat()
    day = attendance.setdefault(date_str, {})
    print("Enter student IDs separated by commas to mark present.")
    ids_raw = input("IDs: ").strip()
    if not ids_raw:
        print("No ids entered.")
        return
    try:
        ids = [int(x.strip()) for x in ids_raw.split(",") if x.strip()]
    except ValueError:
        print("Invalid id list.")
        return
    for sid in ids:
        if sid in students:
            day[str(sid)] = "present"
    save_attendance(attendance)
    print(f"Marked present for date {date_str}.")

def view_attendance_for_date(students, attendance):
    date_str = input("Enter date YYYY-MM-DD (empty = today): ").strip()
    if date_str == "":
        date_str = datetime.now().date().isoformat()
    day = attendance.get(date_str)
    if not day:
        print("No attendance for that date.")
        return
    print(f"Attendance on {date_str}:")
    for sid_str, status in sorted(day.items(), key=lambda x: x[0]):
        try:
            sid = int(sid_str)
        except Exception:
            sid = sid_str
        name = students.get(sid, {}).get("student_name", "Unknown") if isinstance(sid, int) else "Unknown"
        print(f"  {sid}: {name} - {status}")

def view_attendance_for_student(students, attendance):
    sid = input_int("Enter student ID: ")
    sid_s = str(sid)
    records = []
    for date in sorted(attendance.keys()):
        status = attendance[date].get(sid_s, "absent")
        records.append((date, status))
    if not records:
        print("No attendance records.")
        return
    print(f"Attendance report for {sid} {students.get(sid,{}).get('student_name','')}:")
    for date, status in records:
        print(f"  {date}: {status}")

def export_paths():
    print(f"Students JSON: {STUDENTS_FILE.resolve()}")
    print(f"Attendance JSON: {ATTENDANCE_FILE.resolve()}")

def main_menu():
    ensure_files()
    students = load_students()
    attendance = load_attendance()
    actions = {
        "1": ("Add student", lambda: add_student(students)),
        "2": ("View students", lambda: view_students(students)),
        "3": ("View student detail", lambda: view_student_detail(students)),
        "4": ("Edit student", lambda: edit_student(students)),
        "5": ("Delete student", lambda: delete_student(students, attendance)),
        "6": ("Search students", lambda: search_students(students)),
        "7": ("Mark attendance (multiple)", lambda: mark_attendance(students, attendance)),
        "8": ("View attendance by date", lambda: view_attendance_for_date(students, attendance)),
        "9": ("View attendance for student", lambda: view_attendance_for_student(students, attendance)),
        "10": ("Show JSON paths", export_paths),
        "0": ("Exit", None),
    }

    while True:
        print("\n=== Student Management System ===")
        for k in sorted(actions, key=lambda x: (int(x) if x.isdigit() else x)):
            print(f"{k}) {actions[k][0]}")
        choice = input("Select option: ").strip()
        if choice == "0":
            print("Goodbye.")
            break
        action = actions.get(choice)
        if not action:
            print("Invalid selection.")
            continue
        try:
            action[1]()
        except Exception as e:
            print("Error:", e)
        # reload data to keep synchronized with file edits
        students = load_students()
        attendance = load_attendance()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
    except Exception as e:
        print("Unexpected error:", e)
        sys.exit(1)
