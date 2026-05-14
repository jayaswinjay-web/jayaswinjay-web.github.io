from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        pass
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(150,150,150)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

pdf = ResumePDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page('P', 'A4')

TEAL = (26, 138, 122)
DARK = (30, 39, 46)
GRAY = (90, 101, 112)
LIGHT_BG = (244, 246, 248)

# HEADER
pdf.set_fill_color(*TEAL)
pdf.rect(0, 0, 210, 50, 'F')
pdf.set_text_color(255,255,255)
pdf.set_font('Helvetica', 'B', 22)
pdf.set_xy(20, 12)
pdf.cell(0, 10, 'ASWIN JAY')
pdf.set_font('Helvetica', '', 11)
pdf.set_xy(20, 26)
pdf.cell(0, 8, 'Founder & CEO at JAY TECH SOLUTIONS')
pdf.set_font('Helvetica', '', 9)
pdf.set_xy(20, 36)
pdf.cell(0, 6, 'contact@jaytechsoln.in  |  Kadayanallur, Tamil Nadu  |  9003368894')

# LEFT COLUMN
left_x = 15
right_x = 80
col_w = 80
full_w = 180
right_w = 115
rx = 88

# Left column background
pdf.set_fill_color(*LIGHT_BG)
pdf.rect(10, 50, 72, 238, 'F')

y = 58
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_xy(14, y)
pdf.cell(65, 6, 'CONTACT')
pdf.set_draw_color(*TEAL)
pdf.line(14, y+7, 78, y+7)
y += 14

pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 8)
pdf.set_xy(14, y)
pdf.cell(65, 4, 'contact@jaytechsoln.in')
y += 5
pdf.set_xy(14, y)
pdf.cell(65, 4, '9003368894')
y += 5
pdf.set_xy(14, y)
pdf.multi_cell(65, 4, 'Kadayanallur,\nTenkasi District,\nTamil Nadu - 627806')
y += 16
pdf.set_xy(14, y)
pdf.cell(65, 4, 'github.com/Aswinajay')
y += 5
pdf.set_xy(14, y)
pdf.cell(65, 4, 'linkedin.com/in/aswinjay-m-543ba0390')
y += 14

# SUMMARY
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_xy(14, y)
pdf.cell(65, 6, 'SUMMARY')
pdf.line(14, y+7, 78, y+7)
y += 14
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 7.5)
pdf.set_xy(14, y)
pdf.multi_cell(65, 3.8,
'Student at Ramco Institute of Technology (CSBS) and '
'Founder/CEO of JAY TECH SOLUTIONS since age 15. '
'Built 7+ software products serving 50,000+ users across India. '
'Recipient of IBM India Research Lab & PALS Certificate of Merit, '
'and IIT Madras Certificate of Appreciation.')
y += 36

# SKILLS
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_xy(14, y)
pdf.cell(65, 6, 'SKILLS')
pdf.line(14, y+7, 78, y+7)
y += 14

skills_data = [
    ('Languages', 'Python, JavaScript, PHP, HTML/CSS, C,\nx86-64 Assembly, AK CODE (own language)'),
    ('Frameworks', 'Next.js, Laravel, Electron, React, Node.js,\nGoogle Gemini API'),
    ('Platforms', 'MySQL, Cloud Infrastructure, Linux,\nGit/GitHub, Windows API, NASM'),
    ('Specialized', 'Compiler Design, OS Development,\nAI/ML Integration, Systems Programming,\nBusiness Software'),
]
for title, sk in skills_data:
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_xy(14, y)
    pdf.cell(65, 5, title)
    y += 5.5
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_xy(14, y)
    pdf.multi_cell(65, 3.5, sk)
    y += len(sk.split('\n')) * 3.5 + 3

y += 3
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_xy(14, y)
pdf.cell(65, 6, 'EDUCATION')
pdf.line(14, y+7, 78, y+7)
y += 14
pdf.set_text_color(*DARK)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_xy(14, y)
pdf.multi_cell(65, 4, 'B.Tech Computer Science &\nBusiness Systems')
y += 9
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', '', 8)
pdf.set_xy(14, y)
pdf.cell(65, 4, '2025 - 2029 (Expected)')
y += 5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 7.5)
pdf.set_xy(14, y)
pdf.cell(65, 4, 'Ramco Institute of Technology')
y += 4
pdf.set_xy(14, y)
pdf.multi_cell(65, 3.5, 'Rajapalayam, Tamil Nadu\nIBM & PALS Merit Recipient')
y += 10

pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_xy(14, y)
pdf.cell(65, 6, 'CERTIFICATIONS')
pdf.line(14, y+7, 78, y+7)
y += 14
certs = [
    'IIT Madras - Certificate of Appreciation (SPOC)',
    'IBM India Research Lab & PALS - Certificate of Merit',
    'GIAC Software Cyber Security - ShikshaVertex (Mar 2026)',
    'JPMorganChase - Software Engineering Job Simulation (Forage)',
    'Tata - GenAI Powered Data Analytics Job Simulation (Forage)',
    'Commonwealth Bank - Data Science Job Simulation (Forage)',
    'Deloitte Australia - Cyber Job Simulation (Forage)',
    '3rd Prize - IEEE Ignite, Kalasalingam University',
    'Best Business Video Award - Rotary Club',
    'Udyam Registered MSME',
]
for c in certs:
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_xy(16, y)
    pdf.cell(62, 4, '- ' + c)
    y += 4.5

# RIGHT COLUMN - EXPERIENCE
ry = 58

pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_xy(rx, ry)
pdf.cell(right_w, 7, 'WORK EXPERIENCE')
pdf.set_draw_color(*TEAL)
pdf.line(rx, ry+8, rx+right_w, ry+8)
ry += 16

def exp_item(title, meta, company, bullets, ry):
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_xy(rx, ry)
    pdf.cell(right_w, 5, title)
    ry += 5.5
    pdf.set_text_color(*TEAL)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_xy(rx, ry)
    pdf.cell(right_w, 4, meta)
    ry += 4.5
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', 'I', 8)
    pdf.set_xy(rx, ry)
    pdf.cell(right_w, 4, company)
    ry += 6
    pdf.set_font('Helvetica', '', 7.8)
    for b in bullets:
        pdf.set_xy(rx+3, ry)
        pdf.multi_cell(right_w-3, 3.8, '- ' + b)
        ry += len(b) // 60 * 3.8 + 5
    return ry + 4

ry = exp_item('Founder & CEO', '2020 - Present', 'JAY TECH SOLUTIONS', [
    'Founded and scaled a business software company from scratch at age 15 while in class 11.',
    'Designed, developed, and deployed 7+ software products serving 50,000+ users across India.',
    'Built JAY AI (Gemini API chatbot), JAY POS (Electron), JAY CRM (Next.js), JAY ERP (Laravel), JAY CLOUD, JAY OFFICE, and Jay Invoicing.',
    'Managed full product lifecycle: conception, architecture, development, deployment, and support.',
    'Registered as Udyam MSME - fully bootstrapped with zero external funding.',
], ry)

ry = exp_item('Technical Support Specialist', 'May 2024 - Feb 2025', 'RMK Associates, Tenkasi', [
    'Provided technical support and IT solutions for enterprise clients.',
    'Gained hands-on experience in enterprise IT operations, troubleshooting, and client relationship management.',
    'Developed strong problem-solving skills in a fast-paced professional environment.',
], ry)

# KEY PROJECTS
ry += 2
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_xy(rx, ry)
pdf.cell(right_w, 7, 'KEY PROJECTS')
pdf.set_draw_color(*TEAL)
pdf.line(rx, ry+8, rx+right_w, ry+8)
ry += 16

ry = exp_item('AK CODE - Programming Language', 'Ongoing', 'Personal Project', [
    'Ground-up programming language with x86-64 assembly bootstrap compiler (NASM). Targets Linux ELF and Windows PE/COFF natively.',
    'Natural English-like syntax with full standard library: AI/ML, web server, database, math, UI modules.',
    'Includes custom IDE (AK IDE) with multi-agent AI panel for code review, refactoring, testing.',
    'Spec: 900+ lines, 100+ language features, 2 architecture targets.',
], ry)

ry = exp_item('Fake OS - Windows Desktop Simulator', 'Ongoing', 'Personal Project', [
    'Windows-like desktop environment simulator built in C using Win32 API.',
    'Features gradient desktop rendering, taskbar, start menu, and window management via GDI.',
    'Demonstrates low-level systems programming and Windows platform expertise.',
], ry)

ry = exp_item('JAY Product Suite', '2020 - Present', 'JAY TECH SOLUTIONS', [
    'JAY AI: AI chatbot & automation platform using Python and Google Gemini API.',
    'JAY POS: Enterprise point-of-sale system with Electron, inventory management, billing.',
    'JAY CRM: Next.js-based customer relationship management platform.',
    'JAY ERP: Laravel-based enterprise resource planning system.',
    'JAY CLOUD: Scalable cloud infrastructure platform.',
    'JAY OFFICE: Monorepo office productivity suite.',
], ry)

# ACHIEVEMENTS
ry += 2
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_xy(rx, ry)
pdf.cell(right_w, 7, 'ACHIEVEMENTS')
pdf.set_draw_color(*TEAL)
pdf.line(rx, ry+8, rx+right_w, ry+8)
ry += 16

pdf.set_text_color(*DARK)
pdf.set_font('Helvetica', '', 8)
achievements = [
    'Awarded Certificate of Merit by IBM India Research Lab & PALS (IIT Alumni initiative) for LLM Systems (2024)',
    'Certificate of Appreciation from IIT Madras as SPOC for the School Connect Program',
    '3rd Prize (Second Runner-Up) - IEEE Ignite, Kalasalingam University (cash prize INR 2,500)',
    'Best Business Video Award - Rotary Club of Virudhunagar & Punch Gurukulam Training Program 53.0 (2025)',
    'Udyam Registered MSME - JAY TECH SOLUTIONS (Govt. of India)',
]
for a in achievements:
    pdf.set_xy(rx+3, ry)
    pdf.multi_cell(right_w-3, 3.8, '- ' + a)
    ry += len(a) // 80 * 3.8 + 4.5

pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', 'I', 7.5)
pdf.set_xy(rx, ry+6)
pdf.cell(right_w, 4, 'Available for remote collaboration worldwide.')

pdf.output('D:/weki pidea/resume.pdf')
print('PDF generated: D:/weki pidea/resume.pdf')
