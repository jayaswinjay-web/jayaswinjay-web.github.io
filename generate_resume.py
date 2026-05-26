from fpdf import FPDF

class ResumePDF(FPDF):
    def footer(self):
        self.set_y(-10)
        self.set_font('Helvetica', 'I', 6.5)
        self.set_text_color(180, 180, 180)
        self.cell(0, 6, f'Page {self.page_no()}/{{nb}}', align='C')

pdf = ResumePDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=12)
pdf.add_page('P', 'A4')

TEAL = (22, 125, 110)
TEAL_LIGHT = (232, 245, 242)
TEAL_DARK = (14, 90, 80)
DARK = (40, 45, 50)
GRAY = (100, 110, 120)
GRAY_LIGHT = (160, 170, 180)
WHITE = (255, 255, 255)
BORDER = (220, 225, 230)

M = 12
LH = 145
CW = 68
RW = 118
CX = M
RX = M + CW + 8

# Left panel background
pdf.set_fill_color(245, 247, 248)
pdf.rect(M, 0, CW + 4, 297, 'F')

# Header bar
pdf.set_fill_color(*TEAL)
pdf.rect(M, 18, CW + 4 + RW + 8, 38, 'F')
pdf.set_text_color(*WHITE)
pdf.set_font('Helvetica', 'B', 24)
pdf.set_xy(M + 6, 22)
pdf.cell(0, 10, 'ASWIN JAY')
pdf.set_font('Helvetica', '', 9)
pdf.set_xy(M + 6, 34)
pdf.cell(0, 6, 'Founder & CEO at JAY TECH SOLUTIONS')
pdf.set_font('Helvetica', '', 7)
pdf.set_xy(M + 6, 42)
pdf.cell(0, 5, 'Kadayanallur, Tamil Nadu  |  9003368894  |  contact@jaytechsoln.in')
pdf.set_xy(M + 6, 48)
pdf.cell(0, 5, 'github.com/jayaswinjay-web  |  linkedin.com/in/aswinjay-m-543ba0390')

Y = 62

def section_line(x, y, w):
    pdf.set_draw_color(*TEAL)
    pdf.set_line_width(0.8)
    pdf.line(x, y, x + w, y)
    pdf.set_line_width(0.2)

def section_head(title, x, y, w):
    pdf.set_fill_color(*TEAL)
    pdf.rect(x, y - 1, w, 13, 'F')
    pdf.set_text_color(*WHITE)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_xy(x + 4, y + 1)
    pdf.cell(w - 8, 10, title.upper())
    return y + 16

def cv(label, val, x, y, w):
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', 'B', 7.2)
    pdf.set_xy(x, y)
    pdf.cell(16, 3.8, label)
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', '', 7.2)
    pdf.set_xy(x + 16, y)
    pdf.cell(w - 16, 3.8, val)
    return y + 4.2

def bl(text, x, y, w, sz=7.2, indent=3):
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', '', sz)
    pdf.set_xy(x + indent, y)
    pdf.multi_cell(w - indent, 3.6, '\x95 ' + text)
    lines = len(text) / 55 + 1
    return y + lines * 3.6 + 1.2

def exp_hdr(title, meta, co, x, y, w):
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_xy(x, y)
    pdf.cell(w - 45, 4.5, title)
    pdf.set_text_color(*TEAL)
    pdf.set_font('Helvetica', 'B', 7)
    pdf.set_xy(x + w - 45, y)
    pdf.cell(45, 4.5, meta, align='R')
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', 'I', 6.5)
    pdf.set_xy(x, y + 4.5)
    pdf.cell(w, 3.5, co)
    return y + 9.5

# === LEFT COLUMN ===
y = Y

pdf.set_draw_color(*TEAL)
pdf.set_line_width(0.6)
pdf.line(CX + 2, y - 1, CX + CW + 2, y - 1)
pdf.set_line_width(0.2)

y = section_head('Profile', CX, y, CW)
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 7)
pdf.set_xy(CX, y)
pdf.multi_cell(CW, 3.3,
'Student at Ramco Institute of Technology (CSBS)\n'
'and Founder/CEO of JAY TECH SOLUTIONS since age\n'
'15. Built 11+ software products serving 50,000+\n'
'users across India. IBM & PALS merit recipient.')
y += 24

y = section_head('Skills', CX, y, CW)
y = cv('Languages:', 'Python, JS/TS, PHP, C, C#, Go, x86-64 Asm', CX, y, CW)
y = cv('Frameworks:', 'React, Next.js, Laravel, Livewire, WPF .NET', CX, y, CW)
y = cv('Platforms:', 'PostgreSQL, MySQL, Redis, Docker, Git, Linux', CX, y, CW)
y = cv('AI / ML:', 'Gemini API, LLM Integration, AI Chatbots', CX, y, CW)
y = cv('Systems:', 'Compiler Design, NASM, ELF/PE, Win32 API', CX, y, CW)
y = cv('IoT/Embedded:', 'IoT AI apps, Embedded systems, Electronics', CX, y, CW)
y += 3

y = section_head('Education', CX, y, CW)
pdf.set_text_color(*DARK)
pdf.set_font('Helvetica', 'B', 7.2)
pdf.set_xy(CX, y)
pdf.cell(CW, 4, 'B.Tech CSBS')
y += 4.5
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', '', 6.8)
pdf.set_xy(CX, y)
pdf.cell(CW, 3.5, 'Ramco Institute of Technology')
y += 3.8
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 6.5)
pdf.set_xy(CX, y)
pdf.cell(CW, 3.5, '2025 - 2029  |  IBM & PALS Merit')
y += 8.5

y = section_head('Certifications', CX, y, CW)
certs = [
    'IBM India Research Lab & PALS Cert. of Merit',
    'IIT Madras Cert. of Appreciation (SPOC)',
    'GIAC Software Cyber Security (Mar 2026)',
    'Best Business Video Award (Rotary Club)',
    '3rd Prize - IEEE Ignite, Kalasalingam Univ.',
    'JPMorganChase SWE Sim. (Forage, Jan 2026)',
    'Tata GenAI Data Analytics (Forage, Jan 2026)',
    'CommBank Data Science Sim. (Forage, Jan 2026)',
    'Deloitte Australia Cyber Sim. (Forage, Dec 2025)',
]
for c in certs:
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', '', 6.8)
    pdf.set_xy(CX + 1, y)
    pdf.cell(CW - 1, 3.4, '\x95 ' + c)
    y += 3.7

# === RIGHT COLUMN ===
ry = Y

pdf.set_draw_color(*TEAL)
pdf.set_line_width(0.6)
pdf.line(RX, ry - 1, RX + RW, ry - 1)
pdf.set_line_width(0.2)

ry = section_head('Experience', RX, ry, RW)

ry = exp_hdr('Founder & CEO', '2020 - Present', 'JAY TECH SOLUTIONS, Kadayanallur', RX, ry, RW)
ry = bl('Founded at 15. Built 11+ products serving 50K+ users across India.', RX, ry, RW)
ry = bl('Products: JAY AI (Gemini), JAY POS (React/Electron), JAY CRM (Next.js/Prisma), JAY ERP (Laravel), JAY OFFICE (Turborepo suite), VAANJAY (Go/React Native social app), JayVibez (C# WPF music player), JAY LMS, JAY CLOUD, Jay Invoicing, Fake OS, AK CODE.', RX, ry, RW)
ry = bl('Full-stack: conception to deployment. Udyam MSME, zero external funding.', RX, ry, RW)

ry = exp_hdr('Tech Support Specialist', 'May 2024 - Feb 2025', 'RMK Associates, Tenkasi', RX, ry, RW)
ry = bl('Enterprise IT support, troubleshooting, and client management.', RX, ry, RW)

ry += 2
ry = section_head('Key Projects', RX, ry, RW)

pdf.set_fill_color(*TEAL_LIGHT)
pdf.rect(RX, ry, 3, 10, 'F')
pdf.set_text_color(*TEAL_DARK)
pdf.set_font('Helvetica', 'B', 7.5)
pdf.set_xy(RX + 6, ry)
pdf.cell(RW - 6, 4, 'AK CODE  -  Programming Language')
ry += 5.5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 6.8)
pdf.set_xy(RX + 6, ry)
pdf.multi_cell(RW - 6, 3.3, 'x86-64 assembly (NASM). English-like syntax, full stdlib, ELF/PE targets, self-hosting compiler, 37K+ LOC, custom AK IDE.')
ry += 13

pdf.set_fill_color(*TEAL_LIGHT)
pdf.rect(RX, ry, 3, 10, 'F')
pdf.set_text_color(*TEAL_DARK)
pdf.set_font('Helvetica', 'B', 7.5)
pdf.set_xy(RX + 6, ry)
pdf.cell(RW - 6, 4, 'VAANJAY  -  Social Media Super-App')
ry += 5.5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 6.8)
pdf.set_xy(RX + 6, ry)
pdf.multi_cell(RW - 6, 3.3, 'Tamil Nadu social platform. Go (Fiber), React Native (Expo), Next.js 14, WebRTC, PostgreSQL, Redis, Cloudflare R2. Reels, stories, live, DMs, calls, UPI payments.')
ry += 13

pdf.set_fill_color(*TEAL_LIGHT)
pdf.rect(RX, ry, 3, 10, 'F')
pdf.set_text_color(*TEAL_DARK)
pdf.set_font('Helvetica', 'B', 7.5)
pdf.set_xy(RX + 6, ry)
pdf.cell(RW - 6, 4, 'JayVibez  -  Music Player')
ry += 5.5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 6.8)
pdf.set_xy(RX + 6, ry)
pdf.multi_cell(RW - 6, 3.3, 'WPF .NET 8. NAudio + YoutubeExplode. Local library scanning, YouTube streaming, playlists, album art. Android APK available.')
ry += 13

pdf.set_fill_color(*TEAL_LIGHT)
pdf.rect(RX, ry, 3, 10, 'F')
pdf.set_text_color(*TEAL_DARK)
pdf.set_font('Helvetica', 'B', 7.5)
pdf.set_xy(RX + 6, ry)
pdf.cell(RW - 6, 4, 'Fake OS  -  Windows Desktop Simulator')
ry += 5.5
pdf.set_text_color(*GRAY)
pdf.set_font('Helvetica', '', 6.8)
pdf.set_xy(RX + 6, ry)
pdf.multi_cell(RW - 6, 3.3, 'C + Win32 API + GDI. Taskbar, start menu, window management.')
ry += 10

ry += 1
ry = section_head('Achievements', RX, ry, RW)
achievements = [
    'IBM India Research Lab & PALS Certificate of Merit',
    'IIT Madras Certificate of Appreciation (SPOC)',
    '3rd Prize - IEEE Ignite, Kalasalingam University',
    'Best Business Video Award - Rotary Club (2025)',
    'GIAC Software Cyber Security Certified',
    'Udyam-registered MSME (Govt. of India)',
]
for a in achievements:
    pdf.set_text_color(*GRAY)
    pdf.set_font('Helvetica', '', 6.8)
    pdf.set_xy(RX + 2, ry)
    pdf.cell(RW - 2, 3.6, '\x95 ' + a)
    ry += 4

pdf.output('D:/github-projects/jayaswinjay-web.github.io/resume.pdf')
print('PDF generated: resume.pdf')
