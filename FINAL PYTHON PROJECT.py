# Query: FINAL PYTHON PROJECT
# Flags: RegExp
# ContextLines: 1

class Patient:
    def _init_(self, id, name, age, gender, diagnosis):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

class HospitalSystem:
    def _init_(self):
        self.patients = []

    def add_patient(self, id, name, age, gender, diagnosis):
        patient = Patient(id, name, age, gender, diagnosis)
        self.patients.append(patient)
        print("Patient added successfully!")

    def view_all_patients(self):
        print("All Patients:")
        for patient in self.patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Diagnosis: {patient.diagnosis}")

    def search_patient_by_id(self, id):
        for patient in self.patients:
            if patient.id == id:
                print(f"Patient found with ID {id}: Name - {patient.name}, Age - {patient.age}, Gender - {patient.gender}, Diagnosis - {patient.diagnosis}")
                return
        print(f"No patient found with ID {id}.")

    def search_patient_by_name(self, name):
        found = False
        for patient in self.patients:
            if patient.name.lower() == name.lower():
                print(f"Patient found with Name {name}: ID - {patient.id}, Age - {patient.age}, Gender - {patient.gender}, Diagnosis - {patient.diagnosis}")
                found = True
        if not found:
            print(f"No patient found with Name {name}.")

def main():
    hospital = HospitalSystem()
    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient by ID")
        print("4. Search Patient by Name")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            diagnosis = input("Enter patient diagnosis: ")
            hospital.add_patient(id, name, age, gender, diagnosis)
        elif choice == '2':
            hospital.view_all_patients()
        elif choice == '3':
            id = input("Enter patient ID to search: ")
            hospital.search_patient_by_id(id)
        elif choice == '4':
            name = input("Enter patient name to search: ")
            hospital.search_patient_by_name(name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    main()
