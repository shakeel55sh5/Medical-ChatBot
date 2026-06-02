from fpdf import FPDF
import os

class ContinuousReport(FPDF):
    def __init__(self):
        super().__init__()
        self.primary_color = (0, 51, 102)  # Dark Medical Blue
        self.set_auto_page_break(auto=True, margin=15)
        self.screenshot_dir = "screenShot Folder"

    def header(self):
        if self.page_no() > 1:
            self.set_font("helvetica", "B", 10)
            self.set_text_color(*self.primary_color)
            self.cell(0, 10, "PAKISTANI MEDICAL AI CHATBOT - PROJECT REPORT", 0, 0, "L")
            self.set_font("helvetica", "I", 10)
            self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "R")
            self.ln(12)
            self.set_draw_color(*self.primary_color)
            self.line(10, 22, 200, 22)
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, "Medical AI Chatbot Research Report", 0, 0, "L")
        self.cell(0, 10, "June 2026", 0, 0, "R")

    def section_heading(self, title):
        self.ln(8)
        self.set_font("helvetica", "B", 14)
        self.set_text_color(*self.primary_color)
        self.set_fill_color(230, 240, 250)
        self.cell(0, 10, title, 0, 1, "L", fill=True)
        self.ln(4)

    def add_screenshot(self, filename, description):
        self.ln(4)
        img_path = os.path.join(self.screenshot_dir, filename)
        
        if os.path.exists(img_path):
            # Check if image fits on page, else add page
            # Assuming image height approx 60mm
            if self.get_y() > 220:
                self.add_page()
            
            curr_y = self.get_y()
            # Center the image
            self.image(img_path, x=25, y=curr_y, w=160)
            self.set_y(curr_y + 95) # Adjust based on image aspect ratio/height
            self.set_font("helvetica", "I", 9)
            self.set_text_color(100, 100, 100)
            self.cell(0, 10, f"Figure: {description}", 0, 1, "C")
            self.ln(2)
        else:
            # Fallback to placeholder if file missing
            self.set_draw_color(180, 180, 180)
            self.set_fill_color(250, 250, 250)
            curr_y = self.get_y()
            if curr_y > 220:
                self.add_page()
                curr_y = self.get_y()
            self.rect(15, curr_y, 180, 60, "DF")
            self.set_y(curr_y + 20)
            self.set_font("helvetica", "B", 11)
            self.set_text_color(100, 100, 100)
            self.cell(0, 10, f"[ MISSING SCREENSHOT: {filename} ]", 0, 1, "C")
            self.set_y(curr_y + 65)

def create_report():
    pdf = ContinuousReport()
    
    # --- Title Page ---
    pdf.add_page()
    pdf.set_draw_color(*pdf.primary_color)
    pdf.rect(5, 5, 200, 287)
    pdf.ln(60)
    pdf.set_font("helvetica", "B", 26)
    pdf.set_text_color(*pdf.primary_color)
    pdf.multi_cell(0, 15, "PAKISTANI MEDICAL AI CHATBOT\nUSING MACHINE LEARNING", 0, "C")
    pdf.ln(20)
    pdf.set_font("helvetica", "B", 18)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Final Year Project Report", 0, 1, "C")
    pdf.ln(40)
    pdf.set_font("helvetica", "", 14)
    pdf.multi_cell(0, 10, "Submitted By:\nStudent Name: ____________________\nRegistration No: ____________________\nDepartment: Computer Science\n\nSubmitted To:\nSupervisor: ____________________", 0, "C")

    # --- Abstract & Table of Contents ---
    pdf.add_page()
    pdf.section_heading("ABSTRACT")
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 7, "The Pakistani Medical AI Chatbot is an intelligent healthcare assistance system developed using Python and Machine Learning techniques. The chatbot analyzes user-provided symptoms and predicts possible diseases using a Random Forest Classification model. The system then recommends suitable Pakistani medicine brands and suggests an appropriate doctor specialization.\n\nThe primary objective is to provide quick preliminary healthcare guidance while emphasizing that professional medical consultation remains essential.")
    
    pdf.section_heading("TABLE OF CONTENTS")
    pdf.set_font("helvetica", "", 10)
    sections = ["1. Introduction", "2. Problem Statement", "3. Objectives", "4. Literature Review", "5. System Analysis", "6. System Design", "7. Methodology", "8. Technologies Used", "9. Implementation", "10. Screenshots", "11. Testing", "12. Advantages", "13. Conclusion", "Appendix A: Source Code"]
    for s in sections:
        pdf.cell(0, 7, s, 0, 1)

    # --- Main Content (Continuous) ---
    content = [
        ("1. INTRODUCTION", "Artificial Intelligence is revolutionizing healthcare. This project uses NLP and Machine Learning to provide a conversational interface for medical guidance, specifically localized for the Pakistani context with relevant medicine brands."),
        ("2. PROBLEM STATEMENT", "Access to immediate medical advice is limited in many areas. This system provides a fast, ML-driven alternative for preliminary symptom analysis."),
        ("3. OBJECTIVES", "- Build an AI chatbot using Python.\n- Predict diseases from symptoms with high accuracy.\n- Provide Pakistani medicine recommendations.\n- Recommend specialist doctors."),
        ("4. LITERATURE REVIEW", "Medical chatbots like Ada and Babylon set the standard. This project adopts Random Forest for its robust classification capabilities in high-dimensional symptom data."),
        ("5. SYSTEM ANALYSIS", "Manual systems are slow. This proposed system is automated, provides instant results, and is customized for local medicine availability."),
        ("6. SYSTEM DESIGN", "The system uses a modular architecture: CLI for interaction, TF-IDF for vectorization, and Random Forest for intelligence."),
        ("7. METHODOLOGY", "Data is sourced from medical databases. Symptoms are processed using Scikit-Learn's TfidfVectorizer and classified by RandomForestClassifier."),
        ("8. TECHNOLOGIES USED", "Python 3.10+, Scikit-Learn, FPDF2, VS Code."),
        ("9. IMPLEMENTATION", "Implementation involves model training on 10+ disease categories with mapping to Pakistani brands like Panadol, Arinac, and Augmentin."),
    ]

    for title, text in content:
        pdf.section_heading(title)
        pdf.set_font("helvetica", "", 11)
        pdf.multi_cell(0, 7, text)

    # --- Screenshots (Integrated) ---
    pdf.section_heading("10. SCREENSHOTS & VISUAL EVIDENCE")
    pdf.add_screenshot("Folder_Structure.png", "Project Folder Structure")
    pdf.add_screenshot("welcome_Screen.png", "Chatbot Welcome Screen and Startup")
    pdf.add_screenshot("Disease_Prediction_Result.png", "Symptom Analysis and Disease Prediction Output")
    pdf.add_screenshot("no_Fever.png", "Negation Detection Logic (Handling 'no fever' input)")
    pdf.add_screenshot("Exit_Screen.png", "Chatbot System Exit and Farewell")

    # --- Final Sections ---
    pdf.section_heading("11. TESTING AND RESULTS")
    pdf.set_font("helvetica", "", 11)
    pdf.multi_cell(0, 7, "Tested for accuracy in prediction and robustness in handling negative inputs. The model successfully identifies diseases like Flu, Migraine, and Gastritis. All screenshots above validate the functional requirements.")

    pdf.section_heading("12. ADVANTAGES & LIMITATIONS")
    pdf.multi_cell(0, 7, "Advantages: Fast, localized, and free.\nLimitations: Small dataset, not a replacement for clinical diagnosis.")

    pdf.section_heading("13. CONCLUSION")
    pdf.multi_cell(0, 7, "This project successfully demonstrates the utility of ML in the Pakistani healthcare sector.")

    # --- Appendices ---
    pdf.section_heading("APPENDIX A: SOURCE CODE")
    pdf.set_font("courier", "", 8)
    with open("medical_bot.py", "r") as f:
        pdf.multi_cell(0, 4, f.read())

    pdf.section_heading("APPENDIX B: DATASET")
    with open("medical_data.py", "r") as f:
        pdf.multi_cell(0, 4, f.read())

    pdf.output("Medical_Chatbot_Report.pdf")
    print("PDF Report with Integrated Screenshots generated successfully.")

if __name__ == "__main__":
    create_report()
