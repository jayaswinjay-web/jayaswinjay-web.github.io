from fpdf import FPDF

class ResumePDF(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.set_text_color(160, 160, 160)
        self.cell(0, 8, f'Page {self.page_no()}/{{nb}}', align='C')

pdf = ResumePDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page('P', 'A4')

TEAL = (26, 138, 122)
DARK = (30, 39, 46)
GRAY = (100, 110, 120)
WHITE = (255, 255, 255)

W = 190
M = 10
CX = M
RX = 110

pdf.set_fill_color(*TEAL)
pdf.rect(0, 0, 210, 38, 'F')
pdf.set_text_color(*WHITE)
pdf.set_font('Helvetica', 'B', 20)
pdf.set_xy(M, 8)
pdf.cell(0, 8, 'ASWIN JAY')
pdf.set_font('Helvetica', '', 10)
pdf.set_xy(M, 19)
pdf.cell(0, 6, 'Founder & CEO at JAY TECH SOLUTIONS')
pdf.set_font('Helvetica', '', 7.5)
pdf.set_xy(M, 27)
pdf.cell(0, 5, 'Kadayanallur, Tamil Nadu  |  9003368894  |  contact@jaytechsoln.in')
pdf.set_xy(M + 130, 27)
pdf.cell(0, 5, 'github.com/jayaswinjay-web  |  linkedin.com/in/aswinjay-m-543ba0390')

Y = 45

def section(title, x, w, y):
    pdf.set_text_color(*TEAL)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_xy(x, y)
    pdf.cell(w, 5, title.upper())
    pdf.set_draw_color(*TEAL)
    pdf.line(x, y + 5.5, x + w, y + 5.5)
    return y + 9

def skill_line(label, items, x, y, w):
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_xy(x, y)
    pdf.cell(18, 4, label)
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_xy(x + 18, y)
    pdf.cell(w - 18, 4, items)
    return y + 4.5

def bullet(text, x, y, w, size=7.5):
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', '', size)
    pdf.set_xy(x + 2, y)
    pdf.multi_cell(w - 2, 3.8, '\x95 ' + text)
    return y + (len(text) // 70 + 1) * 3.8 + 1.5

def exp_header(title, meta, company, x, y, w):
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_xy(x, y)
    pdf.cell(w, 4.5, title)
    pdf.set_text_color(*TEAL)
    pdf.set_font('Helvetica', 'B', 7)
    pdf.set_xy(x + w - 50, y)
    pdf.cell(50, 4.5, meta, align='R')
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', 'I', 7)
    pdf.set_xy(x, y + 4.5)
    pdf.cell(w, 4, company)
    return y + 9

# LEFT COLUMN
pdf.set_fill_color(248, 249, 250)
pdf.rect(M, Y - 4, 95, 245, 'F')

left = M + 3
lw = 89
y = Y

y = section('Summary', left, lw, y)
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(left, y)
pdf.multi_cell(lw, 3.5,
'Student at Ramco Institute of Technology (CSBS) and '
'Founder/CEO of JAY TECH SOLUTIONS since age 15. '
'Built 11+ software products serving 50,000+ users across India. '
'Skilled in full-stack development, AI/ML, systems programming, '
'IoT, and embedded electronics. '
'IBM India Research Lab & PALS Certificate of Merit recipient.')
y += 28

y = section('Skills', left, lw, y)
y = skill_line('Languages:', 'Python, JS/TS, PHP, C, C#, Go, x86-64 Assembly', left, y, lw)
y = skill_line('Frameworks:', 'React, Next.js, Laravel, Livewire, Electron, WPF .NET', left, y, lw)
y = skill_line('Platforms:', 'PostgreSQL, MySQL, Redis, Docker, Git, Linux', left, y, lw)
y = skill_line('AI/ML:', 'Gemini API, LLM Integration, AI Chatbots', left, y, lw)
y = skill_line('Systems:', 'Compiler Design, NASM, ELF/PE, Win32 API, GDI', left, y, lw)
y = skill_line('IoT/Electronics:', 'IoT-based AI apps, Embedded systems, Electronics', left, y, lw)
y += 2

y = section('Education', left, lw, y)
pdf.set_text_color(*DARK)
pdf.set_font('Helvetica', 'B', 7.5)
pdf.set_xy(left, y)
pdf.cell(lw, 4, 'B.Tech CSBS - Ramco Institute of Technology')
y += 4.5
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', '', 7)
pdf.set_xy(left, y)
pdf.cell(lw, 3.5, '2025 - 2029 (Expected)  |  IBM & PALS Merit')
y += 4.5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', 'I', 7)
pdf.set_xy(left, y)
pdf.cell(lw, 3.5, 'Rajapalayam, Tamil Nadu')
y += 6

y = section('Certifications', left, lw, y)
certs = [
    'IBM India Research Lab & PALS - Cert. of Merit',
    'IIT Madras - Certificate of Appreciation (SPOC)',
    'GIAC Software Cyber Security - Mar 2026',
    'Best Business Video - Rotary Club, Nov 2025',
    '3rd Prize - IEEE Ignite, Kalasalingam Univ.',
    'JPMorganChase SWE Job Simulation - Forage',
    'Tata GenAI Data Analytics - Forage',
    'CommBank Data Science - Forage',
    'Deloitte Australia Cyber - Forage',
]
for c in certs:
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', '', 7)
    pdf.set_xy(left + 1, y)
    pdf.cell(lw - 1, 3.5, '\x95 ' + c)
    y += 3.8

# RIGHT COLUMN
ry = Y
rw = 82

ry = section('Experience', RX, rw, ry)

ry = exp_header('Founder & CEO', '2020 - Present', 'JAY TECH SOLUTIONS', RX, ry, rw)
ry = bullet('Founded company at 15. Built 11+ products serving 50K+ users across India.', RX, ry, rw)
ry = bullet('Products: JAY AI (Gemini), JAY POS (React/Electron), JAY CRM (Next.js), JAY ERP (Laravel), JAY OFFICE (Turborepo), VAANJAY (Go/React Native), JayVibez (C# WPF), JAY LMS, & more.', RX, ry, rw)
ry = bullet('Full-stack dev: conception through deployment. Udyam MSME, bootstrapped.', RX, ry, rw)

ry = exp_header('Tech Support Specialist', 'May 2024 - Feb 2025', 'RMK Associates, Tenkasi', RX, ry, rw)
ry = bullet('Enterprise IT support, troubleshooting, and client relationship management.', RX, ry, rw)

ry += 2
ry = section('Key Projects', RX, rw, ry)

pdf.set_text_color(*DARK)
pdf.set_font('Helvetica', 'B', 8)
pdf.set_xy(RX, ry)
pdf.cell(rw, 4, 'AK CODE')
ry += 4.5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(RX, ry)
pdf.multi_cell(rw, 3.5, 'Programming language in x86-64 assembly (NASM). English-like syntax, full stdlib, ELF/PE targets, self-hosting compiler, 37K+ LOC, custom IDE.')
ry += 14

pdf.set_text_color(*DARK)
pdf.set_font('Helvetica', 'B', 8)
pdf.set_xy(RX, ry)
pdf.cell(rw, 4, 'VAANJAY')
ry += 4.5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(RX, ry)
pdf.multi_cell(rw, 3.5, 'Social super-app for Tamil Nadu. Go (Fiber), React Native, Next.js, WebRTC, PostgreSQL, Redis. Reels, stories, live, DMs, calls, UPI.')
ry += 14

pdf.set_text_color(*DARK)
pdf.set_font('Helvetica', 'B', 8)
pdf.set_xy(RX, ry)
pdf.cell(rw, 4, 'JayVibez')
ry += 4.5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(RX, ry)
pdf.multi_cell(rw, 3.5, 'WPF .NET 8 music player. NAudio, YoutubeExplode, TagLibSharp. Local + YouTube streaming, playlists, album art. Android APK available.')
ry += 14

pdf.set_text_color(*DARK)
pdf.set_font('Helvetica', 'B', 8)
pdf.set_xy(RX, ry)
pdf.cell(rw, 4, 'Fake OS')
ry += 4.5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(RX, ry)
pdf.multi_cell(rw, 3.5, 'Windows desktop simulator in C (Win32 API, GDI). Taskbar, start menu, window management.')
ry += 12

ry += 1
ry = section('Achievements', RX, rw, ry)
achievements = [
    'IBM India Research Lab & PALS Certificate of Merit (LLM Systems)',
    'IIT Madras Certificate of Appreciation as SPOC',
    '3rd Prize - IEEE Ignite, Kalasalingam Univ. (INR 2,500)',
    'Best Business Video Award - Rotary Club (2025)',
    'GIAC Software Cyber Security Certified',
    'Udyam-registered MSME (Govt. of India)',
]
for a in achievements:
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', '', 7)
    pdf.set_xy(RX + 1, ry)
    pdf.cell(rw - 1, 3.8, '\x95 ' + a)
    ry += 4.2

pdf.output('D:/github-projects/jayaswinjay-web.github.io/resume.pdf')
print('PDF generated: resume.pdf')
