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

left_x = 15
right_x = 80
col_w = 80
full_w = 180
right_w = 115
rx = 88

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
pdf.cell(65, 4, 'github.com/jayaswinjay-web')
y += 5
pdf.set_xy(14, y)
pdf.cell(65, 4, 'linkedin.com/in/aswinjay-m-543ba0390')
y += 14

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
'Built 11+ software products serving 50,000+ users across India. '
'Experienced in full-stack development, AI/ML, systems programming, '
'IoT, and embedded electronics. '
'Recipient of IBM India Research Lab & PALS Certificate of Merit, '
'and IIT Madras Certificate of Appreciation.')
y += 36

pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 10)
pdf.set_xy(14, y)
pdf.cell(65, 6, 'SKILLS')
pdf.line(14, y+7, 78, y+7)
y += 14

skills_data = [
    ('Languages', 'Python, JavaScript, TypeScript, PHP,\nHTML/CSS, C, C#, x86-64 Assembly,\nAK CODE (own language)'),
    ('Frameworks', 'Next.js, React, Laravel, Livewire,\nElectron, Node.js, WPF .NET,\nGoogle Gemini API, Prisma'),
    ('Platforms', 'Go (Fiber), PostgreSQL, MySQL, Redis,\nCloudflare R2, Docker, Git/GitHub,\nLinux, Win32 API, NASM'),
    ('Specialized', 'Compiler Design, IoT & Embedded Systems,\nAI/ML Integration, WebRTC,\nSystems Programming, Business Software,\nElectronics & Electrical'),
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
    'Best Business Video Award - Rotary Club (Nov 2025)',
    '3rd Prize - IEEE Ignite, Kalasalingam University',
    'JPMorganChase - SWE Job Simulation (Forage)',
    'Tata - GenAI Data Analytics Job Simulation (Forage)',
    'CommBank - Data Science Job Simulation (Forage)',
    'Deloitte Australia - Cyber Job Simulation (Forage)',
    'Udyam Registered MSME',
]
for c in certs:
    pdf.set_text_color(*DARK)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_xy(16, y)
    pdf.cell(62, 4, '- ' + c)
    y += 4.5

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
    'Founded and scaled a business software company from scratch at age 15 (class 11).',
    'Designed, developed, and deployed 11+ software products serving 50,000+ users across India.',
    'Built JAY AI (Gemini API chatbot), JAY POS (React/Electron), JAY CRM (Next.js), JAY ERP (Laravel), JAY OFFICE (Turborepo suite), VAANJAY (Go/React Native social app), JayVibez (C# WPF music player), JAY LMS, JAY CLOUD, Jay Invoicing, Fake OS, and AK CODE programming language.',
    'Managed full product lifecycle: conception, architecture, development, deployment, and support.',
    'Registered as Udyam MSME - fully bootstrapped with zero external funding.',
], ry)

ry = exp_item('Technical Support Specialist', 'May 2024 - Feb 2025', 'RMK Associates, Tenkasi', [
    'Provided technical support and IT solutions for enterprise clients.',
    'Gained hands-on experience in enterprise IT operations, troubleshooting, and client relationship management.',
    'Developed strong problem-solving skills in a fast-paced professional environment.',
], ry)

ry += 2
pdf.set_text_color(*TEAL)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_xy(rx, ry)
pdf.cell(right_w, 7, 'KEY PROJECTS')
pdf.set_draw_color(*TEAL)
pdf.line(rx, ry+8, rx+right_w, ry+8)
ry += 16

ry = exp_item('AK CODE - Programming Language', 'Ongoing', 'Personal Project', [
    'Ground-up programming language with x86-64 assembly bootstrap compiler (NASM). Targets Linux ELF and Windows PE/COFF.',
    'Natural English-like syntax with full standard library: AI/ML, web server, database, math, UI modules.',
    'Includes custom IDE (AK IDE) with multi-agent AI panel for code review, refactoring, testing.',
    '37K+ lines of code, 100+ language features, 2 architecture targets.',
], ry)

ry = exp_item('VAANJAY - Social Media Super-App', 'Ongoing', 'Personal Project', [
    'Production-ready social platform combining Instagram, WhatsApp, Facebook, Twitter for Tamil Nadu.',
    'Built with Go (Fiber), React Native (Expo), Next.js 14, WebRTC, PostgreSQL, Redis, Cloudflare R2.',
    'Features: reels, stories, live streams, DMs, group chats, audio/video calls, UPI payments, Tamil calendar.',
], ry)

ry = exp_item('JayVibez - Music Player', 'Ongoing', 'Personal Project', [
    'WPF .NET 8 desktop music player with local library scanning and YouTube streaming via YoutubeExplode.',
    'NAudio playback engine with playlist management, album art, shuffle/repeat, queue management.',
    'Online/offline modes. Also available as an Android APK.',
], ry)

ry = exp_item('JAY Product Suite', '2020 - Present', 'JAY TECH SOLUTIONS', [
    'JAY AI: AI chatbot & automation platform using Python and Google Gemini API.',
    'JAY POS: Enterprise point-of-sale with React, TypeScript, Electron, and Supabase.',
    'JAY CRM: Next.js-based customer relationship management with Prisma ORM.',
    'JAY ERP: Laravel-based ERP with 60+ modules and Anna AI assistant.',
    'JAY OFFICE: Turborepo monorepo office suite (Docs, Sheets, Slides, Mail, Drive, Meet, Chat).',
    'JAY CLOUD: Scalable cloud infrastructure platform.',
], ry)

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
    'Awarded Certificate of Merit by IBM India Research Lab & PALS (IIT Alumni) for LLM Systems (2024)',
    'Certificate of Appreciation from IIT Madras as SPOC for the School Connect Program',
    '3rd Prize (Second Runner-Up) - IEEE Ignite, Kalasalingam University (cash prize INR 2,500)',
    'Best Business Video Award - Rotary Club of Virudhunagar & Punch Gurukulam Training Program 53.0 (2025)',
    'GIAC Software Cyber Security certification - ShikshaVertex (Mar 2026)',
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

pdf.output('D:/github-projects/jayaswinjay-web.github.io/resume.pdf')
print('PDF generated: resume.pdf')
